weight = input ("體重Kg: ")
height = input("身高公尺: ")
weight = float(weight)
height = float(height)
bmi = (weight / (height**2))
if bmi < 18.5:
	print("你的bmi", bmi, "體重過輕")
elif bmi >= 18.5 and bmi < 24:
	print("你的bmi", bmi,"正常範圍")
elif bmi >= 24 and bmi < 27:
	print("你的bmi", bmi,"過重")
elif bmi >= 27 and bmi <30:
	print("你的bmi", bmi,"輕度肥胖")
elif bmi >= 30 and bmi < 35:
	print("你的bmi", bmi,"中度肥胖")
else:
	print("你的bmi", bmi, "重度肥胖")