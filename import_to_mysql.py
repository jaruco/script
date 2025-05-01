import json
import mysql.connector
from datetime import datetime

def import_to_mysql():
    # Leer el archivo JSON
    with open('pokemon_data.json', 'r', encoding='utf-8') as f:
        pokemon_data = json.load(f)
    
    # Configuración de la conexión a MySQL
    config = {
        'user': 'root',
        'password': 'Spain25!',
        'host': 'localhost',
        'database': 'pokemones'
    }
    
    try:
        # Establecer conexión
        conn = mysql.connector.connect(**config)
        cursor = conn.cursor()
        
        # Preparar la consulta de inserción
        insert_query = """
        INSERT INTO pokemons (id, name, height, weight, types, abilities, front_sprite, back_sprite, official_artwork, created_at, updated_at)
        VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
        ON DUPLICATE KEY UPDATE
            name = VALUES(name),
            height = VALUES(height),
            weight = VALUES(weight),
            types = VALUES(types),
            abilities = VALUES(abilities),
            front_sprite = VALUES(front_sprite),
            back_sprite = VALUES(back_sprite),
            official_artwork = VALUES(official_artwork),
            updated_at = VALUES(updated_at)
        """
        
        # Insertar cada Pokémon
        current_time = datetime.now()
        for pokemon in pokemon_data:
            values = (
                pokemon['id'],
                pokemon['name'],
                pokemon['height'],
                pokemon['weight'],
                json.dumps(pokemon['types']),
                json.dumps(pokemon['abilities']),
                pokemon['sprites']['front_default'],
                pokemon['sprites']['back_default'],
                pokemon['official_artwork'],
                current_time,
                current_time
            )
            cursor.execute(insert_query, values)
        
        # Confirmar los cambios
        conn.commit()
        print(f"Se han importado {len(pokemon_data)} Pokémon exitosamente")
        
    except mysql.connector.Error as err:
        print(f"Error: {err}")
    finally:
        if 'conn' in locals() and conn.is_connected():
            cursor.close()
            conn.close()

if __name__ == "__main__":
    import_to_mysql() 