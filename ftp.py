from ftplib import FTP
import time

folder 	= 'files'
fileGet = 'test.txt'
filePut = 'myfile2.txt'

def getFTP(host, user, passwd, path, file):

	print('--- GET ---')

	ftp = FTP(host) 	# connect to host, default port
	ftp.login(user, passwd)	# user anonymous, passwd anonymous@
	ftp.cwd(path)           	# change into "debian" directory
	ftp.retrlines('LIST') 

	millisStart = int(round(time.time() * 1000))

	ftp.retrbinary('RETR ' + file, open(file, 'wb').write)

	millisEnd = int(round(time.time() * 1000))
	segTotal = (millisEnd - millisStart)/1000

	print ('Tiempo de respuesta: ' + str(segTotal) + ' segundos.')

	files = ftp.nlst()
	totalFiles = len(files);

	print ('Numero de archivos: ' + str(totalFiles))
	print ('Archivos: ' + str(files))

	ftp.quit()

def putFTP(host, user, passwd, path, file):

	print('--- PUT ---')

	ftp = FTP(host) 	# connect to host, default port
	ftp.login(user, passwd)	# user anonymous, passwd anonymous@
	ftp.cwd(path)           	# change into "debian" directory
	ftp.retrlines('LIST') 

	millisStart = int(round(time.time() * 1000))

	ftp.storbinary('STOR ' + file, open(file, 'rb'))
	ftp.sendcmd('SITE CHMOD 777 /' + path + '/' + file)

	millisEnd = int(round(time.time() * 1000))
	segTotal = (millisEnd - millisStart)/1000

	print ('Tiempo de respuesta: ' + str(segTotal) + ' segundos.')

	files = ftp.nlst()
	totalFiles = len(files);

	print ('Numero de archivos: ' + str(totalFiles))
	print ('Archivos: ' + str(files))

	ftp.quit()


def main():

	#getFTP('192.168.0.6', 'ftpsalomon', '1234', 'files', 'salomon.txt')
	putFTP('192.168.0.6', 'ftpsalomon', '1234', 'files', 'test.txt')

main()
