# Pokémon Data Script

This project contains Python scripts to download data for all Pokémon in JSON format and then import them into a MySQL table.

## Main Files

- `pokemon_pip.py`: Script to download Pokémon data and save it to a JSON file.
- `import_to_mysql.py`: Script to import data from the JSON file into a MySQL table.
- `pokemon_data.json`: Generated file containing Pokémon data in JSON format.

## Requirements

- Python 3.8 or higher
- MySQL Server
- Python packages listed in `requirements.txt` (if applicable)

## Usage

1. Run `pokemon_pip.py` to download the Pokémon data:
   ```bash
   python pokemon_pip.py
   ```

2. Run `import_to_mysql.py` to import the data into MySQL:
   ```bash
   python import_to_mysql.py
   ```

## Notes

- Make sure to properly configure MySQL credentials in `import_to_mysql.py`.
- The `pokemon_data.json` file will be generated automatically when running `pokemon_pip.py`.

## Contributions

If you want to contribute to this project, please open an issue or submit a pull request.