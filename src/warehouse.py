import json

from product import *


class Warehouse:
    def __init__(self, path_warehouse: str):
        """
        Inizializza un magazzino.

        Args:
            path_warehouse (str): Il percorso del magazzino.
        """
        self.products = []  # Lista dei prodotti nel magazzino
        self.path_warehouse = path_warehouse  # Percorso del file del magazzino
        self.init_warehouse()  # Inizializza il magazzino all'avvio

    def get_product(self, product_name: str) -> Product | None:
        """
        Ottiene un prodotto dal magazzino in base al nome.

        Args:
            product_name (str): Il nome del prodotto da cercare.

        Returns:
            Product | None: Il prodotto trovato o None se non trovato.
        """
        for i in self.products:
            if i.name.lower() == product_name.lower():
                return i

        return None

    def upsert_product(self, product: Product):
        """
        Aggiorna o inserisce un prodotto nel magazzino.

        Args:
            product (Product): Il prodotto da aggiungere o aggiornare.

        Raises:
            ValueError: Se il prodotto non è di tipo Product o la quantità è negativa.
        """
        assert product.quantity > 0, "La quantità deve essere positiva"

        if not isinstance(product, Product):
            raise ValueError("In questo magazzino solo prodotti! (vegani...)")

        existing_product = self.get_product(product.name)

        if existing_product is None:
            self.products.append(product)
        else:
            existing_product.quantity += product.quantity

        self.save_warehouse()

    def get_sales_data(self) -> tuple:
        """
        Ottiene i dati sulle vendite totali e i profitti.

        Returns:
            tuple: Una tupla contenente il valore totale delle vendite e il valore totale dei profitti.
        """
        total_sales_value = 0
        total_product_cost = 0
        for i in self.products:
            if isinstance(i, Product):
                if i.sales > 0:
                    total_sales_value += i.sales * i.sale_price
                    total_product_cost += i.quantity * i.purchase_price

        return total_sales_value, total_sales_value - total_product_cost

    def record_sales(self, product_name: str, sales_quantity: int) -> tuple:
        """
        Registra le vendite di un prodotto.

        Args:
            product_name (str): Il nome del prodotto venduto.
            sales_quantity (int): La quantità venduta.

        Returns:
            tuple: Una tupla contenente il nome del prodotto, la quantità venduta, il prezzo di vendita del prodotto e il totale delle vendite.
        """
        assert sales_quantity > 0, "La quantità deve essere positiva"
        product = self.get_product(product_name)
        if product is None:
            raise TypeError("Prodotto non trovato!")

        assert sales_quantity <= product.quantity, "Quantità insufficiente!"

        product.quantity -= sales_quantity
        product.sales += sales_quantity

        self.save_warehouse()

        return product_name, sales_quantity, product.sale_price, product.sale_price * sales_quantity

    def save_warehouse(self):
        """
        Salva lo stato corrente del magazzino.
        """
        data = list()
        for i in self.products:
            if isinstance(i, Product):
                data.append(i.to_dict())

        with open(self.path_warehouse, "w+") as final:
            json.dump(data, final, indent=6)

    def init_warehouse(self):
        """
        Inizializza il magazzino caricando i dati dal file di magazzino.
        """
        with open(self.path_warehouse, encoding='utf-8') as json_file:
            data = json.load(json_file)
            for i in data:
                self.products.append(Product.from_dict(i))
