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
    """
    Task Class

    A dataclass representing a task with attributes for task ID, description,
    status, creation timestamp, and update timestamp. It includes methods for
    converting the object to and from a dictionary representation.

    Attributes:
        id (int): The unique identifier for the task.
        description (str): A brief description of the task.
        status (Status): The current status of the task.
        createdAt (datetime): The timestamp when the task was created.
        updatedAt (datetime): The timestamp when the task was last updated.

    Methods:
        to_dict():
            Converts the Task object into a dictionary representation.

        from_dict(data: Dict[str, Any]):
            Creates a Task object from a dictionary representation.
    """

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
        """
        Create a Task object from a dictionary.

        Args:
            data (Dict[str, Any]): A dictionary containing task data. The `status` field
                                   must match one of the `Status` enum values (case-sensitive).

        Returns:
            Task: A Task object created from the dictionary.

        Raises:
            KeyError: If required keys are missing in the dictionary.
            ValueError: If the `status` field does not match a valid `Status` enum value.
        """
        return Task(
            id=data["id"],
            description=data["description"],
            status=Status[data["status"].upper()],
            createdAt=datetime.fromisoformat(data["createdAt"]),
            updatedAt=datetime.fromisoformat(data["updatedAt"]),
        )
