import numpy as np

def levenshtein(seq1, seq2):
    size_x = len(seq1) + 1
    size_y = len(seq2) + 1
 
    matrix = np.zeros ((size_x, size_y)) 
 
    for x in range(size_x):
        matrix [x, 0] = x # row aray with elements of x
    for y in range(size_y):
        matrix [0, y] = y # column array with elements of y
    for x in range(1, size_x):
        for y in range(1, size_y):
            if seq1[x-1] == seq2[y-1]: # if the alphabets at the postion is same
                matrix [x,y] = min(
                    matrix[x-1, y] + 1,
                    matrix[x-1, y-1],
                    matrix[x, y-1] + 1
                )
 
            else:         # if the alphabbets at the position are different
                matrix [x,y] = min(
                    matrix[x-1,y] + 1,
                    matrix[x-1,y-1] + 1,
                    matrix[x,y-1] + 1
                )
 
    # returning the levenshtein distance
    return (matrix[size_x - 1, size_y - 1])