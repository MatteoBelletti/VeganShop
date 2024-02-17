import product
import warehouse
import sys


def print_commands():
    """
    Stampa i comandi disponibili.
    """
    print("aggiungi: aggiungi un prodotto al magazzino")
    print("elenca: elenca i prodotto in magazzino")
    print("vendita: registra una vendita effettuata")
    print("profitti: mostra i profitti totali")
    print("aiuto: mostra i possibili comandi")
    print("chiudi: esci dal programma")
    return


def read_str(instructions: str) -> str:
    """
    Legge una stringa dall'input.

    Args:
        instructions (str): Istruzioni da mostrare all'utente.

    Returns:
        str: La stringa letta dall'utente.
    """
    return input(instructions)


def read_float(instructions: str) -> float:
    """
    Legge un valore float dall'input.

    Args:
        instructions (str): Istruzioni da mostrare all'utente.

    Returns:
        float: Il valore float letto dall'utente.
    """
    while True:
        try:
            value = float(input(instructions))
            return value
        except Exception as e:
            print("Errore durante la lettura del valore, ripetere...")
            print(f"Dettagli eccezione: {e}")


def read_int(instructions: str) -> int:
    """
    Legge un valore intero dall'input.

    Args:
        instructions (str): Istruzioni da mostrare all'utente.

    Returns:
        int: Il valore intero letto dall'utente.
    """
    while True:
        try:
            value = int(input(instructions))
            return value
        except Exception as e:
            print("Errore durante la lettura del valore, ripetere...")
            print(f"Dettagli eccezione: {e}")


def help_command():
    """
    Mostra i comandi disponibili.
    """
    print_commands()


def another_time():
    """
    Chiede all'utente se desidera eseguire un'altra operazione.

    Returns:
        bool: True se l'utente vuole eseguire un'altra operazione, False altrimenti.
    """
    while True:
        redo_command = input("Aggiungere un altro prodotto ? (si/no): ")
        if redo_command.lower() == "no":
            return False
        elif redo_command.lower() == "si":
            return True
        else:
            print("devi scrivere si o no...")


class Program:
    def __init__(self, warehouse_obj: warehouse.Warehouse):
        """
        Inizializza il programma con un'istanza del magazzino.

        Args:
            warehouse_obj (warehouse.Warehouse): Un'istanza del magazzino.
        """
        self.warehouse_obj = warehouse_obj

    def switch_command(self, command):
        """
        Esegue il comando specificato.

        Args:
            command (str): Il comando da eseguire.
        """
        command = command.lower()
        if command == "aggiungi":
            self.upsert_product_to_warehouse()
        elif command == "elenca":
            self.list_warehouse_products()
        elif command == "vendita":
            self.record_sale()
        elif command == "profitti":
            self.print_sales_summary()
        elif command == "aiuto":
            help_command()
        elif command == "chiudi":
            print("Bye bye")
            sys.exit(0)
        else:
            print("Comando non valido")
            print("I comandi disponibili sono i seguenti")
            help_command()

    def start(self):
        """
        Avvia il programma, consentendo all'utente di inserire comandi fino a quando non viene chiuso.
        """
        while True:
            command = input("Inserisci un comando: ")
            self.switch_command(command)

    def record_sale(self):
        """
        Registra una vendita.
        """
        try:
            product_name = read_str("Nome del prodotto: ")
            product_quantity = read_int("Quantità: ")
            product_in_warehouse = self.warehouse_obj.get_product(product_name)
            if product_in_warehouse is None:
                print("Prodotto non in magazzino - ridigitare")
                self.record_sale()
                return
            else:
                sales_data = self.warehouse_obj.record_sales(product_name, product_quantity)
                print("VENDITA REGISTRATA")
                print(f"{sales_data[1]} X {sales_data[0]}:€ {sales_data[2]}")
                print(f"Totale:€ {sales_data[3]}")

            if another_time():
                self.record_sale()
            else:
                return
        except Exception as ex:
            print("Eccezione!")
            print(ex.args)
            if another_time():
                self.record_sale()
            else:
                return

    def list_warehouse_products(self):
        """
        Elenca i prodotti nel magazzino.
        """
        if len(self.warehouse_obj.products) == 0:
            print("Il magazzino è vuoto")
            return

        print(
            '{:<20} {:<20} {:<20}'.format(
                "PRODOTTO",
                "QUANTITA'",
                "PREZZO"
            ))

        for warehouse_product in self.warehouse_obj.products:
            if isinstance(warehouse_product, product.Product):
                print(
                    '{:<20} {:<20} {:<20}'.format(
                        warehouse_product.name,
                        f"{warehouse_product.quantity}",
                        "€ " + f"{warehouse_product.sale_price:.2f}"
                    ))

    def upsert_product_to_warehouse(self):
        """
        Aggiunge o aggiorna un prodotto nel magazzino.
        """
        product_name = read_str("Nome del prodotto: ")
        product_quantity = read_int("Quantità: ")
        product_in_warehouse = self.warehouse_obj.get_product(product_name)
        if product_in_warehouse is None:
            product_purchase_price = read_float("Prezzo di acquisto: ")
            product_sales_price = read_float("Prezzo di vendita: ")
            product_sales = 0
        else:
            product_purchase_price = product_in_warehouse.purchase_price
            product_sales_price = product_in_warehouse.sale_price
            product_sales = product_in_warehouse.sales

        product_dto = product.Product(
            product_name,
            product_quantity,
            product_purchase_price,
            product_sales_price,
            product_sales
        )

        self.warehouse_obj.upsert_product(product_dto)

        print(f"AGGIUNTO: {product_quantity} X {product_name}")

        if another_time():
            self.upsert_product_to_warehouse()
        else:
            return

    def print_sales_summary(self):
        """
        Stampa un riepilogo delle vendite.
        """
        profits_data = self.warehouse_obj.get_sales_data()
        print(f"Profitto:")
        print(f"Lordo: € {profits_data[0]}")
        print(f"Netto: € {profits_data[1]}")
