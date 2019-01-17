#Celsius to Fahrenheit Conversion Script
#Morgan P.
#11/14/2018


def convert():
	fahrenheit = eval(input("What is the temperature in Fahrenheit? "))
	celsius = fahrenheit - 32 / 1.8
	print ("The temperature is", celsius,"°C")
convert()
