def average_celsius(farenheit_readings):
    celcius_numbers = []

    # convert each reading and add to array
    for numbers in range(farenheit_readings):
        celsius_conversion = (farenheit_readings - 32) // 1.8
        celcius_numbers.append(celsius_conversion)
        #print(celcius_numbers)
        break

    # get sum of all celcius numbers
    sum = 0.0
    for numbers in celcius_numbers:
        sum += numbers

    print("The average celsius reading is : " + str(celcius_numbers))

average_celsius(75)

