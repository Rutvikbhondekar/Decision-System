class RulesEngine:
    def __init__(self, rules_config):
        # Store rules in a dictionary for quick lookup
        self.rules = {rule["id"]: rule for rule in rules_config["rules"]}

    def evaluate_rule(self, rule_id, data):
        rule = self.rules.get(rule_id)
        if not rule:
            return {"rule": rule_id, "status": "error", "message": "Rule not found"}

        if rule["type"] == "presence":
            missing = [f for f in rule["fields"] if f not in data]
            if missing:
                return {"rule": rule_id, "status": "fail", "message": rule["error"]}
            return {"rule": rule_id, "status": "pass"}

        elif rule["type"] == "threshold":
            value = data.get(rule["field"])
            if value is None or not self._compare(value, rule["operator"], rule["value"]):
                return {"rule": rule_id, "status": "fail", "message": rule["error"]}
            return {"rule": rule_id, "status": "pass"}

        elif rule["type"] == "conditional":
            # Safer evaluation: only handle simple boolean flags
            condition = rule["condition"]
            if condition == "flagged == true" and data.get("flagged") is True:
                return {
                    "rule": rule_id,
                    "status": "fail",
                    "message": "Condition triggered",
                    "action": rule.get("action")
                }
            return {"rule": rule_id, "status": "pass"}

        return {"rule": rule_id, "status": "unknown"}

    def _compare(self, left, operator, right):
        if operator == ">=": return left >= right
        if operator == ">": return left > right
        if operator == "<=": return left <= right
        if operator == "<": return left < right
        if operator == "==": return left == right
        if operator == "!=": return left != right
        return False
