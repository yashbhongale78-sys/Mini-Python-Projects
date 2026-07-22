from PyPDF2 import PdfWriter

merger = PdfWriter()

pdfs = []

n = int(input("enter number  of PDF :"))

for i in range (0,n):

    name = input("Enter name of PDF :")
    
    pdfs.append(name)

for pdf in pdfs:
    merger.append(pdf)

merger.write("merged-pdf.pdf")
merger.close()