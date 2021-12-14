weight = float (input("น้ําหนักของคุณคือ >> " ))
height = float (input("ความสูงของคุณคือ >> " ))
bmi = weight/(height*height)
print("BMI = %.2f"%bmi)
if(bmi>=40):
    print("อ้วนขั้นสูงสุด") 
elif(bmi>=35):
    print("อ้วนขั้นที่ 2") 
elif(bmi>=28.5):
    print("อ้วนขั้นที่ 1") 
elif(bmi>=23.5):
    print("น้ําหนักเกิน") 
elif(bmi>=20.5):
    print("อยู่ในเกณฑ์ปกติ")
else:
    print("น้ําหนักต่ํากว่าเกณฑ์")