from sys import stdin

counter = 0
for line in stdin:
    money_to_pay = 0
    if line.strip("\n") != '0 0 0':
        a = line.strip("\n").split(" ")
        if counter == 0:
            number_of_drivers = int(a[0])
            allowed_hours = int(a[1])
            money_per_hour = int(a[2])
            counter += 1
        elif counter == 1:
            morning = sorted(list(map((lambda x: int(x)), a)))
            counter += 1
        elif counter == 2:
            evening = sorted(list(map((lambda x: int(x)), a)), reverse=True)
            for i in range(number_of_drivers):
                driver_hours = int(morning[i]) + int(evening[i])
                if driver_hours > allowed_hours:
                    money_to_pay += (driver_hours - allowed_hours) * money_per_hour
            print(money_to_pay)
            counter = 0
    else:
        break
