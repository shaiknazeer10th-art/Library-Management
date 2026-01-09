# even numbers between 1-20 using for loop 

# for num in range (1,21):
#     if num % 2 == 0:
#         print(num)

# num = 1 
# while num <= 20:
#     if num % 2 == 0:
#         print(num)
#     num += 1
# num = num + 1





# print(list(range(2,10,2)))






# for num in range(2,10,2):
#     print(num)











# num=1
# while num<=20:
#     if num % 2==1:
#         print(num)
#     num+=1

    















# a = int (input("enter first number:"))
# b = int (input("enter second number:"))

# print("addition =  " , a+b) 
# print("substraction = " , a-b)
# print("multiplication = " , a*b)
# print("division = " , a/b)

















# a = [1, 2, 3, 4, 5, 6, -8, -6] 
# for num in a:
#     if num > 0:
#         print(num)

















# a = [1, 2, -3, -4, 0, 5, 6, -8, 9] 
# for num in a:
#     if num == 0 :
#         print("zero encountered stopping the loop")
#         break
#     print(num) 

















# marks = int(input("enter marks:"))
# if marks>= 90:
#     print("Grade-A")

# elif marks >=75:
#     print("Grade-B")

# elif marks >=50:
#     print("Grade-C")

# else:
#     print("Fail") 



# for num in range(1,51):
  
#     if num % 5 == 0 :
#         continue

#     if num == 37:
#         break 

#     print(num)


# a = [1, 2, 3, 4, 100, 6, 7, 8, 9]
# for num in a:
#     if num % 2 == 1:
#         continue

#     if num == 100:
#         break
#     print(num) 


books = [
        [101, "python programming", True],
        [102, "data structure", True],
        [103, "web development", True],
        [104, "machine learning", True],
        [105, "database systems", True]
]

def issue_book(book_id):
    found = False
    for book in books:
        if book[0] == book_id:
            found = True 
            if book[2]:
                book[2] = False
                print("book issued successfully")
            else:
                print("book unavailable")
    if not found:
        print("book id not found") 

issue_book(102)

























































# try:
#     x= 10/0
# except ZeroDivisionError:
#  print("cannot divide by zero")

# class A:
#     def show(self):
#         print("A")

# class C(A):
#     def show(self):
#         print("C")
# obj = C()        
# obj.show()

# import re

# text = "Hello world!"
# result = re.match("Hello", text)
# print(result.group())

# fahrenheit = float(input("Enter a value : ")) 


# celsius = (fahrenheit - 32) * 5/9 


# print(f"The temperature in Celsius is: {celsius}")

# num = int(input("enter the value"))
# if num % 2 == 0:
#     print("even")

# else:
#     print("odd") 

# num1 = int(input("enter first number:"))
# num2 = int(input("enter second number:"))
# num3 = int(input("enter third number:"))

# if (num1 > num2) and (num1 > num3):
#     print("num1 = largest number")

# elif (num2 > num1) and (num2 > num3):
#     print("num2 = largest number")

# else:
#     print("num3 = largest number")


# n=int(input("enter number "))
# factorial=1
# if n<0:
#     print("sorry, factorial does not exist for negative nummber ")
# elif n==0:
#     print("factorial of 0is 1")
# else:
#     i = 1
#     while i <= n:
#         factorial *= i
#         i += 1

#     print(f"The factorial of {n} is {factorial}")


