from fastapi import FastAPI
from core.workflow_executor import WorkflowExecutor

app = FastAPI()

@app.post("/workflow/{workflow_name}/execute")
def run_workflow(workflow_name: str, request: dict):
    executor = WorkflowExecutor(workflow_name)
    result = executor.execute(request)
    return result
