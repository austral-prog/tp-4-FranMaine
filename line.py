def line():
	print("TO DO")
	A= float(input("Ingrese el coeficiente A: "))
	B= float(input("Ingrese el coeficiente B: "))
	X1= float(input("Ingrese el coeficiente X1: "))
	X2= float(input("Ingrese el coeficiente X2: "))
	print(f"El coeficiente A de su ecuación de la recta es: {A}")
	print(f"El coeficiente B de su ecuación de la recta es: {B}")
	print(f"El coeficiente X1 de su ecuación de la recta es: {X1}")
	print(f"El coeficiente X2 de su ecuación de la recta es: {X2}")
	print()
	Ecu=("Para la siguiente ecuación:")
	print(Ecu)
	print(f"\tY={A}X + {B}")
	print()
	print("Dados los sigueintes puntos:")
	Y1= (A*X1+B)
	Y2= (A*X2+B)
	print(f"\tP1 ({X1}, {Y1})")
	print(f"\tP1 ({X2}, {Y2})")
	print(f"La distancia entre ellos es: {((Y1-Y2)**2+(X1-X2)**2)**0.5}")

line()
