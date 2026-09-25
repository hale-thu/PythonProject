def sum_and_average(s1):
    total = 0
    count = 0
    for c in s1:
        if c.isdigit():
            total += int(c)
            count += 1
    if count == 0:
        return 0, 0
    return total, total/count

s1 = input("input s1: ")
total, average = sum_and_average(s1)
print("Sum is:", total, "and average is:", average)

