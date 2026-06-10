from typing import TypedDict, Optional

# Subtle Inconsistency: Instead of a formal class structure like user.py, 
# the task model leans completely on Python's structural typing/Dictionaries.
class TaskDict(TypedDict):
    id: str
    title: str
    completed: bool
    user_id: str
    due_date: Optional[str]
