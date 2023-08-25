#รับค่า\ป้อนทางแป้นพิมพ์ ใช้ฟังก์ชั่น input() โดยสิ่งที่ป้อนทั้งหมดถือว่าเป็น String

#ตัวแปร variable เป็น identifier มีหน้าที่เก็บข้อมูลที่เกิดขึ้นในโปรแกรม ข้อมูลที่เก็บจะอยู่ใน RAM
#identifier คือ ชื่อที่ dev. ตั้งขึ้นมาเอง ต้องเป็นไปตามกฎการตั้งชื่อของภาษานั้นๆ

std_id = input('ป้อนรหัสนักศฃศึกษา: ')
std_name = input('ป้อนชื่อนักศึกษา: ')
stdYearBron = input('ป้อนปีเกิด: ') #สิ่งที่ป้อนทั้งหมดถือเป็น String
print('..................................')
print(f"ยินดีต้อนรับ {std_id} ชื่อ {std_name}")
stdAge = 2023 - int(stdYearBron) #ต้องแปลง String เป็น nuber -> int(), float()
print(f"คุณเกิดปี {stdYearBron} อายุ {stdAge}")
print('....................................')
print() #ใช้ ,
print("ยินดีต้อนรับ",std_id,"ชื่อ",std_name)
print("คุณเกิดปี",stdYearBron,"อายุ",stdAge,)
print('.....................................')
print() #ใช้ +
print("ยินดีต้อนรับ "+str(std_id)+' ชื่อ '+str(std_name))
print("คุณเกิดปี "+str(stdYearBron)+' อายุ '+str(stdAge))
print('...................................')
print() #ใช้ เมธอต format
print("ยินดีต้อนรับ {} ชื่อ {} ".format(std_id,std_name))
print("คุณเกิดปี {} อายุ {} ".format(stdYearBron,stdAge))
print('.....................................')
print() #ใช้ %
print("ยินดีต้อนรับ %s ชื่อ %s " %(std_id,std_name))
print("คุณเกิดปี %s อายุ %s " %(stdYearBron,stdAge))