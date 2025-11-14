class Product :
    def __init__(self, sku , name , cost_price , selling_price ,  stock_quantity):
        self.sku = sku
        self.name = name
        self.cost_price=cost_price
        self.selling_price = selling_price
        self.margin = self.cost_price - self.selling_price
        self.stock_quantity = stock_quantity
        self._data = {}
    def __repr__(self):
        return f"Product{self.sku} , name : {self.name} ,\n Product cost price : {self.cost_price} , \n Stock quantity : {self.stock_quantity}"
    def __str__(self):
        return f"{self.name} ({self.sku} - Stock : {self.stock_quantity})"
    def __eq__(self, other):
        if not isinstance(other , Product):
            return NotImplemented
        return self.sku == other.sku
    def __gt__(self, other):
        if not isinstance(other, Product):
            return NotImplemented
        return self.margin > other.margin
    def __lt__(self, other):
        if not isinstance(other, Product):
            return NotImplemented
        return self.margin < other.margin
    def __add__(self, other):
        if not isinstance(other, Product):
            return NotImplemented

        if self.sku == other.sku:
            return Product(
                sku=self.sku,
                name=self.name,
                cost_price=self.cost_price,
                selling_price=self.selling_price,
                stock_quantity=self.stock_quantity + other.stock_quantity
            )
        else:
            raise ValueError("Faqat SKU'lari bir xil bo'lgan mahsulotlarni qo'shish mumkin")
    def __getitem__(self, key):
        if key == 'margin' :
            return self.margin
        if key== 'roi' :
            if self.cost_price > 0.0:
                roi = f"{(self.cost_price/self.margin) *100 }% "
                return roi
            else:
                return 0.0
        elif key in self._data:
            return self._data[key]
        else:
            raise KeyError(f"Key '{key}' not found. ")

class SalesOrder:
    def __init__(self , order_id , customer_id):
        self.order_id = order_id
        self.customer_id = customer_id
        self.items = []

    def add_item(self, item):
        self.items.append(item)

    def __len__(self):
        return len(self.items)

    def __contains__(self, item):
        return item in self.items

    def __iadd__(self, other):
        if isinstance(other, SalesOrder):
            self.order_id += other.order_id
            self.customer_id += other.customer_id

        else:
            self.order_id += other
            self.customer_id += other

        return self
    def __bool__(self):
        return len(self.items) > 0