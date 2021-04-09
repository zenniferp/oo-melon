"""Classes for melon orders."""

class AbstractMelonOrder():
    def __init__(self, species, qty):
        self.species = species
        self.qty = qty
        self.shipped = False

    def get_total(self):
        """Calculate price, including tax."""
        base_price = 5
        if self.species == "Christmas":
            base_price = base_price * 1.5
        else:
            base_price = 5

        total = (1 + self.tax) * self.qty * base_price
        if order_type == "international" and qty < 10:
            total += 3
        else:
            total = (1 + self.tax) * self.qty * base_price
        return total

    def mark_shipped(self):
        """Record the fact than an order has been shipped."""
        self.shipped = True

class DomesticMelonOrder(AbstractMelonOrder):
    """A melon order within the USA."""
    order_type = "domestic"
    tax = 0.08
    def __init__(self, species, qty):
        super().__init__(species, qty) #setting these attributes by calling the init method from above
        #super().get_total()
        #super().mark_shipped
        """Initialize melon order attributes."""

class InternationalMelonOrder(AbstractMelonOrder):
    """An international (non-US) melon order."""
    order_type = "international"
    tax = 0.17
    
    def __init__(self, species, qty, country_code):
        """Initialize melon order attributes."""
        super().__init__(species, qty)
        #super().get_total()
        #super().mark_shipped()
        self.country_code = country_code

    def get_country_code(self):
        """Return the country code."""

        return self.country_code
