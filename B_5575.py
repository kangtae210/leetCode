import sys

A=[]
for i in sys.stdin.readline().split():
    A.append(int(i))
A_res = []
A_res.append(A[3] - A[0])
A_res.append(A[4] - A[1])
A_res.append(A[5] - A[2])
if A_res[2] < 0:
    A_res[2] += 60
    A_res[1] -= 1
if A_res[1] <0:
    A_res[1] += 60
    A_res[0] -= 1
A_str = ""
for i in A_res:
    A_str += str(i) + " "


A=[]
for i in sys.stdin.readline().split():
    A.append(int(i))
A_res = []
A_res.append(A[3] - A[0])
A_res.append(A[4] - A[1])
A_res.append(A[5] - A[2])
if A_res[2] < 0:
    A_res[2] += 60
    A_res[1] -= 1
if A_res[1] <0:
    A_res[1] += 60
    A_res[0] -= 1
B_str = ""
for i in A_res:
    B_str += str(i) + " "





A=[]
for i in sys.stdin.readline().split():
    A.append(int(i))
A_res = []
A_res.append(A[3] - A[0])
A_res.append(A[4] - A[1])
A_res.append(A[5] - A[2])
if A_res[2] < 0:
    A_res[2] += 60
    A_res[1] -= 1
if A_res[1] <0:
    A_res[1] += 60
    A_res[0] -= 1
C_str = ""
for i in A_res:
    C_str += str(i) + " "



print(A_str)
print(B_str)
print(C_str)


