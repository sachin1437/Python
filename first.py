# Write a Python program to find the factorial of a number entered by the user

n=int(input("Enter a number: ")) #taking input from the user here, int is the data type of the input value
fact=1 # we have to assign a factorial variable as 1 , we can't assign any other number otherwise it will give wrong output
    # why did we assign fact ? because if we didn't assign it then it will give an error that fact is not defined as interpreter will not understand what is fact
for i in range(1,n+1): # here i'm using for loop to go through every value of i in the range of 1 to n (here n+1 is written because we want to print till the input number that is n)
    fact=fact*i  # here fact is being multiplied by every value of i in the range of 1 to n and it keeps updating fact value per iteration and if i write print(fact) here it will print every value of fact which is being solved
print(fact)  # here i have written the print statement outside the loop to avoid printing every value of fact which is being solved 


