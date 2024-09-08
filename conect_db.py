import mysql.connector
from dotenv import load_dotenv
import os


load_dotenv()

def insert_data(df_combinado):
    
    conexion = mysql.connector.connect(
        host=os.getenv('DB_HOST'),
        user=os.getenv('DB_USER'),
        password=os.getenv(''),
        database=os.getenv('school')
    )
    
    cursor = conexion.cursor()

    try:
        
        for index, row in df_combinado.iterrows():
            query = """
            INSERT INTO estudiantes (nombre, años, grado, calificaciones)
            VALUES (%s, %s, %s, %s)
            """
            cursor.execute(query, (row['nombre'], row['años'], row['grado'], row['calificaciones']))
        
        
        conexion.commit()

        print("Datos insertados exitosamente")

    except mysql.connector.Error as err:
        print(f"Error: {err}")
        conexion.rollback()

    finally:
        cursor.close()
        conexion.close()

