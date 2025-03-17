import json
from datetime import datetime

class Task():

    def __init__(self, file_path:str = 'db.json', start_data=[]):
        self.load_file()
        self.file_path = file_path
        self.start_data = start_data

    def load_file(self):
        try:
            with open(self.file_path, "r") as file:
                self.data = json.load(file)
        except (json.decoder.JSONDecodeError, FileNotFoundError):
            self.data = self.start_data

    def create(self, description, status='not done'):
        new_task = {
            "id": self.get_last_id(),
            "description": description,
            "status": status,
            "createdAt": datetime.now().isoformat(),
            "updatedAt": datetime.now().isoformat()
        }
        self.data.append(new_task)
        self.write_json()

    def get_last_id(self):
        try:
            return int(self.data[-1]["id"]) + 1
        except (IndexError, AttributeError, ValueError):
            return 1

    def write_json(self):
        with open(self.file_path, "w") as file:
            json.dump(self.data, file, indent=4)

    def update(self, task_id:int, description:str):
        pass

    def delete():
        pass

    def list():
        pass

if __name__ == '__main__':
    new_task = Task(1, "sad", "!", "asd", "sad")
    print(new_task.load_file())
    # print(new_task)
    # print(new_task.task_to_dict())