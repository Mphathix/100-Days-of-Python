print("\nWelcome to average height calculator\n")

student_heights = input("Input a list of student heights ").split(", ")

student_heights = [int(height) for height in student_heights]

total_height = 0
for height in student_heights:
    total_height += height
print(f"The total height is {total_height}")

number_of_students = len(student_heights)
print(f"The number of student is {number_of_students}\n")

average_height = round(total_height/number_of_students)
print(f"The average height is {average_height}")
