
# 구구단
# n = int(input())
# for i in range(1,10):
#     print( f'{n} * {i} = {n*i}')

# 두수의 합
# T = int(input())
# for i in range(T):
#     a, b = map(int,input().split())
#     print(a+b)

# n까지의 합
# n = int(input())
# a=0
# for i in range(1,n+1):
#     a += i    
# print(a)

# 빠른 A+B
# import sys
# T = int(input())
# for i in range(T):
#     A = sys.stdin.readline().split()
#     print(int(A[0])+int(A[1]))

# N찍기
# a = int(input())
# for i in range(1,a+1):
#     print(i)

# 기찍N
# a = int(input())
# for i in range(a,0,-1):
#     print(i)

# A+B -7
# T = int(input())
# for i in range(1,T+1):
#     a,b = map(int,input().split())
#     print(f'Case #{i}: {a+b}')

# A+B -8
# T = int(input())
# for i in range(1,T+1):
#     a,b = map(int,input().split())
#     print(f'Case #{i}: {a} + {b} = {a+b}')

# 별 찍기 - 1
# n = int(input())
# for i in range(1,n+1):
#     print('*'*i)

# 별 찍기 -2 
# n = int(input())
# for i in range(1,n+1):
#     print(' '*(n-i) + '*'*i )

# x 보다 작은 수

# a, b = map(int,input().split())
# x = map(int,input().split())
# for i in x:
#     if b > i:
#         print(i,end=' ')