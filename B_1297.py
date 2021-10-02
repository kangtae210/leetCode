# TV 대각선 길이, 높이 및 너비 비율을 입력받으면
# TV의 높이와 너비를 출력한다.
import sys
import math

D,H,W = map(int, sys.stdin.readline().split())
parameter = math.sqrt((D * D) / (H*H + W*W))

H = math.floor(H * parameter)
W = math.floor(W * parameter)
print(H, W)
