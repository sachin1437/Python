# Write a Python program to find the factorial of a number entered by the user

n=int(input("Enter a number: "))
fact=1
for i in range(1,n+1):
    fact=fact*i  # here fact is being multiplied by every value of i in the range of 1 to n and if i write print(fact) here it will print every value of fact which is being solved

print(fact)  # here i have written the print statement outside the loop to avoid printing every value of fact which is being solved 
