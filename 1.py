waga = float(input('Jaka jest Twoja waga: '))

wzrost = float(input('Jaki jest Twoj wzrost: '))

BMI = waga / (wzrost/100) ** 2

print(BMI)

if BMI <= 18.5:  
    print("Oops! Masz za mala wage.")  
elif BMI <= 24.9:  
    print("Super! Jestes zdrowy.")  
elif BMI <= 29.9:  
    print("Eee! Masz nadwage.")
else:  
    print("Seesh! Jestes gruby.")  
