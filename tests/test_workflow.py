from core.workflow_executor import WorkflowExecutor

def test_happy_path():
    # Pass both workflow and rules filenames explicitly
    executor = WorkflowExecutor(workflow_file="workflow.yaml", rules_file="rules.yaml")
    request = {
        "name": "Alice",
        "dob": "1990-01-01",
        "email": "alice@example.com",
        "age": 25,
        "credit_score": 750,
        "flagged": False
    }
    result = executor.execute(request)
    assert result["state"]["status"] == "approved"
