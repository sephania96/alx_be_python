import datetime
def display_current_datetime():
    current_date = datetime.datetime.now()
    formatted_date = current_date.strftime("%Y-%m-%d %H:%M:%S")
    print(f"Current date and time:{formatted_date}")
    return(formatted_date)
display_current_datetime()

entry = int(input("Enter the number of days to add to the current date: "))
def calculate_future_date():
    current_date = datetime.date.today()
    delta = datetime.timedelta(days = entry)
    future_date = current_date + delta
    print(future_date)
    return(future_date)
calculate_future_date()
