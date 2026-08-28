daily_hours=[8, 9, 7.5, 10, 8, 6, 11]
print(daily_hours)
total_hours=0
for hours in daily_hours:
    total_hours=total_hours+hours
    if hours>8:
        print(hours, "-OVERTIME")
    else:
            print(hours, "-normal")
print("Total hours this week:", total_hours)

