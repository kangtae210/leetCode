
import sys

S, T, D = map(int, sys.stdin.readline().split())


print(int((D / (S * 2)) * T))