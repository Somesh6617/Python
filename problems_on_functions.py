"""#sum of 2 numbers
def sum(n1,n2):
    return n1+n2
n1=int(input("Num1:"))
n2=int(input("Num2:"))
result=sum(n1,n2)
print(f"sum of {n1} and {n2} is {result}")"""
"""#find area of circle
def area(radius):
    return 3.14*radius**2
radius=float(input("Enter the radius:"))
result=area(radius)
print(f"area of circle with radius {radius} is {result}")"""
"""#Quadratic equation ((b*b)-+(4*a*c))/2*a
def quadratic_equation(a,b,c):
    r1=(-b+((b*b)-(4*a*c))**0.5)/(2*a)
    r2=(-b-((b*b)-(4*a*c))**0.5)/(2*a)
    print(f"root1={r1} \nroot2={r2}")
values=input("Enter 3 values separated with comma(,):")
a,b,c=map(int,values.split(","))
quadratic_equation(a,b,c)"""
"""#swap to variables without using third variable
def swapping(v1,v2):
    v2=v1+v2
    v1=v2-v1
    v2=v2-v1
    print(f"two variables after swapping v1={v1} and v2={v2}")
v1=int(input("Enter num1:"))
v2=int(input("Enter num2:")) 
print(f"two variables before swapping v1={v1} and v2={v2}")
swapping(v1,v2)"""
#converting temperature units
def c_f(celcius):
    return celcius*(9/5)+32
def c_k(celcius):
    return celcius+273.15
def f_c(fahrenheit):
    return (fahrenheit-32)*(5/9)
def f_k(fahrenheit):
    return (fahrenheit-32)*(5/9)+273.15
def k_c(kelvin):
    return kelvin-273.15
def k_f(kelvin):
    return (kelvin-273.15)*(9/2)+32
celcius=float(input("Enter the celcius:"))
fahrenheit=float(input("Enter the fahrenheit:"))
kelvin=float(input("Enter the kelvin:"))
print(f"celcius to fahrenheit:{c_f(celcius):.2f}")
print(f"celcius to kelvin:{c_k(celcius):.2f}")
print(f"fahrenheit to celcius:{f_c(fahrenheit):.2f}")
print(f"fahrenheit to kelvin:{f_k(fahrenheit):.2f}")
print(f"kelvinto celcius:{k_c(kelvin):.2f}")
print(f"kelvin to fahrenheit:{k_f(kelvin):.2f}")

