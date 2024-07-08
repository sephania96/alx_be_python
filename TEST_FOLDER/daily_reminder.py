task = input("Enter a task description: ")
priority = input("Priority (high/medium/low):")
time_bound = input("Is it time-bound? (yes/no):")

match priority:
    case "high":
        if time_bound.lower() == "yes":
            print(f"Reminder: '{task}' is a high priority task that requires immediate attention today!")
        else:
            print(f"Reminder: '{task}' you still have time to complete it!")
    case "low":
        if time_bound.lower() == "no":
            print(f"Reminder: '{task}' is a low priority task. Consider completing it when you have free time.")
        else:
            print(f"Reminder: '{task}' is a low priority task. But deadline is today.")
    case _:
        if time_bound == "yes":
            print(f"Reminder: '{task}' is a medium priority task.There is no more time complete it now ")
        else:
            print(f"Reminder: '{task}' is a medium priority task. Consider completing it when you have free time.!")