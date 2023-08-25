

# a^2 + b^2 = c^2
# a + b >= c

triangle = [0, 0, 0]

solution_count = 0

for i in range(3, 1000 + 1):
    perimeter = i
    solutions = []

    for c in range(1, int(perimeter/2)): # minimum side length is 1, so max c value is perimeter - 1 - 1
        for a in range(1, int((perimeter - c)/2)):
            b = perimeter - c - a
            triangle = [a, b, c]
            if a*a + b*b == c*c:
                solutions.append(triangle)
    if len(solutions) > solution_count:
        solution_count = len(solutions)
        print(perimeter)

# provides correct solution (840)

