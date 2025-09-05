# Write a Python program to check if a given number is an Armstrong number.
# Armstrong numbers are those numbers whose each digit when powered to the number of total digits and added it becomes the number itself.
# example:- 153,  total number of digits here is 3 (1,5 and 3) so the power will be 3 on each digit,  like 1^3+5^3+3^3, when you will solve it you will get the number 153 itself.

num=int(input("Enter a number: "))
l=len(str(num))  # Here i'm calculating the length of the num by converting it into string because len() function does not work on integer directly.
arm=0 # Here I have defined arm (a variable) so that it don't throw an error of arm not defined
for ch in str(num):  # Here for loop is used to iterate the num entered by the user, num can only be iterated by converting to string (NOTE: In Python u can't iterate integer)
    digit=int(ch)  # Here, Convert each and every iterated digits into integer for calculation.
    arm=arm+digit**l  # Here, arm variable is used to store the calculated number; arm is already 0 then it goes like this suppose the num is 153 then the very first ch will be 1 so arm=0+1**3 (3 is the length of num)now this same calculation will repeat till last digit of the num and the arm value will be updated after every calculation.
# print(arm) # use this statement only when you want to see what is the arm value otherwise leave it.
if num==arm: # Here, compare num to arm. 
    print(f"{num} is an Armstring Number.")
else:
    print(f"{num} is not an  Armstrong Number.")


# Find Armstring numbers between 1 to 1000
# n=int(input("Enter a number: "))  # U can use this line if you want user to define till what number he wants to find just write [for n in range(1,num+1)].
for num in range(1,1001): #Here i have already defined starting and ending range.
    l=len(str(num)) 
    arm=0
    for ch in str(num):
        d=int(ch)
        arm=arm+d**l  # Here, d**l means d to the power l (d^l)
    if num==arm:
        print(num)  # We have to print num because we are checking for the number to be armstrong number whereas arm is the calculated sum.
