

def circle_area(a):
    num = a**2*3.14
    return num

def circle_circum(b):
    num = b*2*3.14
    return num


a = int(input("請輸入半徑："))
area = circle_area(a)
lens = circle_circum(a)

print("圓面積：",area)
print("圓周長：",lens)

        
      