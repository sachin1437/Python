# Write a Python program to check if a given string is a palindrome.

a=input("Enter a string: ").replace(" ","").lower()  #here i'm using .replace() because it will replce the exact thing which i write in it like here i have written to replace spaces (" ") with ("") no space here any space entered by the user will be ignored and .lower() is used because python is case-sensitive language so any uppercase alphabet will be converted to lowercase so that it should not conflict during palindrome checking.
if a[::-1]==a:  # here I am checking if the a string is equals to reversed a string, how? by using [::-1] slicing method,this is used for reversing any string manually without using any pre-defined function.
    print(f"{a} is a palindrome.")  #here, I have used f string which means i can write the variables inside a string and can print them. this process is also called as string interpolation.
else:
    print(f"{a} is not a palindrome.")


# you can use re library if you want to counter these types of problem like :- "A man, a plan, a canal, Panama!" let's say this phrase was given and this could become a palindrome but how that is the question so here we do these things:-
import re
a=re.sub(r'[^a-z0-9]','',input("Enter a string: ").lower()) #here re.sub is a in-built function in the python's re module sub means substitute basically it searches for a pattern in the string and replaces it with something else whatever you want you can tell it like here i have told it [^] this is the symbol of not , [^a-z0-9] so by this it will not replace a to z alphabets and 0-9 digits and everything else will be replced by ('') which means just remove them or even you can write something in between '' then it will replace it with whatever you entered in '' . 
if a[::-1]==a:
    print(f"{a} is a palindrome.")
else:
    print(f"{a} is not a palindrome.")







# r string example
print(r"Tasbgisbisnfob\nsifbsifb") 

#here i have used \n which is escape character basically to change the line from b and start a new line from s but by using r string i can print \n also.
#if you remove r keyword then you can see how  this string will change line while executing. 