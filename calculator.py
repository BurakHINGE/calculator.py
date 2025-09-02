def calc(x,y,operator):
	
	if operator not in "+-**/":
		return "Sadece +, -, *, /, ** işaretlerini kullanabilirsiniz!"

	if operator == "+":
		return(str(x) + " " + operator + " " + str(y) + " = " + str(x + y))

	if operator == "-":
		return(str(x) + " " + operator + " " + str(y) + " = " + str(x - y))

	if operator == "*":
		return(str(x) + " " + operator + " " + str(y) + " = " + str(x * y))

	if operator == "/":
		return(str(x) + " " + operator + " " + str(y) + " = " + str(x / y))

	if operator == "**":
		return(str(x) + " " + operator + " " + str(y) + " = " + str(x ** y))


while True:

	x = int(input("İlk sayınızı seçiniz: "))
	y = int(input("İkinci sayınızı seçiniz: "))
	operator = input("Yapmak istediğiniz işlemi seçiniz: +, -, *, /, ** :")

	print(calc(x,y,operator))
