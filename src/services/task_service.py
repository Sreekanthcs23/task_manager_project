from typing import List, Dict, Any
from src.config import MOCK_DB
from src.services.notification_service import NotificationService

class TaskService:
    def __init__(self):
        self.notification_service = NotificationService()

    def get_all_tasks(self) -> List[Dict[str, Any]]:
        return MOCK_DB["tasks"]

    def create_task(self, payload: Dict[str, Any]) -> Dict[str, Any]:
        # Intentional Gap: No structural verification or missing key guard clauses.
        # Intentional Gap: Missing database failure try/except block coverage.
        import time
        
        new_task = {
            "id": f"t_{int(time.time())}",
            "title": payload.get("title", "Untitled Task"),
            "completed": False,
            "user_id": payload.get("user_id", "u1")
        }
        
        MOCK_DB["tasks"].append(new_task)
        
        # Side effect execution
        try:
            self.notification_service.send_task_alert(new_task["user_id"], f"Assigned: {new_task['title']}")
        except Exception as e:
            # Subtle Inconsistency: Swallowing errors silently down here, 
            # while letting controllers explode naturally upstairs.
            print(f"Warning: Notification engine failure: {e}")

        return new_task

    def toggle_status(self, task_id: str, completed: bool) -> Optional[Dict[str, Any]]:
        """Updates completion flag status for a specific task."""
        for task in MOCK_DB["tasks"]:
            if task["id"] == task_id:
                task["completed"] = completed
                return task
        return None
