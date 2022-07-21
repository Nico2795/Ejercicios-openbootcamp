import sqlite3

def main():
    conn = sqlite3.connect('tarea1.db')
    cursor = conn.cursor()

    query = f"SELECT id FROM alumnos WHERE nombre = 'nico'"
    print("Este es el alumno que buscas")

    rows = cursor.execute(query)
    data = rows.fetchall()

    cursor.close()
    conn.close()

if __name__ == '__main__':
        main()
