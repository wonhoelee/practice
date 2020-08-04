import sys
sys.stdin =open('sample_input_4.txt')

t = int(input())
for i in range(t):
    a=[]
    d=[]

    n, m = map(int,input().split())
    x = list(map(int,input().split()))

    for j in range(1,len(x)-m+2):
        num = 0
        for w in x[j-1:j+m-1]:
            num += w
        a += [num]
        d += [num]
    b = a[0]
    c = d[0]
    for j in range(len(a)):
        if b <= a[j]:
            b = a[j]
    for q in range(len(d)):
        if c >= d[q]:
            c = d[q]
    print(f'#{i+1} {b - c}')