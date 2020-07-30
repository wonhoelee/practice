#두 정수 A와 B가 주어졌을 때, A와 B를 비교하는 프로그램을 작성하시오.

# a,b = map(int,input().split())

# if a > b:
#     print('>')
# elif a < b : 
#     print('<')
# else :
#     print('==')

# 시험 점수를 입력받아 90 ~ 100점은 A, 80 ~ 89점은 B, 70 ~ 79점은 C, 60 ~ 69점은 D, 나머지 점수는 F를 출력하는 프로그램을 작성하시오.
# a = int(input())
# if a >= 90 : 
#     print('A')
# elif a>=80:
#     print('B')
# elif a>= 70:
#     print('C')
# elif a>= 60:
#     print('D')
# else:
#     print('F')

# 윤년


# a = int(input())
# if a % 4 == 0 and a % 100 != 0:
#     print('1')
# elif a % 400 == 0:
#     print('1')
# else :
#     print('0')

#좌표

# a = int(input())
# b = int(input())
# if a > 0 and b > 0:
#     print('1')
# elif a > 0 and b < 0:
#     print('4')
# elif a < 0 and b > 0:
#     print('2')
# else:
#     print('3')

#알람 시계

a ,b = map(int,input().split())

if b - 45 < 0 and a == 0:
    a = 23
    b = 15 + b 
    print(a,b ,end=' ')
else:
    a = a - 1
    b = 15 +b
    print(a,b ,end=' ')

    
