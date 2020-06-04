# MCS 260 Project Two by Veronica Kalicki
import random

# Welcome statement
print("Welcome to my average maximum hourly customer volume calculator!")

# Prompting for user input
hours = int(input("Please give the number of business hours per day: "))
customers = int(input("Please give the number of customers per day: "))
days = int(input("Please give the number of days to simulate: "))
h = hours * 60  # converting hours to minutes

# Simulating each day, making a list of the daily maximum hourly customer volumes
day_list = []
for d in range(days):
    # Simulating the random minutes each customer arrives at during the day,
    #  using a list of random hours that were multiplied by 60 by of length cust_per_day
    cust_list = []
    for c in range(customers):
        cust_list.append(random.randint(0, h))
        cust_list.sort()  # the customer arrival time is now in order from first to last arrival

        # generates random amount of time that each customer will have to wait
    serve_time = []
    for s in range(customers):
        serve_time.append(int(random.uniform(5, 16)))

    wait_list = []
    wait_time = 0
    for w in range(customers - 1):
        if cust_list[w + 1] < (cust_list[w] + serve_time[w] + wait_time):
            # checking if arrival of next customer is earlier than the sum of arrival of current customer,
            #  serve time and wait time of current customer
            wait_time = cust_list[w] + serve_time[w] + wait_time - cust_list[w + 1]  # if yes wait_time is updated.
        else:
            wait_time = 0  # else wait_time is set to 0
        wait_list.append(wait_time)  # adding all the wait_time to wait_list
    # print wait_list
    day_list.append(max(wait_list))  # adding maximum wait_time from wait_list to day_list

    # Computing the average
    # print day_list
average = float(sum(day_list)) / days

# Printing the output for the user
print("The average maximum customer wait time is : ", average)
