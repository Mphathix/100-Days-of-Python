even_number = 0
for number in range(1, 101):
    if number % 2 == 0:
        even_number += number
print(f"The total value of even number between 0 - 100 is: {even_number}")
