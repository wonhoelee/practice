import sys
sys.stdin = open('input.txt')

t = int(input())
for i in range(t):
    x = list(map(str,input()))

    if x == x[::-1]:
        print(0)
        continue
    else:
        lyes ,ryes = True, True
        l = 0
        r = len(x)-1
        cnt = False
        while l <= r:
            if x[l] != x[r]:
                if not cnt:
                    cnt = True
                    r-=1
                else:
                    lyes = False
                    break
            else:
                l += 1
                r -= 1
        l = 0
        r = len(x) - 1
        cnt = False
        while l <= r:
            if x[l] != x[r]:
                if not cnt:
                    cnt = True
                    l+=1
                else:
                    ryes = False
                    break
            else:
                l += 1
                r -= 1
    if not (lyes or ryes):
        print(2)
    else:
        print(1)



