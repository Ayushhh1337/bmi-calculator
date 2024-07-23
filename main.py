height = float(input("Enter your height in inches: "));
weight = float(input("enter your weight in lbs: "));

def BMI(height,weight):
    bmi=weight/(height**2) * 703;
    
    if (bmi<16):
        return 'severly underweight',bmi;
    
    elif(bmi >=16.00 and bmi < 18.5):
        return 'underweight',bmi;
    elif(bmi >=18.5 and bmi < 25):
        return 'healthy',bmi;
    elif(bmi >=25.00 and bmi < 30.00):
        return "Overweight",bmi;
    elif(bmi >=30.00):
        return "Obese",bmi
    
quote, bmi = BMI (height,weight);
print('Your bmi is: {} and you are: {}'.format(bmi,quote));
    
    