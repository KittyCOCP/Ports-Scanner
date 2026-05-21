import socket

object = "127.0.0.1"

try:
    print(f"---- Estos son los puertos abiertos: ----- ")
    for port in range(1, 65535):
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        # objeto de conección
        s.settimeout(0.1)  # Tiempo de espera corto
        result = s.connect_ex((object, port))

        if result == 0:
            print(f"Port {port}")

        s.close()

except:
    pass
