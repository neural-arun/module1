# only even squares from 1 to 10

even_squares = [x**2 for x in range(1,11) if x % 2 == 0]
print(even_squares)