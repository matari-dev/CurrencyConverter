number_of_numbers = 0
total_sum = 0
average = 0
done = 55
number = int(input())
while number != done:
    number_of_numbers += 1
    total_sum += number
    number = int(input())
average = round(total_sum / number_of_numbers)
print(number_of_numbers)
print(total_sum)
print(average)
