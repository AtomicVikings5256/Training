
import math

def menue():
	print("1. add")
	print("2. subtract")
	print("3. multiply")
	print("4. divide")
	
def menueInput():
	select = int(input("chose process"))
	return select
def inputs():	
	num1 = int(input("please chose a number"))
	return num1

menue()
select = menueInput()

if select > 4:
	print("I cannot do that jim ")
	menue()
	menueInput()
	
if select < 1:
	print("I cannot do that jim")
	menue()
	menueInput()
	
if select == 1:
	num1 = inputs()
	num2 = inputs()
	inputs()
	print(num1+num2)
	
if select == 2:
	num1 = inputs()
	num2 = inputs()
	print(num1-num2)
	
	
