def AccumlateNo(max, add):
    #i = 0
    numbers = []
    # while i < max:
    #     print("At the top i is %d" % i)
    #     numbers.append(i)
    #
    #     i = i + add
    #     print("Numbers now: ", numbers)
    #     print("At the bottom i is %d" % i)
    for i in range(max):
        print("At the top i is %d" % i)
        numbers.append(i)

    return numbers

numbers = AccumlateNo(5, 2)

print("The numbers: ")

for num in numbers:
    print(num)