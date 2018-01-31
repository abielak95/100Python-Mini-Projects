#Convert Celsius to Fahrenheit and vice versa

def toCelsius(fahrenheitTemp):
    return (float(5 / 9) * (fahrenheitTemp - 32))

def toFahrenheit(celsiusTemp):
    return (float(9 / 5) * celsiusTemp + 32)

method = int(input("Type 1 if you want to convert temperature to Celsius\nType 2 if you want to convert temperature to Fahrenheit \n"))
temp = int(input("Type temperature: "))

if method == 1:
    print("Temp in Celcius: %.2f" % toCelsius(temp))
else:
    print("Temp in Fahrenheit: %.2f" % toFahrenheit(temp))
