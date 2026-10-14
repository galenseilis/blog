
jump_spots = (7,10,14,23,24,28)

R = [[0] * 30 for i in range(30)]

for i in range(30):
    if i+1 not in jump_spots:
        for j in range(i+1, min(i + 6, 29) + 1):
            R[i][j] = 1/6

R[10-1][3-1] = 1
R[7-1][19-1] = 1
R[14-1][25-1] = 1
R[24-1][9-1] = 1
R[23-1][29-1] = 1
R[28-1][12-1] = 1
