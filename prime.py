# Write a program that takes an integer input from the user and checks whether it is a prime number.

# num=int(input("Enter a number: "))
# if num<=1:   # Here, if the number is 1 or less than 1 will be printed as not a prime.
#     print(f"{num} is not a prime number.")
# else:
#     for i in range(2,num):  # Here started with 2 because 1 is factor of every number and only num is written which automatically means 'num-1', it confirms we are not checking the number itself also as the number itself is also a factor.
#         if num%i==0: # Here, if any num value is divisible by i it will be not a prime number because a prime number only has 2 factors which are 1 and the number itself.
#             print(f"{num} is not a prime number.")
#             break  # Here, break because if we did not use break statement then the else block which is used with for loop will be also executed, if num is not divisible by i then it jumps out of the loop and the else block will be executed
#     else:  # Here else block is used with for loop because only when the 'if' statement in the for loop didn't work then only the else block will be executed.
#         print(f"{num} is a prime number.")



# More optimized method using math module and sqrt() function.

# import math  # Here, imported math module
# num=int(input("Enter the value of num: "))
# if num<=1:
#     print(f"{num} is not a prime number.")
# else:
#     for i in range(2, int(math.sqrt(num)+1)):  # Here, int is used to convert the floating numbers into integer because after doing square root the result will be in float number; math.sqrt() is a function to calculate square root , and +1 because here we have to check square root of num value itself.
#         if num%i==0:
#             print(f"{num} is not a prime number.")
#             break
#     else:
#         print(f"{num} is a prime number.")



# Find prime numbers in a range from 1 to 100.
import math
for i in range(1,100):
    if i<=1:
        print(f"{i} is not a prime number.")
        continue  # Here, i have used continue statement because we are not giving user input so it will start checking from 1 upto 100 so continue is used that it jumps of this loop and executes the second loop.
    for v in range(2,int(math.sqrt(i)+1)):
        if i%v==0:
            print(f"{i} is not a prime number.")
            break
    else:
        print(f"{i} is a prime number.")
