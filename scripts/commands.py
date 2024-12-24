from scripts.json_manage import FileManage
def procces_task_tracker(args):
    filemanage = FileManage()
    
    if args.command == 'add':
        description_task = args.description
        filemanage.add_task(description_task)
        
    elif args.command == 'update':
        id_task_update = args.id
        new_description = args.new_description
        filemanage.update_task_description(id_task_update, new_description)
        
    elif args.command == 'delete':
        id_task_delete = args.id
        filemanage.delete_task(id_task_delete)
        
    elif args.command == 'mark':
        id_task_mark = args.id
        status_task = args.status
        filemanage.mark_task(id_task_mark, status_task)
        
    elif args.command == 'list':
        filter_status = args.status
        if filter_status == "todo":
            filemanage.list_tasks_todo()
            
        elif filter_status == "in-progress":
            filemanage.list_tasks_in_progress()
            
        elif filter_status == "done":
            filemanage.list_tasks_done()
            
        else:
            filemanage.list_tasks_all()