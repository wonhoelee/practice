import sys
sys.stdin =open('input.txt')

t = 10
for i in range(t):
    d = int(input())
    x = list(map(int, input().split()))
    for j in range(d):
        m = max(x)
        n = min(x)
        x.remove(m)
        x.append(m-1)
        x.remove(n)
        x.append(n+1)
    print(f'#{i+1} {max(x) - min(x)}')

