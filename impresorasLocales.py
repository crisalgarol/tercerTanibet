# Example of getting a list of printers
import cups


def consultaLibreria():

	cups.setServer("127.0.0.1")
	cups.setPort(631)
	conn = cups.Connection()
	printers = conn.getPrinters ()

	#Estado de impresiones

	#
	# print( "f: " + str(printers))

	for printer in printers:
		nombreImpresora = printers[printer]["printer-make-and-model"]
		estadoImpresora = printers[printer]["printer-state"] 
		estadoTintaImpresora = printers[printer]["printer-state-reasons"]

	#Imprimir estado
	print("IMPRESORA: " + str(nombreImpresora))
	print("ESTADO: " + str(estadoImpresora))


	#Niveles de tinta

	if 'marker-supply' in estadoTintaImpresora:
		print("Niveles de tinta:  BAJOS")
	else:
		print("Niveles de tinta: NORMAL")

def main():

	consultaLibreria()

main()


