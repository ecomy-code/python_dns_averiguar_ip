import socket
import time
import datetime


def convertir_url_ip(namePage):
	ipd = socket.gethostbyname(namePage)
	ipd = f"La ip de {namePage} es:  {ipd}"
	return ipd

if __name__=='__main__':
	namePage=''
	endBucle = True


	if namePage.upper() == 'FIN':
		endBucle = False
	else:
		endBucle = True

	print ('Agrega alguna dirección web para decirte su IP')
	print ('ej: google.com')
	while endBucle:
		
		print ('')
		print("Si quieres salir escribe  fin")
		namePage = str(input('Dirección Web: '))
		print ('')
		print ('')
		if namePage.upper() == 'FIN':
			endBucle = False
		else:

			try:
				resp = str(convertir_url_ip(namePage))
				print (f'{resp}')
			except Exception as e:
				print(e)
			print ('')
			endBucle = True

#Yeisson Araya
