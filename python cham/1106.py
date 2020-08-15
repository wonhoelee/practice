import sys

sys.stdin = open('input.txt')

C, N =map(int, input().split())

for i in range(N):
    a, b = list(map(int,input().split())) # a비용 b고객
 