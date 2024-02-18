class Product:
    def __init__(
            self,
            name: str,
            quantity: int,
            purchase_price: float = None,
            sale_price: float = None,
            sales: int = None
    ):
        """
        Inizializza un oggetto prodotto con le informazioni fornite.

        Args:
            name (str): Il nome del prodotto.
            quantity (int): La quantità del prodotto disponibile.
            purchase_price (float, optional): Il prezzo di acquisto del prodotto. Default è None.
            sale_price (float, optional): Il prezzo di vendita del prodotto. Default è None.
            sales (int, optional): Il numero di vendite del prodotto. Default è None.
        """
        self.name = name  # Nome del prodotto
        self.purchase_price = purchase_price  # Prezzo di acquisto del prodotto
        self.sale_price = sale_price  # Prezzo di vendita del prodotto
        self.quantity = quantity  # Quantità del prodotto disponibile
        self.sales = sales  # Numero di vendite del prodotto

    def item_profit(self) -> float:
        """
        Calcola il profitto per singolo articolo.

        Returns:
            float: Il profitto per singolo articolo.
        """
        return self.sale_price - self.purchase_price

    def total_item_profit(self) -> float:
        """
        Calcola il profitto totale per il prodotto.

        Returns:
            float: Il profitto totale per il prodotto.
        """
        return self.sales * (self.sale_price - self.purchase_price)

    def total_purchase_price(self) -> float:
        """
        Calcola il costo totale dell'acquisto del prodotto.

        Returns:
            float: Il costo totale dell'acquisto del prodotto.
        """
        return self.quantity * self.purchase_price

    def to_dict(self):
        """
        Converte l'oggetto Product in un dizionario.

        Returns:
            dict: Un dizionario contenente le informazioni dell'oggetto Product.
        """
        return {
            "name": self.name,
            "purchase_price": self.purchase_price,
            "sale_price": self.sale_price,
            "quantity": self.quantity,
            "sales": self.sales
        }

    @classmethod
    def from_dict(cls, dictionary):
        """
        Costruisce un oggetto Product da un dizionario.

        Args:
            dictionary (dict): Il dizionario contenente le informazioni per costruire l'oggetto.

        Returns:
            Product: Un oggetto Product costruito dal dizionario.
        """
        return cls(
            dictionary["name"],
            dictionary["quantity"],
            dictionary["purchase_price"],
            dictionary["sale_price"],
            dictionary["sales"]
        )

    def __repr__(self):
        """
        Rappresentazione dell'oggetto Product come stringa.

        Returns:
            str: La rappresentazione dell'oggetto Product.
        """
        return (f""
                f"Product(name={self.name}, "
                f"purchase_price={self.purchase_price}, "
                f"sale_price={self.sale_price}, "
                f"quantity={self.quantity}, "
                f"sales={self.sales})")
