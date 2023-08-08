import csv

# pull in the matrix data from the provided .csv file
with open('p81_matrix.csv') as f:
    data = list(csv.reader(f, delimiter=','))
f.close()

# convert strings to integers
for i in range(0, len(data)):
    data[i] = list(map(int, data[i]))

# set the initial coordinates (starting at the top left corner (x, y) = (0, 0))
x,y = 0,0

# store the totals calculated in each path in a list
sum = [0]

# Track what moves are in a given path
# r: move right
# d: move down
moves = ['r', 'd']#, 'l', 'u'] # allowed moves (right, down, left, up)
steps = ['r', 'r', 'd', 'd']

sum[0] = data[y][x]

def calc_sum(steps, subset, x, y):
    total = 0
    for step in steps:
        if step == "r": x += 1
        if step == "d": y += 1
        # if step == "l": x -= 1
        # if step == "u": y -= 1

        total += subset[y][x] # first list determines vertical position, second list determines horizontal position, vertical axis flipped


calc_sum(steps, data, x, y)



def add_step(moves, prior_steps):
    # add another step with each allowed move
    steps = []

    count = 0

    while count < len(prior_steps)*len(moves):

        steps.append([])

        for prior_step in prior_steps:

            for move in moves:
                # add each move to the end of the prior_steps list
                steps[i] = list(prior_step)
                print(steps)
                print(prior_step.copy())
                steps[i].append(move)
                print(steps[i])
                print(steps)
                print("done")
    return steps

steps = [['r'], ['d']]
for i in range(0, 2):
    print(steps)
    steps = add_step(moves, steps)
    # print(steps)
print('####')
print(steps)