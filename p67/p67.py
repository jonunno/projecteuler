
with open('data.txt', 'r') as f:
    data = f.read()


rows = data.split('\n')
tri = [[]]*len(rows)
for i in range(0, len(rows)):
    tri[i] = rows[i].split(" ")
    tri[i] = [int(x) for x in tri[i]]
print(tri)

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