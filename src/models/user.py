class User:
    """Pattern: Rich Domain Model (OOP Approach)"""
    def __init__(self, user_id: str, name: str, email: str, email_notif: bool):
        self.user_id = user_id
        self.name = name
        self.email = email
        self.email_notif = email_notif

    def can_receive_email(self) -> bool:
        return self.email_notif
