# Task Tracker CLI

A lightweight command-line application to track and manage your tasks. Store tasks in a JSON file and perform common operations like adding, updating, deleting, marking status, and listing tasks by status—all from the terminal.

---

## Download & Installation

1. **Clone the repository:**
   ```bash
   git clone https://github.com/yourusername/task-tracker-cli.git
   cd task-tracker-cli
   ```
2. **(Optional) Set up a virtual environment:**
   ```bash
   python3 -m venv .venv
   source .venv/bin/activate  # Windows: .venv\\Scripts\\activate
   ```
3. **Install the CLI tool:**
   ```bash
   pip install --editable .
   ```
   Now the `task-cli` command is available globally in your shell.

---

## Usage

Run `task-cli --help` to see available commands:

```bash
$ task-cli --help
Usage: task-cli [OPTIONS] COMMAND [ARGS]...
...
```

### Commands

| Command                                | Description                                                    | Example                                       |
|----------------------------------------|----------------------------------------------------------------|-----------------------------------------------|
| `task-cli add "<description>"`         | Add a new task with the given description                      | `task-cli add "Buy groceries"`               |
| `task-cli update <id> "<description>"` | Update the description of an existing task                     | `task-cli update 1 "Cook dinner"`            |
| `task-cli delete <id>`                 | Delete the task with the specified ID                         | `task-cli delete 1`                           |
| `task-cli mark-in-progress <id>`       | Mark the task as in-progress                                   | `task-cli mark-in-progress 2`                 |
| `task-cli mark-done <id>`              | Mark the task as done                                          | `task-cli mark-done 2`                        |
| `task-cli list [status]`               | List tasks. Optionally filter by status: `todo`, `in_progress`, `done` | `task-cli list` <br> `task-cli list done` |

---

## Examples

```bash
# Add tasks
$ task-cli add "Write README"
Task added successfully (ID: 1)

# Update a task
$ task-cli update 1 "Write detailed README"
Task #1 updated.

# Delete a task
$ task-cli delete 1
Task #1 deleted.

# Mark tasks
$ task-cli add "Implement feature X"
Task added successfully (ID: 2)
$ task-cli mark-in-progress 2
Task #2 marked in-progress.
$ task-cli mark-done 2
Task #2 marked done.

# List tasks
$ task-cli list
1: Write detailed README [todo]
2: Implement feature X [done]

$ task-cli list todo
1: Write detailed README [todo]

$ task-cli list in_progress
(none)

$ task-cli list done
2: Implement feature X [done]
```

---

## File Structure

```
├── main.py
├── models.py
├── task_manager.py
├── setup.py
├── tasks.json      # Auto-created after first run
└── README.md
```

---

## Contributing & License

Contributions welcome! Please fork, implement features, add tests, and submit a pull request.  
Distributed under the MIT License. See [LICENSE](./LICENSE) for details.


[# Task-Tracker](https://roadmap.sh/projects/task-tracker)