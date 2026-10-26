#Traditional Approach:
numbers = [1, 2, 3, 4, 5]
square = []

for number in numbers:
    square.append(number * number)
print(square) #[1, 4, 9, 16, 25]

#Comprehension Approach:
squares = [number * number for number in numbers]
even_no = [number for number in numbers if number %2 == 0]
print(squares) #[1, 4, 9, 16, 25]
print(even_no) #[2, 4]