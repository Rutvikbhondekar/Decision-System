import time
import random

class FailureHandler:
    def __init__(self, max_retries=3, backoff_factor=2):
        self.max_retries = max_retries
        self.backoff_factor = backoff_factor
        self.processed_requests = set()  # simple idempotency check

    def check_duplicate(self, request_id):
        if request_id in self.processed_requests:
            return True
        self.processed_requests.add(request_id)
        return False

    def retry_operation(self, operation, *args, **kwargs):
        retries = 0
        while retries < self.max_retries:
            try:
                return operation(*args, **kwargs)
            except Exception as e:
                wait_time = (self.backoff_factor ** retries) + random.uniform(0, 1)
                time.sleep(wait_time)
                retries += 1
        raise Exception("Max retries exceeded")

    def handle_dependency_failure(self, dependency_name):
        return {
            "status": "fail",
            "message": f"Dependency {dependency_name} failed",
            "action": "retry_or_manual_review"
        }
