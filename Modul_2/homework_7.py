list_car = ["BMV", "MB", "LADA", "KIA", "HONDA"]
for i in list_car:
    print('Я езжу на автомобиле марки ' + '"' + i + '"')
cars_count = 0
for i in range(len(list_car)):
    if i > 0:
        cars_count += 10
        print(str(i), str(cars_count))
    else:
        print(str(i), str(cars_count))
