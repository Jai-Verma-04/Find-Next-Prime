
num = int(input("Enter Number: "))

def check_prime(num):
    flag = False
    if num >= 1:
        for i in range(2, int(num/2)+1):
            if (num % i) == 0:
                flag = False
                break
        else:
            flag =True
    else:
        flag = False
    
    return flag
while True:
    num+=1
    if check_prime(num) == True:
        print(num)
        break
    else:
        continue