class Task:
    
    def __init__(self, id: int, description: str, created_at: str, update_at: str):
        self.id = id
        self.description = description
        self.state = "todo"
        self.created_at = created_at
        self.update_at = update_at

    def __str__(self):
        return f"description={self.description}, created_at={self.created_at}, update_at={self.update_at}"

    