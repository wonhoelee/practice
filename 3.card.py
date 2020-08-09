import sys
sys.stdin =open('sample_input_3.txt')

t = int(input())
for i in range(t):
    c = [0] * 10
    n = int(input())
    x = int(input())
    for j in range(n):
        c[x%10] += 1
        x = x // 10
    for w in range(len(c)):
        if c[w] == max(c):
            a = w
    print(f'#{i+1} {a} {max(c)}')