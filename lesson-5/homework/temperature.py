def convert_cel_to_far(C):
     F = C * 9/5 + 32
     return round(F, 2)
def convert_far_to_cel(F):
     C = (F - 32) * 5/9
     return round(C, 2)
F = float(input('Enter a temperature in degrees F: '))
print(f'{F} degrees F = {convert_far_to_cel(F)} degrees C')
C = float(input('Enter a temperature in degrees C: '))
print(f'{C} degrees C = {convert_cel_to_far(C)} degrees F')