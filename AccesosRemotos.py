import spur

def main():
    
    shell = spur.SshShell(hostname = "192.168.0.14",
        username = "stefan",
        password = "madrid_messi",
        port = 22,
        missing_host_key = spur.ssh.MissingHostKey.accept)
    with shell:
        result = shell.run(["snmpget", "-v2c", "-c", "Stefan10", "localhost", "1.3.6.1.2.1.2.2.1.10.1"])
        result2 = shell.run(["snmpget", "-v2c", "-c", "Stefan10", "localhost", "1.3.6.1.2.1.2.2.1.16.1"])
        result3 = shell.run(["snmpget", "-v2c", "-c", "Stefan10", "localhost", "1.3.6.1.2.1.1.3.0"])
    #shell = spur.LocalShell()
    #print(result.output) # prints hello
    var = result.output
    arreglo = var.split()
    inOc = arreglo[-1]
    print("Tráfico de entrada: " + str(inOc));
    
    #print(result2.output) # prints hello
    var2 = result2.output
    arreglo2 = var2.split()
    outOc = arreglo2[-1]
    print("Tráfico de salida: " + str(outOc));

    #print(result3.output) # prints hello
    var3 = result3.output
    arreglo3 = var3.split()
    upTime = arreglo3[-1]
    horas = upTime[0:1]
    minutos = upTime[2:4]
    segundos = upTime[5:]
    print("Timepo de actividad: " + str(horas) + " horas " + str(minutos) + " minutos " + str(segundos) + " segundos");
    
main()