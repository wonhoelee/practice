import sys
sys.stdin =open('sample_input_1.txt')

t = int(input())
for i in range(t):
    n = int(input())
    x = list(map(int,input().split()))
    a = x[0]
    b = x[0]
    for j in range(len(x)):
        if a <= x[j]:
            a = x[j]
    for q in range(len(x)):
        if b >= x[q]:
            b = x[q]

    print(f'#{i+1} {a-b}')