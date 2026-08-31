class Task:
    def __init__(self, name, hours, status):
        self.name=name
        self.hours=hours
        self.status=status
    def mark_complete(self):
        self.status="complete"
task1=Task("Pour foundation", 12, "in progress")
print(task1.name, task1.hours, task1.status)
task1.mark_complete()
print(task1.name, task1.hours, task1.status)