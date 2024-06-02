import smtplib
import time
from colorama import Fore, Style

# Inicializar colorama
Fore.RESET

def check_smtp_users(smtp_ip, smtp_port, user_list):
    # Función para conectar al servidor SMTP
    def connect_to_server():
        server = smtplib.SMTP(smtp_ip, smtp_port)
        return server

    # Función para verificar un usuario SMTP
    def verify_user(server, user):
        try:
            code, message = server.verify(user)
            if code == 252:
                print(Fore.GREEN + f"User {user} exists: {message.decode()}" + Style.RESET_ALL)
            else:
                print(Fore.RED + f"User {user} does not exist: {message.decode()}" + Style.RESET_ALL)
        except smtplib.SMTPServerDisconnected:
            print(Fore.RED + f"Server disconnected while verifying user {user}. Reconnecting..." + Style.RESET_ALL)
            raise
        except Exception as e:
            print(Fore.RED + f"Failed to verify user {user}: {e}" + Style.RESET_ALL)

    # Conectar al servidor SMTP inicialmente
    server = connect_to_server()
    
    # Iterar sobre la lista de usuarios para verificar
    for user in user_list:
        try:
            verify_user(server, user)
        except smtplib.SMTPServerDisconnected:
            # Reconectar si el servidor se desconecta
            server = connect_to_server()
            verify_user(server, user)
        except Exception as e:
            print(Fore.RED + f"Unexpected error: {e}" + Style.RESET_ALL)
            time.sleep(1)  # Esperar 1 segundo antes de continuar para evitar sobrecargar el servidor

    # Cerrar la conexión con el servidor SMTP
    server.quit()

# Banner ASCII
banner = """

███████╗███╗   ███╗████████╗██████╗     ██╗   ██╗███████╗███████╗██████╗     ███████╗███╗   ██╗██╗   ██╗███╗   ███╗
██╔════╝████╗ ████║╚══██╔══╝██╔══██╗    ██║   ██║██╔════╝██╔════╝██╔══██╗    ██╔════╝████╗  ██║██║   ██║████╗ ████║
███████╗██╔████╔██║   ██║   ██████╔╝    ██║   ██║███████╗█████╗  ██████╔╝    █████╗  ██╔██╗ ██║██║   ██║██╔████╔██║
╚════██║██║╚██╔╝██║   ██║   ██╔═══╝     ██║   ██║╚════██║██╔══╝  ██╔══██╗    ██╔══╝  ██║╚██╗██║██║   ██║██║╚██╔╝██║
███████║██║ ╚═╝ ██║   ██║   ██║         ╚██████╔╝███████║███████╗██║  ██║    ███████╗██║ ╚████║╚██████╔╝██║ ╚═╝ ██║
╚══════╝╚═╝     ╚═╝   ╚═╝   ╚═╝          ╚═════╝ ╚══════╝╚══════╝╚═╝  ╚═╝    ╚══════╝╚═╝  ╚═══╝ ╚═════╝ ╚═╝     ╚═╝
                                                                                                          by p314d0                                          
"""

print(banner)

# Leer usuarios desde un archivo de texto
def read_user_list(file_path):
    with open(file_path, 'r') as file:
        return [line.strip() for line in file.readlines()]

# Configuración del servidor SMTP
smtp_ip = "10.129.189.241"  # Reemplaza con la IP de tu servidor SMTP
smtp_port = 25             # Reemplaza con el puerto de tu servidor SMTP

# Leer la lista de usuarios desde el archivo usuarios.txt
user_list = read_user_list('users.txt') # Reemplaza con tu lista de usuarios

# Llamada a la función principal para verificar los usuarios
check_smtp_users(smtp_ip, smtp_port, user_list)