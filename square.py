while True:
    a,b,c=map(float,input().split())
    if b**2 < 4*a*c:
        print("Нет коррней!!!")
    else:
        print("Корни: "+str((-b+(b**2-4*a*c)**0.5)/2/a)+", "+str((-b-(b**2-4*a*c)**0.5)/2/a)+"\n"+"Сумма: "+str(-b/a)+"\n"+"Произведение: "+str(c/a))
