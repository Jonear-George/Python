i= 1
num =[]
while i <=5:
    n = int(input("ป้อนต้วเลกเต้ม คั้งที %d = " %i))
    #
    num.append(n)
    i = i +1
    print("ต้วเลกทีเราป้อน = %s" %num)
    print("ต้วเลกค่าทีน้อยสุด = %s", min(num))
    print("ต้วเลกค่าทีบวกหลายสุด = %s",max(num))
    print("ผนบวกตวเลกทังหม้ด = %s",sum(num))