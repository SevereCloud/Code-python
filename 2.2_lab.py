#����� ����� �� �����
#1 a*c
#2 b*d
#3 (a+b)
#4 3-2-1
#5 �������� 1 4 � 2

def multipli(x,y):
        if len(str(x)) == 1 or len(str(y)) == 1:
                return x*y
        else:
                n = max(len(str(x)),len(str(y)))
                nby2 = n / 2
                
                #��������� ����� �� �����
                a = x / 10**(nby2)
                b = x % 10**(nby2)
                c = y / 10**(nby2)
                d = y % 10**(nby2)
                #print(a,b,c,d)
                
                ac = multipli(a,c) #������ �����
                bd = multipli(b,d) #������ �����
                ad_bc = multipli(a+b,c+d) - bd - ac #3 � 4 �����
                print(ac,bd,ad_bc)

                result = ac * 10**(2*nby2) + (ad_bc * 10**nby2) + bd #5 ���

                return result


s = 0
while s==0:
        s1=int(input("������� ������ ����� \n"))
        s2=int(input("������� ������ ����� \n"))
        print(multipli(s1,s2))


print(quit())
