task={"name":"Pour foundation", "hours": 12, "status":"in progress"}
print(task["name"])
print(task["hours"])
def describe_task(task):
    print(task["name"],"-", task["hours"], "hours -", task["status"])
describe_task(task)
