import requests
import json
import time
from pathlib import Path
import sys

def download_pokemon_data():
    # URL base de la API
    base_url = "https://pokeapi.co/api/v2/pokemon"
    
    # Lista para almacenar todos los pokemon
    all_pokemon = []
    
    # Crear directorio para las imágenes si no existe
    Path("pokemon_images").mkdir(exist_ok=True)
    
    try:
        # Primero obtenemos el número total de pokemon
        response = requests.get(f"{base_url}?limit=1")
        response.raise_for_status()
        total_pokemon = response.json()['count']
        
        print(f"Total Pokémon a descargar: {total_pokemon}")
        
        # Obtener todos los pokemon
        response = requests.get(f"{base_url}?limit={total_pokemon}")
        response.raise_for_status()
        results = response.json()['results']
        
        # Procesar cada pokemon
        for index, pokemon in enumerate(results, 1):
            try:
                # Obtener detalles del pokemon
                print(f"Descargando datos de {pokemon['name']} ({index}/{total_pokemon})...")
                
                response = requests.get(pokemon['url'])
                response.raise_for_status()
                pokemon_data = response.json()
                
                # Extraer solo la información relevante
                processed_pokemon = {
                    'id': pokemon_data['id'],
                    'name': pokemon_data['name'],
                    'height': pokemon_data['height'],
                    'weight': pokemon_data['weight'],
                    'types': [t['type']['name'] for t in pokemon_data['types']],
                    'abilities': [a['ability']['name'] for a in pokemon_data['abilities']],
                    'stats': {
                        stat['stat']['name']: stat['base_stat'] 
                        for stat in pokemon_data['stats']
                    },
                    'sprites': {
                        'front_default': pokemon_data['sprites']['front_default'],
                        'back_default': pokemon_data['sprites']['back_default'],
                        'front_shiny': pokemon_data['sprites']['front_shiny'],
                        'back_shiny': pokemon_data['sprites']['back_shiny']
                    }
                }
                
                # Obtener artwork oficial si está disponible
                if 'official-artwork' in str(pokemon_data['sprites']):
                    processed_pokemon['official_artwork'] = (
                        pokemon_data['sprites']['other']
                        ['official-artwork']['front_default']
                    )
                             
                all_pokemon.append(processed_pokemon)
                
                # Pequeña pausa para no sobrecargar la API
                time.sleep(1)
                
            except requests.exceptions.RequestException as e:
                print(f"Error descargando {pokemon['name']}: {e}")
                continue
            except KeyError as e:
                print(f"Error procesando datos de {pokemon['name']}: {e}")
                continue
            
            # Guardar progreso cada 10 pokemon
            if index % 10 == 0:
                with open('pokemon_data.json', 'w', encoding='utf-8') as f:
                    json.dump(all_pokemon, f, indent=2, ensure_ascii=False)
                print(f"Progreso guardado: {index}/{total_pokemon} Pokemon")
        
        # Guardar todos los datos al final
        with open('pokemon_data.json', 'w', encoding='utf-8') as f:
            json.dump(all_pokemon, f, indent=2, ensure_ascii=False)
        
        print("\n¡Descarga completada!")
        print(f"Total de Pokemon descargados: {len(all_pokemon)}")
        print("Los datos han sido guardados en 'pokemon_data.json'")
        
    except requests.exceptions.RequestException as e:
        print(f"Error de conexión: {e}")
        sys.exit(1)
    except Exception as e:
        print(f"Error inesperado: {e}")
        sys.exit(1)

if __name__ == "__main__":
    download_pokemon_data()