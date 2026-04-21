# Importamos la libreriaa socket
# Esta libreria permite trabajar con redes (conexiones, puertos, IPs)
import socket

# --------------------------------
# FUNCION: Resolver dominio -> IP.
# --------------------------------

# Funcion
def resolve_target(target):
    '''
    Convierte un dominio (ej: google.com) a IP.
    '''
    try:
        ip = socket.gethostbyname(target)
        return ip
    except socket.gaierror:
        print("[!] Invalid target")
        return None



# ----------------------------------
# FUNCION: Escaneo rangos de puertos
# ----------------------------------

# Funcion
def scan_ports(target, start_port, end_port):

    '''
    Escanea un rango de puertos en el target.
    '''

    print("\n[+] Scanning {target} from port {start_port} to {end_port}\n")  

    open_ports = 0

    # Iteramos sobre el rango de puertos.
    for port in range(start_port, end_port + 1):

        try:
            # Creamos un socket TCP
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            # Tiempo maximo de espera (0.5 segundo)
            sock.settimeout(0.5)

            # Intentamos conexion.
            result = sock.connect_ex((target, port))


            # Si el puerto esta abierto
            if result == 0:
                print(f"[Open] {port} ({port})")
                open_ports += 1


            # Cerramos conexion siempre
            sock.close()
        
        except Exception as e:
            print(f"Error on port {port}: {e}")
    
    print(f"\n[+] Total open ports: {open_ports}")
    print("[+] Scan complete\n")



# -----------------------
# MAIN
# -----------------------+

if __name__ == "__main__":

    # Pedimos al usuario el objetivo
    target_input = input("Enter target (IP or domain): ")

    # Convertimos a IP
    target = resolve_target(target_input)

    if target:
        try:
            # Pedimos rango de puertos.
            start_port = int(input("Enter start port: "))
            end_port = int(input("Enter end port: "))

            # Ejecutamos escaneo.
            scan_ports(target, start_port, end_port)

        except ValueError:
            print("[!] Please enter valid port numbers")


