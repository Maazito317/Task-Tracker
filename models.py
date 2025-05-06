from dataclasses import dataclass, field
from datetime import datetime
from enum import Enum
from typing import Dict, Any


class Status(Enum):
    """An enumeration representing the status of a task."""

    TODO = "todo"
    IN_PROGRESS = "in_progress"
    DONE = "done"


@dataclass
class Task:
    """A class representing a task."""

    id: int
    description: str
    status: Status = Status.TODO
    createdAt: datetime = field(default_factory=datetime.now)
    updatedAt: datetime = field(default_factory=datetime.now)

    def to_dict(self):
        """Convert the Task object to a dictionary."""
        return {
            "id": self.id,
            "description": self.description,
            "status": self.status.value,
            "createdAt": self.createdAt.isoformat(),
            "updatedAt": self.updatedAt.isoformat(),
        }

    @staticmethod
    def from_dict(data: Dict[str, Any]):
        """Create a Task object from a dictionary."""
        return Task(
            id=data["id"],
            description=data["description"],
            status=Status[data["status"].upper()],
            createdAt=datetime.fromisoformat(data["createdAt"]),
            updatedAt=datetime.fromisoformat(data["updatedAt"]),
        )
