# Importamos la libreriaa socket
# Esta libreria permite trabajar con redes (conexiones, puertos, IPs)
import socket

# -----------------------
# Resolver dominio -> IP
# -----------------------

# Funcion
def resolve_target(target):
    try:
        # gethostbyname convertira dominio -> IP
        ip = socket.gethostbyname(target)
        return ip

    except socket.gaierror:
        print("[!] Invalid target")
        return None



# -----------------------
# Escaneo de puertos
# -----------------------

# Funcion
def scan_target(target):

    # Diccionario de puertos comunes y su servicio
    common_ports = {
        21: "FTP",
        22: "SSH",
        23: "Telnet",
        80: "HTTP",
        443: "HTTPS",
        445: "SMB",
        3389: "RDP"
    }

    print("\n[+] Scanning {target}\n")  

    open_ports = 0

    # Hay que iterar sobre los puertos del diccionario
    for port, service in common_ports.items():

        try:
            # Creamos un socket TCP
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            # Tiempo maximo de espera (1 segundo)
            sock.settimeout(1)

            # connect_ex intenta conectarse al puerto
            # devuelve 0 si esta abierto
            result = sock.connect_ex((target, port))


            # Si el puerto esta abierto
            if result == 0:
                print(f"[Open] {port} ({service})")
                open_ports += 1


                # Detectaremos servicios inseguros
                if port == 21:
                    print("FTP is insecure")
                elif port == 23:
                    print("Tenet is insecure")
                elif port == 445:
                    print("SMB exposed")
                elif port == 3389:
                    print("RDP exposed")
            
            # Cerramos conexion siempre
            sock.close()
        
        except Exception as e:
            print(f"Error on port {port}: {e}")
    
    print(f"\n[+] Open ports found: {open_ports}")
    print("[+] Scan complete\n")



# -----------------------
# MAIN
# -----------------------+

if __name__ == "__main__":

    # Peddimos al usuario el objetivo
    target_input = input("Enter target (IP or domain): ")

    # Convertimos a IP
    target = resolve_target(target_input)

    # Si la IP es valida, escaneamos
    if target:
        scan_target(target)