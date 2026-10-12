from pydantic import BaseModel

from .member import MemberOut
from .task import TaskOut


class DashboardStats(BaseModel):
    total_meetings: int
    total_tasks: int
    pending_tasks: int
    in_progress_tasks: int
    completed_tasks: int
    overdue_tasks: int
    members: list[MemberOut]
    upcoming_deadlines: list[TaskOut]
