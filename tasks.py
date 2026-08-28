task={"name":"Pour foundation", "hours": 12, "status":"in progress"}
print(task["name"])
print(task["hours"])
def describe_task(task):
    print(task["name"],"-", task["hours"], "hours -", task["status"])
describe_task(task)
def calculate_pay(hours, rate):
    total=hours*rate
    return total
pay=calculate_pay(12, 45.50)
print("Pay for this task:", pay)
