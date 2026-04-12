student_score = input("Enter a list of student score? ").split(", ") 

student_score = [int(n) for n in student_score] 

highest_score = 0
for score in student_score:
    if score > highest_score:
        highest_score = score

print(f"\nThe highest score in the class is: {highest_score}")