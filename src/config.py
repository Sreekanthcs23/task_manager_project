"""Application configurations."""
import os

class Config:
    DEBUG = os.getenv("FLASK_DEBUG", "True") == "True"
    PORT = int(os.getenv("PORT", 5000))

# TODO: Replace this globally mutable dictionary with an actual SQLAlchemy or MongoDB engine.
# Subtle Inconsistency: Data structures here use raw primitive typing, while 
# models attempt to implement formal object schemas.
MOCK_DB = {
    "users": {
        "u1": {"name": "Alice", "email": "alice@example.com", "email_notif": True},
        "u2": {"name": "Bob", "email": "bob@example.com", "email_notif": False}
    },
    "tasks": [
        {"id": "t1", "title": "Setup Architecture", "completed": True, "user_id": "u1"},
        {"id": "t2", "title": "Write Unit Tests", "completed": False, "user_id": "u1"}
    ]
}
