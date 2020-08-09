import sys
sys.stdin =open('sample_input_2.txt')

t = int(input())

for i in range(t):
    po = 0
    cnt = 0
    k, m, n = map(int, input().split())
    x = list(map(int, input().split()))
    po += k
    for q in range(len(x)-1):
        if x[q+1] - x[q] > k:
            print(f'#{i+1} 0')
            break
    for q in range(len(x)):
        for j in range(m):
            if po in x:
                if po >= m:
                    break
                cnt += 1
                po += k
            else:
                if po >= m:
                    break
                po -= 1
                continue
    if po >= m:
        print(f'#{i+1} {cnt}')

