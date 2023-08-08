tri = [
    [75],
    [95, 64],
    [17, 47, 82],
    [18, 35, 87, 10],
    [20, 4, 82, 47, 65],
    [19, 1, 23, 75, 3, 34],
    [88, 2, 77, 73, 7, 63, 67],
    [99, 65, 4, 28, 6, 16, 70, 92],
    [41, 41, 26, 56, 83, 40, 80, 70, 33],
    [41, 48, 72, 33, 47, 32, 37, 16, 94, 29],
    [53, 71, 44, 65, 25, 43, 91, 52, 97, 51, 14],
    [70, 11, 33, 28, 77, 73, 17, 78, 39, 68, 17, 57],
    [91, 71, 52, 38, 17, 14, 91, 43, 58, 50, 27, 29, 48],
    [63, 66, 4, 68, 89, 53, 67, 30, 73, 16, 69, 87, 40, 31],
    [4, 62, 98, 27, 23, 9, 70, 98, 73, 93, 38, 53, 60, 4, 23]
    ]

totals = [[]] * len(tri)
for i in range(0,len(tri)):
    if i == 0:
        # first row in the triangle, no upper rows to add, total is equal to the first row in the triangle
        totals[i] = tri[i]
        continue
    for j in range(0, len(tri[i])):
        print(i, j)
        # total for the upper right path if exists, else 0
        if j == len(tri[i])-1:
            right_path_total = 0
        else:
            right_path_total = totals[i-1][j]
        # total for the upper left path, if it exists, else 0
        if j == 0:
            # no upper left path
            left_path_total = 0
        else:
            left_path_total = totals[i-1][j-1]
        totals[i] = totals[i] + [tri[i][j] + max(left_path_total, right_path_total)]

print(totals)

# the max value of the last row gives the highest total possible on a path
print(max(totals[len(tri)-1]))