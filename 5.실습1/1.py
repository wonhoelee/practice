# 5명 평균
# b=0
# for i in range(5):
#     a = int(input())
#     if a < 40 :
#         b += 40
#     else:
#         b += a
# print(b//5)

# 상근날드
# a=[]
# b=[]
# for i in range(3):
#     a += [int(input())]
# for j in range(2):
#     b += [int(input())]

# print(min(a)+min(b)-50) 

#세개의 수
# x = map(int,input().split())
# b=sorted(x)
# print(b[1])

#별찍기-8
# n = int(input())
# for i in range(1,2*n):
#     if i >= 2*n-i:
#         print('*'*(2*n-i))
#     else:
#         print('*'*i)

#별찍기-9

# n = int(input())
# for i in range(2*n-1):
#     if i >= 2*n-i:
#         print(' '*(2*n-2-i)+"*"*(2*i-2*n+3)+' '*(2*n-2-i))
#     else :
#         print(' '*i + '*'*(2*n-2*i-1) + ' '*i)

# n = int(input())
# for i in range(1,n+1):
#     print(' '*(i-1)+'*'*(2*n-2*i+1))
# for j in range(1,n):
#     print(' '*(n-j-1)+'*'*(2*j+1))

#별찍기 -21
# a = int(input())
# b,c = a,a//2
# for i in range(1,a+1):
#     if b%2 == 1:
#         print('* '*(b-c))
#         print(' *'*c)
#     else:
#         print('* '*c)
#         print(' *'*(b-c))
    