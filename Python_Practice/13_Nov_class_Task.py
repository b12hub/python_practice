from abc import ABC, abstractmethod
from reportlab.pdfgen import canvas
from openpyxl import Workbook
import html
class InvoiceGenerator (ABC):
    @abstractmethod
    def __init__(self,client_name,items):
        self.client_name = client_name
        self.items = items
        pass
    def calculate_total(self):
        pass
    def generate_invoice(self):
        pass
class PDFInvoiceGenerator(InvoiceGenerator):
    def __init__(self,client_name , items):
        super().__init__(client_name , items)
    def calculate_total(self):
       pass

    def generate_invoice(self):
        pdf_file = canvas.Canvas("invoice.pdf")
        pdf_file.drawString(100,750 , self.items)
        pdf_file.drawString(100,700 , self.client_name)
        pdf_file.save()
        print("PDF - Invoice generated successfully , invoice.pdf")


class ExcelInvoiceGenerator(InvoiceGenerator):
    def __init__(self,client_name , items):
        super().__init__(client_name , items)
    def calculate_total(self):
        pass

    def generate_invoice(self):
        exl_file = Workbook()
        exl_file = exl_file.active
        exl_file.title = "Invoice"
        exl_file.append(["Items" , "Client Name"])
        headers = list(self.items.keys())
        for col_num , headrers in enumerate(headers,1):
            exl_file.cell(row=1,column=col_num,value=headers)
        exl_file.append([self.items.values() , self.client_name])
        exl_file.save("Invoice.xlsx")
        print("Excel - Invoice generated successfully , Invoice.xlsx")


class HTMLInvoiceGenerator(InvoiceGenerator):
    def __init__(self,client_name , items):
        super().__init__(client_name , items)
    def calculate_total(self):
        pass
    def generate_invoice(self):
        html_file = open("invoice.html","w")
        html_file.write(f"<h1>Invoice for {self.client_name}</h1>")
        html_file.write("<table>")
        for item in self.items:
            html_file.write(f"<tr><td>{item}</td><td>{self.items[item]}</td></tr>")
            html_file.write("</table>")
            html_file.close()

        html_file = open("invoice.html","r")
        html_content = html_file.read()
        html_file.close()
        print("HTML - Invoice generated successfully , invoice.html")

class InvoiceManager():
    def __init__(self):
        self.invoice_generators = []
        pass
    def export_invoice(self):
        self.generator_invoice()
        pass