#!/usr/bin/env python3

import argparse
from models import Status
from task_manager import TaskManager


def parse_args():
    parser = argparse.ArgumentParser(
        prog="Task Tracker CLI",
        description="A command-line interface for managing tasks.",
    )

    subparsers = parser.add_subparsers(
        dest="command", required=True, help="Available task management commands"
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
        choices=[status.value for status in Status],
        help="(optional) Filter tasks by status",
    )

    return parser.parse_args()


def main():
    args = parse_args()
    manager = TaskManager()

    if args.command == "add":
        try:
            task = manager.add_task(args.description)
            print(f"Task added successfully (ID: {task.id})")
        except Exception as e:
            print(f"Failed to add task: {e}")

    elif args.command == "update":
        try:
            task = manager.update_task(args.task_id, args.description)
            print(f"Task updated successfully (ID: {task.id})")
        except ValueError as e:
            print(f"Error: {e}")

    elif args.command == "delete":
        try:
            task = manager.delete_task(args.task_id)
            print(f"Task #{task.id} deleted.")
        except ValueError as e:
            print(f"Failed to delete task: {e}")

    elif args.command == "mark-in-progress":
        try:
            task = manager.mark_status(args.task_id, Status.IN_PROGRESS)
            print(f"Task #{task.id} marked as in progress.")
        except ValueError as e:
            print(f"Failed to mark in progress task: {e}")

    elif args.command == "mark-done":
        try:
            task = manager.mark_status(args.task_id, Status.DONE)
            print(f"Task #{task.id} marked as done.")
        except ValueError as e:
            print(f"Failed to mark done task: {e}")

    elif args.command == "list":
        status = Status(args.status) if args.status else None
        for t in manager.list_tasks(status):
            print(f"{t.id}: {t.description} [{t.status.value}]")


if __name__ == "__main__":
    main()
