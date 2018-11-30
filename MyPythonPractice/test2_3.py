'''birthday=tuple(input("Birth:"))
year=str(birthday[0])
month=str(birthday[1])
day=str(birthday[2])
print("我的出生日期是"+year+"年"+month+"月"+day+"日。")'''


birthday=str(input("Birth:"))
birth=birthday.split(',')
print("我的出生日期是"+birth[0]+"年"+birth[1]+"月"+birth[2]+"日。")