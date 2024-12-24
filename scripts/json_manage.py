from models.task import Task
import json
from datetime import datetime

class FileManage():
    
    def __init__(self):
        self.task = None
        self.data_json = None
        self.id_tasks = 0
    
    def increment_id(self, array_json: list):
        lenght_array = len(array_json)
        if lenght_array == 0:
            return 1
        else:
            self.id_tasks = lenght_array+1
            return self.id_tasks
    
    def create_task(self, description: str):
        date_now = datetime.now()
        str_date = date_now.strftime("%Y-%m-%d %H:%M:%S")
        id = None
        self.task = Task(id, description, str_date, None)
        
    def converter_to_json(self):
        if self.task:
            self.data_json = {
                "id": self.task.id,
                "description": self.task.description,
                "created_at": self.task.created_at,
                "update_at": self.task.update_at,
                "state": self.task.state
            }
            return self.data_json
        else:
            print("Task not exists")
    
    def create_file(self):
        try:
            with open("task_tracker.json", "x") as f:
                json.dump({"list": []}, f)
        
        except FileExistsError:
            print("The file exists")
    
    def read_file(self):
        try:
            with open("task_tracker.json", "r") as f:
                data_file = json.load(f)
                print(data_file["list"])
        except:
            print("Hay un error")
            
    def add_task(self, description):
        try:
            with open("task_tracker.json", "r+") as f:
                data_file = json.load(f)

                self.create_task(description)
                self.converter_to_json()
                self.data_json["id"] = self.increment_id(data_file["list"])
                data_file["list"].append(self.data_json)

                f.seek(0)
                json.dump(data_file, f, indent=4)
                f.truncate()
            print(f"Task added successfully (ID: {self.data_json["id"]})") 
        except FileNotFoundError:
            self.create_file()
            self.add_task(description)

    def update_task_description(self, id_task: int, new_description):
        try:
            with open("task_tracker.json", "r+") as f:
                data_file = json.load(f)
                if id_task < 1 or id_task > len(data_file)+1:
                    print("The id not exists")
                    return
                
                data_file["list"][id_task-1]["description"] = new_description
                
                f.seek(0)
                json.dump(data_file, f, indent=4)
                f.truncate()
                
        except Exception as err:
            print(err)
    
    def mark_task(self, id_task, state):
        try:
            with open("task_tracker.json", "r+") as f:
                data_file = json.load(f)
                
                if id_task < 1 or id_task > len(data_file)+1:
                    print("The id not exists")
                    return
                
                data_file["list"][id_task-1]["state"] = state
                
                f.seek(0)
                json.dump(data_file, f, indent=4)
                f.truncate()
                
        except Exception as err:
            print(err)
            
    def delete_task(self, id_task):
        try:
            with open("task_tracker.json", "r+") as f:
                data_file = json.load(f)
                
                if id_task < 1 or id_task > len(data_file)+1:
                    print("The id not exists")
                    return
                
                del data_file["list"][id_task-1]
                
                f.seek(0)
                json.dump(data_file, f, indent=4)
                f.truncate()
                
        except Exception as err:
            print(err)
            
    def list_tasks_all(self):
        try:
            with open("task_tracker.json", "r") as f:
                data_file = json.load(f)
                for task in data_file["list"]:
                    print(task)
        except Exception as err:
            print(err)

    def list_tasks_todo(self):
        try:
            with open("task_tracker.json", "r") as f:
                data_file = json.load(f)
                for task in data_file["list"]:
                    if task["state"] == "todo":
                        print(task)
        except Exception as err:
            print(err)

    def list_tasks_in_progress(self):
        try:
            with open("task_tracker.json", "r") as f:
                data_file = json.load(f)
                for task in data_file["list"]:
                    if task["state"] == "in-progress":
                        print(task)
        except Exception as err:
            print(err)
    
    def list_tasks_done(self):
        try:
            with open("task_tracker.json", "r") as f:
                data_file = json.load(f)
                for task in data_file["list"]:
                    if task["state"] == "done":
                        print(task)
        except Exception as err:
            print(err)