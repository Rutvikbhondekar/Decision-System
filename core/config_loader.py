import yaml
import os

class ConfigLoader:
    def __init__(self, base_path="config"):
        self.base_path = base_path

    def load_workflow(self, workflow_file="workflow.yaml"):
        path = os.path.join(self.base_path, "workflows", workflow_file)
        with open(path, "r") as f:
            return yaml.safe_load(f)

    def load_rules(self, rules_file="rules.yaml"):
        path = os.path.join(self.base_path, "rules", rules_file)
        with open(path, "r") as f:
            return yaml.safe_load(f)
