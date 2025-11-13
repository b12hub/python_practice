import os
from abc import ABC, abstractmethod
from reportlab.pdfgen import canvas
from openpyxl import Workbook
OUTPUT_DIR = "invoices"
if not os.path.exists(OUTPUT_DIR):
    os.makedirs(OUTPUT_DIR)
class InvoiceGenerator(ABC):
    def __init__(self, client_name, items):
        self.client_name = client_name
        self.items = items
    @abstractmethod
    def calculate_total(self):
        pass
    @abstractmethod
    def generate_invoice(self):
        pass

class PDFInvoiceGenerator(InvoiceGenerator):
    def __init__(self, client_name, items):
        super().__init__(client_name, items)
    def calculate_total(self):
        return sum(self.items.values())

    def generate_invoice(self):
        file_path = os.path.join(OUTPUT_DIR, "invoice.pdf")
        pdf_file = canvas.Canvas(file_path)
        pdf_file.drawString(100, 750, f"Client: {self.client_name}")
        y = 700
        for item, price in self.items.items():
            pdf_file.drawString(100, y, f"{item}: ${price}")
            y -= 20
        pdf_file.drawString(100, y-20, f"Total: ${self.calculate_total()}")
        pdf_file.save()
        return file_path

class ExcelInvoiceGenerator(InvoiceGenerator):
    def __init__(self, client_name, items):
        super().__init__(client_name, items)

    def calculate_total(self):
        return sum(self.items.values())

    def generate_invoice(self):
        file_path = os.path.join(OUTPUT_DIR, "Invoice.xlsx")
        wb = Workbook()
        ws = wb.active
        ws.title = "Invoice"
        ws.append(["Item", "Price", "Client Name"])
        for item, price in self.items.items():
            ws.append([item, price, self.client_name])
        ws.append(["Total", self.calculate_total(), self.client_name])
        wb.save(file_path)
        return file_path


class HTMLInvoiceGenerator(InvoiceGenerator):
    def __init__(self, client_name, items):
        super().__init__(client_name, items)

    def calculate_total(self):
        return sum(self.items.values())

    def generate_invoice(self):
        file_path = os.path.join(OUTPUT_DIR, "invoice.html")
        html_content = f"<h1>Invoice for {self.client_name}</h1><table>"
        for item, price in self.items.items():
            html_content += f"<tr><td>{item}</td><td>{price}</td></tr>"
        html_content += f"<tr><td>Total</td><td>{self.calculate_total()}</td></tr></table>"
        with open(file_path, "w") as f:
            f.write(html_content)
        return file_path

class InvoiceManager():
    def __init__(self):
        self.invoice_generators = []

    def add_generator(self, generator: InvoiceGenerator):
        self.invoice_generators.append(generator)

    def export_invoice(self):
        for generator in self.invoice_generators:
            generator.generate_invoice()