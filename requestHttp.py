from pysnmp.hlapi import *
import urllib.request
import time

def main():
    #Url a acceder
    url = 'http://google.com'

    #Medir el tiempo de respuesta 
    tiempoInicio = time.time()
    tiempoFinal = time.time()

    req = urllib .request.Request(url) 
    rea = urllib.request.urlopen(req)
    respuestaF = rea.read()

    #Medir el tiempo de respuesta final
    tiempoFinal = time.time()
    print("Tiempo de respuesta: " + str(tiempoFinal-tiempoInicio)[:6])

    #Parte 2 tamanio en bytes
    tamBytes = bytes(str(respuestaF), 'utf-8')
    print("Tamanio en bytes: " + str(len(tamBytes)) + " bytes")

    #Parte 3 velocidad de descarga
    #Obtener megas
    velocidadDeDescarga = (len(tamBytes)/tiempoFinal) * 1024 * 1024 
    print("Velocidad de descarga: " + str(velocidadDeDescarga)[:6] + " MB/S")

main()

def consultaSNMP(comunidad,host,oid):
    errorIndication, errorStatus, errorIndex, varBinds = next(
        getCmd(SnmpEngine(),
               CommunityData(comunidad),
               UdpTransportTarget((host, 161)),
               ContextData(),
               ObjectType(ObjectIdentity(oid))))

    if errorIndication:
        print(errorIndication)
    elif errorStatus:
        print('%s at %s' % (errorStatus.prettyPrint(),errorIndex and varBinds[int(errorIndex) - 1][0] or '?'))
    
    else:
        for varBind in varBinds:
            varB=(' = '.join([x.prettyPrint() for x in varBind]))
            resultado= varB.split()[2]
    return resultado
