import time
def start():
	try:
		s = int(input("Ecrivez un nombre de secondes \n->"))
		for t in range(s):
			print(s, "restantes")
			time.sleep(1)
			s-=1
		print("tu as fini, cher ami")
		start()
	except ValueError:
		print("chiffre invalide")
		start()
start()