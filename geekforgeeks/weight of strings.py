'''
Weight of Strings
'''
for _ in range(int(input("Enter Number : "))):

    s1=str(input("Enter String : "))
    s2=str(input("Enter String : "))

    l1=l2=0

    for i in s1:
        l1 += (ord(i)%96)
    for j in s2:
        l2 += (ord(j)%96)
        
    if(l1 > l2):
        print(1)
    if(l1 < l2):
        print(2)
    if(l1 == l2):
        print('equal')
