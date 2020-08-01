# from pprint import pprint
# f = open("input.txt", 'r')
# line = f.readlines()

x= input()

b={}
for i in range(len(x)):
    a=0
    for j in x:
        if i == j:
            a += 1
    b[i] = a 
q=[]
w=[]
for key, value in b.items():
    q += [key]
    w += [value]
print(f'{w.index(max(w))}점 , {max(w)}번')    



#pprint(line)


