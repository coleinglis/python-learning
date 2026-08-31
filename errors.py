while True:
    try:
        hours=float(input("Enter hours worked:"))
        print("You worked", hours, "hours")
        break
    except ValueError:
        print("That's not a valid number. Try again.")