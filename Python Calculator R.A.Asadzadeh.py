print ('Welcome to Kalku-lator by R.A.Asadzadeh, to start calculating, please choose a operator')
def main():
    print ('1-addition  2-subtraction  3-multiplication  4-division  5-exponentitation')
    x=int (input())
    if x > 5 or x < 1:
        print ('Please choose the correct operator')
        return
    y=int (input('input first number '))
    z=int (input('input second number '))
    print ('Your result is,')
    if x == 1:
        print (y, '+', z, "=", y + z)  
    elif x == 2:
        print (y, '-', z, "=", y - z)
    elif x == 3:
        print (y, '*', z, "=", y * z) 
    elif x == 4:
        print (y, '/', z, "=", y / z) 
    elif x == 5:
        print (y, '^', z, "=", y ** z)

while 1==1:
    main()
