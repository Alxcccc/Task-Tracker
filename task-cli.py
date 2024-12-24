import argparse
from scripts.commands import procces_task_tracker

if __name__ == "__main__":
    print("""
           By: 
                    
        ░▒▓██████▓▒░░▒▓█▓▒░      ░▒▓█▓▒░░▒▓█▓▒░░▒▓██████▓▒░  
        ░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░      ░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░ 
        ░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░      ░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░        
        ░▒▓████████▓▒░▒▓█▓▒░       ░▒▓██████▓▒░░▒▓█▓▒░        
        ░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░      ░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░        
        ░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░      ░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░ 
        ░▒▓█▓▒░░▒▓█▓▒░▒▓████████▓▒░▒▓█▓▒░░▒▓█▓▒░░▒▓██████▓▒░  
          """)
    
    parser = argparse.ArgumentParser(description="Task Tracker CLI")

    subparsers = parser.add_subparsers(dest='command')

    add_parser = subparsers.add_parser('add', help='Add a new task')
    add_parser.add_argument('description', type=str, help='Description of the task')

    update_parser = subparsers.add_parser('update', help='Update an existing task')
    update_parser.add_argument('id', type=int, help='ID of the task to update')
    update_parser.add_argument('new_description', type=str, help='New description of the task')

    delete_parser = subparsers.add_parser('delete', help='Delete a task')
    delete_parser.add_argument('id', type=int, help='ID of the task to delete')

    mark_parser = subparsers.add_parser('mark', help='Mark a task as in progress or done')
    mark_parser.add_argument('id', type=int, help='ID of the task to mark')
    mark_parser.add_argument('status', choices=['in-progress', 'done'], help='Status to set for the task')

    list_parser = subparsers.add_parser('list', help='List all tasks or filter by status')
    list_parser.add_argument('status', nargs='?', choices=['todo', 'in-progress', 'done'], help='Filter tasks by status')

    args = parser.parse_args()
    procces_task_tracker(args)


