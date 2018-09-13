#!/usr/bin/python3

def rotate_matrix(m):
    if not m:
        return m
    result = []
    w = len(m[0])
    h = len(m)
    for i in range(w):
        row = []
        for j in range(h, -1, -1):
            row.append(m[i][j])
        result.append(row)