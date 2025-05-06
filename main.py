import argparse
from models import Status
from task_manager import TaskManager


def parse_args():
    parser = argparse.ArgumentParser(
        prog="Task Tracker CLI",
        description="A command-line interface for managing tasks.",
    )

    subparsers = parser.add_subparsers(
        dest="command", required=True, help="Available commands"
    )

    # add: task-cli add "Do something"
    add = subparsers.add_parser(
        "add",
        help="Add a new task",
    )
    add.add_argument(
        "description",
        type=str,
        help="The task to add",
    )

    # update: task-cli update 1 "New description"
    update = subparsers.add_parser(
        "update",
        help="Update an existing task",
    )
    update.add_argument(
        "task_id",
        type=int,
        help="The ID of the task to update",
    )
    update.add_argument(
        "description",
        type=str,
        help="The new description of the task",
    )

    # delete: task-cli delete 1
    delete = subparsers.add_parser(
        "delete",
        help="Delete a task",
    )
    delete.add_argument(
        "task_id",
        type=int,
        help="The ID of the task to delete",
    )

    # mark-in-progress: task-cli mark-in-progress 1
    mip = subparsers.add_parser(
        "mark-in-progress",
        help="Mark a task as in progress",
    )
    mip.add_argument(
        "task_id",
        type=int,
        help="The ID of the task to mark as in progress",
    )

    # mark-done: task-cli mark-done 1
    md = subparsers.add_parser(
        "mark-done",
        help="Mark a task as done",
    )
    md.add_argument(
        "task_id",
        type=int,
        help="The ID of the task to mark as done",
    )

    # list: task-cli list [status]
    lst = subparsers.add_parser(
        "list",
        help="List tasks",
    )
    lst.add_argument(
        "status",
        type=str,
        nargs="?",
        choices=["todo", "in-progress", "done"],
        default="all",
        help="(optional) Filter tasks by status",
    )

    return parser.parse_args()


def main():
    args = parse_args()
    manager = TaskManager()

    if args.command == "add":
        task = manager.add_task(args.description)
        print(f"Task added successfully (ID: {task.id})")

    elif args.command == "update":
        task = manager.update_task(args.task_id, args.description)
        print(f"Task updated successfully (ID: {task.id})")

    elif args.command == "delete":
        task = manager.delete_task(args.task_id)
        print(f"Task #{task.id} deleted.")

    elif args.command == "mark-in-progress":
        task = manager.mark_status(args.task_id, Status.IN_PROGRESS)
        print(f"Task #{task.id} marked as in progress.")

    elif args.command == "mark-done":
        task = manager.mark_status(args.task_id, Status.DONE)
        print(f"Task #{task.id} marked as done.")

    elif args.command == "list":
        status = Status(args.status) if args.status else None
        for t in manager.list_tasks(status):
            print(f"{t.id}: {t.description} [{t.status.value}]")


if __name__ == "__main__":
    main()
