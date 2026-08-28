hours_log=[]
entry=input("Enter hours worked (or 'done' to finish):")
while entry !="done":
    hours_log.append(float(entry))
    entry=input("Enter hours worked(or 'done' to finish):")
print("Logged hours:", hours_log)
print("day-by-day breakdown:")
for i in range(len(hours_log)):
    print("Day", i+1,":", hours_log[i],"hours")
    