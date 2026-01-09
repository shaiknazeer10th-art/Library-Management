# def user_input():
#     student_name = str(input("enter your name: "))
#     marks = []
#     for i in range (1,6):
#         mark = float(input(f"enter marks for subject {i}: "))
#         marks.append(mark)
#     return student_name, marks

# def calculate_avg(marks: list[float]):
#     avg = sum(mark)/len(marks)
#     return avg

# def assign_grade(avg):
#  if avg >= 90:
#     print("A+")

#  elif avg >= 80:
#     print("A")

#  elif avg >= 70:
#     print("B")

#  elif avg >= 60:
#     print("C")

#  elif avg >= 50:
#     print("D")

#  else:
#     print("F")

# def pass_or_fail(avg):
#     if avg >= 50:
#      return"pass"
#     else:
#         return "fail"
    
# def display_result(name,average,grade,status):
#     print("---result---")
#     print(f"student name:{name}")
#     print(f"average: {average}")
#     print(f"grade:{grade}")
#     print(f"status:{status}")

# while True:
#     student_name, mark = user_input()
#     avg = calculate_avg(mark)
#     grade = assign_grade(avg)
#     status = pass_or_fail(avg)

#     display_result(student_name, avg, grade, status)

#     next = input(" Do you want to continue? - YES/NO")
#     if next == "YES" :
#            continue
#     else:
#          break
    

# tuple = (1, 2, 3, 4)
# list = list(tuple)
# print(list)
s = (1, 2, 3, 4, 2, 4, 5)
print(s)
l = [1, 1, 2, 3, 4]
s = set(1)
print(s)