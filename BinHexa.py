# Ejercicio suma binarios y hexa (enteros, positivos), pasaje entre sistemas (AS)
from random import randint

#Diccionarios
diccio_bin_to_hex = {'0000': '0', '0001' : '1', '0010': '2', '0011': '3', '0100': '4', '0101' : '5', '0110' : '6','0111' : '7', '1000' : '8','1001': '9','1010': 'A', '1011': 'B','1100': 'C','1101' : 'D','1110': 'E','1111': 'F'}
diccio_hex_to_bin = {'0': '0000', '1' : '0001', '2': '0010', '3': '0011', '4': '0100', '5' : '0101', '6' : '0110', '7' : '0111', '8' : '1000', '9' : '1001', 'A' :'1010' , 'B' :'1011', 'C' :'1100','D' :'1101' ,'E' :'1110','F' :'1111'}
diccio_hex_to_dec = {'0': 0, '1' : 1, '2': 2, '3': 3, '4': 4, '5' : 5, '6' : 6, '7' : 7, '8' :8 , '9' : 9, 'A' :10 , 'B' : 11, 'C' : 12,'D' :13 ,'E' : 14,'F' : 15}
diccio_dec_to_hex = {0: '0', 1 : '1', 2: '2', 3: '3', 4: '4', 5 : '5', 6 : '6', 7 : '7', 8 :'8' , 9 : '9', 10: 'A' , 11:  'B' , 12: 'C', 13: 'D' ,14: 'E' ,15: 'F' }
#Sets (para definir qué caracteres son válidos para el sistema)
hexa_codes = {'0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'A', 'B', 'C', 'D', 'E', 'F'}
bin_codes = {'0', '1'}


def valid_hexa(h_number):
	hexa_string= str(h_number)    # me aseguro que sea string para validar cada dígito como cadena
	hexa_ok=True
	for i in range (len(hexa_string)):
		if hexa_string[i] in hexa_codes:
			pass
		else:
			hexa_ok=False
			print (hexa_string[i] + " is not a valid hexa character")
			break
	return hexa_ok
	
def valid_bin(b_number):
	bin_string= str(b_number)    # me aseguro que sea string para validar cada dígito como cadena
	bin_ok=True
	for i in range (len(bin_string)):
		if bin_string[i] in bin_codes:
			pass
		else:
			bin_ok=False
			print (bin_string[i] + " is not a valid binary character")
			break
	return bin_ok
	
def hexa_to_bin(h_number):
	hexa_string= str(h_number)    # me aseguro que sea string para validar cada dígito como cadena
	bin_string=""
	for i in range (len(hexa_string)):
		bin_string = bin_string + diccio_hex_to_bin[hexa_string[i]] 
	return bin_string


def bin_to_hexa(b_number):
	bin_string= str(b_number)    # me aseguro que sea string para validar cada dígito como cadena
	hexa_string=""
	# Completo el binario al nibble, para poder usar el diccionario
	if (len(bin_string) // 4) == (len(bin_string) / 4):
		faltan_digitos = 0
	else:
 		faltan_digitos = 4 - len(bin_string) % 4
	for i in range (faltan_digitos):
		bin_string = '0' + bin_string
	for i in range (0, len(bin_string), 4):
		hexa_string = hexa_string + str(diccio_bin_to_hex[bin_string[i:i+4]] )
	return(hexa_string)


def suma_hexa(h_number1, h_number2):
	carry=0
	resultado=''
	hexa_string1= str(h_number1)
	hexa_string2= str(h_number2)
	if len(hexa_string1) > len(hexa_string2):
		for i in range (len(hexa_string2), len(hexa_string1)):
			hexa_string2= '0'+hexa_string2    # completo para tener igual cantidad de dígitos
	if len(hexa_string2) > len(hexa_string1):
		for i in range (len(hexa_string1), len(hexa_string2)):
			hexa_string1= '0'+hexa_string1    # completo para tener igual cantidad de dígitos
	for i in range (len(hexa_string1)-1, -1, -1):
		parcial=  diccio_hex_to_dec[hexa_string1[i]] + diccio_hex_to_dec[hexa_string2[i]] + carry
		carry = parcial // 16
		sobra = parcial % 16
		resultado = diccio_dec_to_hex[sobra] + resultado
	if carry > 0:
		resultado = str(carry) + resultado
	return resultado
	
	
def suma_bin(b_number1, b_number2):
	carry=0
	resultado=''
	bin_string1= str(b_number1)
	bin_string2= str(b_number2)
	if len(bin_string1) > len(bin_string2):
		for i in range (len(bin_string2), len(bin_string1)):
			bin_string2= '0'+ bin_string2    # completo para tener igual cantidad de dígitos
	if len(bin_string2) > len(bin_string1):
		for i in range (len(bin_string1), len(bin_string2)):
			bin_string1= '0'+bin_string1    # completo para tener igual cantidad de dígitos
	for i in range (len(bin_string1)-1, -1, -1):
		parcial=  int(bin_string1[i]) + int(bin_string2[i]) + carry
		if parcial < 2:
			resultado = str(parcial) + resultado
			carry = 0
		elif parcial == 2:
			resultado = '0' + resultado
			carry = 1
		elif parcial == 3:
			resultado = '1' + resultado
			carry = 1
	if carry > 0:
		resultado = '1' + resultado
	return resultado

def hexa_to_dec (h_number):
	hexa_string= str(h_number)    # me aseguro que sea string para usar cada dígito como cadena
	decimal=0
	for i in range (len(hexa_string)):
		decimal = decimal + diccio_hex_to_dec[hexa_string[i]] * (16 ** (len(hexa_string) -1 - i ))
	return decimal


	

# Programa principal

print("Programa para jugar con binarios y hexa")
opcion = int(input("Ingresá tu opción \n 1 : Convertir binario a hexa \n 2 : Convertir hexa a binario \n 3 : Sumar dos hexa (enteros, positivos) \n 4 : Sumar dos binarios (enteros, positivos) \n 0: Salir \n"))
while opcion != 0:
	if opcion == 1:   # Convertir binario a hexa
		bin= input("Ingresá el número binario a convertir:  ")
		if valid_bin(bin):
			print("El número binario " + bin + " es el hexa: " + bin_to_hexa(bin))
		else:
			print("No es un binario válido")
	elif  opcion == 2:   #  Convertir hexa a binario
		hexa= input("Ingresá el número hexadeciaml a convertir:  ")
		if valid_hexa(hexa.upper()):
			print("El número hexadecimal " + hexa + " es el binario: " +   hexa_to_bin(hexa.upper()))
		else:
			print("No es un hexadecimal válido")
	elif  opcion == 3:   #  Sumar dos hexa (enteros, positivos)
		hexa1= input("Ingresá el primer  hexadeciaml a sumar:  ")
		while valid_hexa(hexa1.upper()) == False: 
			hexa1= input("Ingresá un número hexadeciaml válido:  ")
		hexa2= input("Ingresá el segundo hexadeciaml a sumar:  ")
		while valid_hexa(hexa2.upper()) == False: 
			hexa2= input("Ingresá un número hexadeciaml válido:  ")
		print("La suma de los hexas  " + hexa1.upper() + " y " + hexa2.upper() + " es el HEXA: "  +  suma_hexa(hexa1.upper(), hexa2.upper()) )
	elif  opcion == 4:   #  Sumar dos binarios (enteros, positivos)
		bin1= input("Ingresá el primer binario a sumar:  ")
		while valid_bin(bin1) == False: 
			bin1= input("Ingresá un número binario válido:  ")
		bin2= input("Ingresá el segundo binario a sumar:  ")
		while valid_bin(bin2) == False: 
			bin2= input("Ingresá un número binario válido:  ")
		print("La suma de los binarios  " + bin1 + " y " + bin2 + " es el BINARIO: "  +  suma_bin(bin1, bin2) )

	opcion = int(input("\n Ingresá tu opción \n 1 : Convertir binario a hexa \n 2 : Convertir hexa a binario \n 3 : Sumar dos hexa (enteros, positivos) \n 4 : Sumar dos binarios (enteros, positivos) \n 0: Salir \n"))

print ("Terminó")
