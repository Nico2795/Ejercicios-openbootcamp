import sqlite3
import getpass

def main():
    username = input("Nombre de usuario:")
    password = getpass.getpass("Contraseña:", None)

    if verifica_usuario(username, password):
        print("Login correcto")
    else:
        print("Login incorrecto")

def verifica_usuario(username,password):
    conn = sqlite3.connect('miaplicacion.db')
    cursor = conn.cursor()
    query = f"SELECT id FROM users WHERE username='{username}'AND password='{password}'"
    print("Query a ejecutar", query)
    rows = cursor.execute(query)
    data = rows.fetchone()
    print("Data es", type(data))



    cursor.close()
    conn.close()

main()
