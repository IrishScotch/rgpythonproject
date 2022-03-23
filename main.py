###########################
# Author: IrishScotch
# DOB: 03/23/2022
# Purpose: Track S5375 +, %
###########################
x = input("Input for lowest spell time (in seconds):")
x = float(x)
eq1 = (1000 + 80 * x ** 0.8)
eq2 = (6 + 0.6 * x ** 0.6)
print(f"additive:", f'+{eq1}')
print("multiplicative:", f'{eq2}%')
