"""3. Print a list of numbers that are divisors of number num. Take input from user for num.
For example:
>>> Enter the number: 20
Divisor List = [1, 2, 4, 5, 10, 20]"""

num = input("Enter a number:")
divisor_list=[]
index = 1
while (index <= num/2):
    if (num % index == 0):
        divisor_list.append(index)
    index += 1;
divisor_list.append(num)
print divisor_list
