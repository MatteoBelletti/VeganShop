import json
import os

from program import Program
from warehouse import Warehouse


def check_create_file(file_path):
    # Ottieni il percorso della directory dal percorso del file
    directory = os.path.dirname(file_path)

    # Verifica se la directory non esiste, se non esiste, creala
    if not os.path.exists(directory):
        print(f"La directory '{directory}' non esiste. Creazione della directory...")
        try:
            os.makedirs(directory)
            print(f"La directory '{directory}' è stata creata con successo.")
        except Exception as e:
            print(f"Si è verificato un errore durante la creazione della directory '{directory}':")
            print(e)

    # Verifica se il file esiste, se non esiste, crealo
    if not os.path.exists(file_path):
        print(f"Il file '{file_path}' non esiste. Creazione del file...")
        try:
            with open(file_path, 'w') as f:
                print(f"Il file '{file_path}' è stato creato con successo.")
                json.dump(list(), f)  # Inizializza il file con una lista vuota
                print(f"Il file '{file_path}' è stato inizializzato con successo.")
        except Exception as e:
            print(f"Si è verificato un errore durante la creazione del file '{file_path}':")
            print(e)
    else:
        print(f"Il file '{file_path}' esiste già.")


def main():
    check_create_file("../db/warehouse_db.json")
    warehouse = Warehouse("../db/warehouse_db.json")
    program = Program(warehouse)
    program.start()


if __name__ == "__main__":
    main()
