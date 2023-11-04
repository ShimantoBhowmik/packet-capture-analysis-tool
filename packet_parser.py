#!/usr/bin/python3

def parse(filename, L):
    with open(filename, 'r') as f:
        lines = f.readlines()
        for line in lines:
            L.append(line.strip().split())
