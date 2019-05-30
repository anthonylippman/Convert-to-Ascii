import binascii

def b2a(b):
	return b.to_bytes((b.bit_length() + 7) // 8, 'big').decode()

def h2a(h):
	return bytes.fromhex(h).decode('ascii')

if __name__ == '__main__':

	answer = 'y'
	while answer == 'y':

		print("Menu:\n\n1) Binary to Ascii\n2) Hex to Ascii\n")
		choice = str(input("Please enter a number from the menu: "))

		if choice ==  '1':
			binary = input("Enter binary string: ")
			binary = binary.replace(" ", "")
			binary = int('0b' + binary, 2)
			bvalue = b2a(binary)
			print(bvalue)

		elif choice == '2':
			hexa = input("Enter hex string: ")
			hexa = hexa.replace(" ","")
			hvalue = h2a(hexa)
			print(hvalue)

		else:
			print("Please enter a valid number (Ex. 1) ")

		answer = input("Would you like to restart the program? (Y/N) ")
		answer = answer.lower()

