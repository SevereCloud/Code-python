s = 0
while s==0:
    n = input("���-�� ����� ")
    max = 0

    for i in range(n):
        a = input("����� ")
        if a > max:
            max = a

    print("max: " + str(max))    

print(quit())
