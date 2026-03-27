import uuid
import datetime

from core.rules_engine import RulesEngine
from core.config_loader import ConfigLoader
from core.state_manager import StateManager
from core.audit_logger import AuditLogger
from core.failure_handler import FailureHandler


class WorkflowExecutor:
    def __init__(self, workflow_file="workflow.yaml", rules_file="rules.yaml"):
        loader = ConfigLoader()
        self.workflow = loader.load_workflow(workflow_file)
        self.rules_config = loader.load_rules(rules_file)

        self.rules_engine = RulesEngine(self.rules_config)
        self.state_manager = StateManager()
        self.audit_logger = AuditLogger()
        self.failure_handler = FailureHandler()


    def execute(self, request_data: dict):
        request_id = str(uuid.uuid4())

        # Check for duplicate requests
        if self.failure_handler.check_duplicate(request_id):
            return {"state": {"request_id": request_id, "status": "duplicate"}, "audit": []}

        state = {
            "request_id": request_id,
            "workflow": self.workflow["workflow"],
            "status": "in_progress"
        }

        for stage in self.workflow["stages"]:
            try:
                stage_result = self._execute_stage(stage, request_data)
            except Exception:
                stage_result = self.failure_handler.handle_dependency_failure(stage["name"])

            self.audit_logger.log(
                request_id,
                stage["name"],
                stage_result.get("rule"),
                stage_result["status"],
                stage_result.get("message", "")
            )

            if stage_result.get("status") == "fail":
                if "fallback" in stage:
                    state["status"] = "manual_review"
                else:
                    state["status"] = "rejected"
                break

        if state["status"] == "in_progress":
            state["status"] = "approved"

        self.state_manager.save_state(request_id, state["workflow"], state["status"])
        return {"state": state, "audit": self.audit_logger.get_logs(request_id)}

    def _execute_stage(self, stage, data):
        results = []
        for rule_id in stage.get("rules", []):
            result = self.rules_engine.evaluate_rule(rule_id, data)
            results.append(result)
            if result["status"] == "fail":
                return result
        return {"stage": stage["name"], "status": "pass", "details": results}
