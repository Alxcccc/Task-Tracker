
# Task Tracker CLI

CLI app to track your tasks and manage your to-do list.

Credits of idea for: https://roadmap.sh/projects/task-tracker


## Technologies
Python
## Commands
add:   Add a new task
Example: 
```bash
python task-cli.py add "Buy groceries"
```
update: Update an existing task
```bash
python task-cli.py update 1 "Buy groceries and cook dinner"
```
delete: Delete a task
```bash
python task-cli.py delete 1
```
mark: Mark a task as in progress or done
```bash
python task-cli.py mark 1 "in-progress"
```

list: List all tasks or filter by status

status available "done", "in-progress" and "todo"
```bash
python task-cli.py list
python task-cli.py list "done"
python task-cli.py list "in-progress"
python task-cli.py list "todo"
```

## Installation

To run the app, ensure you have Python installed and follow these steps:

Clone the repository:

```bash
git clone https://github.com/yourUsername/Task-Tracker.git
```

Navigate to the project directory:
```bash
cd task_tracker
```

Run the program:
```bash
python main.py -help
```



    
