# Pokémon Data Script

Este proyecto contiene scripts en Python para descargar datos de todos los Pokémon en formato JSON y luego importarlos a una tabla MySQL.

## Archivos principales

- `pokemon_pip.py`: Script para descargar los datos de los Pokémon y guardarlos en un archivo JSON.
- `import_to_mysql.py`: Script para importar los datos del archivo JSON a una tabla MySQL.
- `pokemon_data.json`: Archivo generado que contiene los datos de los Pokémon en formato JSON.

## Requisitos

- Python 3.8 o superior
- MySQL Server
- Paquetes de Python listados en `requirements.txt` (si aplica)

## Uso

1. Ejecuta `pokemon_pip.py` para descargar los datos de los Pokémon:
   ```bash
   python pokemon_pip.py
   ```

2. Ejecuta `import_to_mysql.py` para importar los datos a MySQL:
   ```bash
   python import_to_mysql.py
   ```

## Notas

- Asegúrate de configurar correctamente las credenciales de MySQL en `import_to_mysql.py`.
- El archivo `pokemon_data.json` se generará automáticamente al ejecutar `pokemon_pip.py`.

## Contribuciones

Si deseas contribuir a este proyecto, por favor abre un issue o envía un pull request.