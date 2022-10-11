print("ເມູນົຕວໍດາເີນນການ")
print("1. ການບວກ")
print("2. ການົລບ")
print("3. ການູຄນ")
print("4. ການຫານ")
key = int(input("ກາຸລນາ ົກດ 1,2,3, ຼືຫ 4 = " ))
a= int(input("້ປອນໍ້ຂູມນົຕວເລກີທ 1 ="))
b= int(input("້ປອນໍ້ຂູມນົຕວເລກີທ 2 ="))
if key == 1:
    print("ົຜນບວກ",a,"+",b,"=",(a+b))
elif key == 2:
    print("ົຜນົລບ",a,"-",b,"=",(a-b))
elif key == 3:
    print("ົຜນູຄນ",a,"*",b,"=",(a*b))
elif key == 4:
    print("ົຜນຫານ",a,"/",b,"=",(a/b))
else:
    print("ິຜດພາດທາງເັຕກິນກ!!!")