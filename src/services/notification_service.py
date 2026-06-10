from src.config import MOCK_DB

class NotificationService:
    def send_task_alert(self, user_id: str, message: str) -> bool:
        """Dispatches system notifications to users based on preferences."""
        user = MOCK_DB["users"].get(user_id)
        
        # Intentional Gap: If user doesn't exist, accessing keys on `None` raises an unhandled AttributeError!
        if user["email_notif"]:
            print(f"[EMAIL SENT] To: {user['email']} | Msg: {message}")
            return True
            
        # TODO: Implement SMS/Push notification fallback if email_notif is disabled
        return False
