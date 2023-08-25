#1. ใช้ ,
print("Hello...",456,'Hi...',True,10+20,"Hey...")
#2. ใช้ + มีข้อแม้ว่าทุกตัวที่มาต่อกันต้องเป็น String
print("Hello... "+str(456)+' Hi... '+str(True)+' '+str(10+20)+" Hey...") 
#3 ใช้เมธอล foemat 
print("Hello... {} Hi... {} {} Hey...".format(456,True,10+20))
print("Hello... {0} Hi... {1} {2} Hey...".format(456,True,10+20)) #index number
#4. ใช้ f-string
print(f"Hello... {456} Hi... {True} {10+20} Hey...")
#5. ใช้ modulas operator (%) ->%d, %f, %c, %s, .......
print("Hello... %d HI... %s %d Hey..." %(456,True,10+20) )
