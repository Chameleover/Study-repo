for number in range(1, 100):
    not_owl = True
    temp = number
    sum = 0
    count = 0
    while temp > 0:
        sum += temp % 10
        temp //= 10
        count += 1
    print(sum)
    # if number % 100 == 0:
    #     print(number)
    # elif not_owl:
    #     print(number, end=",")


    # LEAVE IT for now