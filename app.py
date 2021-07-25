
from reportlab.pdfgen import canvas
from PyPDF2 import PdfFileWriter, PdfFileReader
import streamlit as st



st.title('app')
selected_file='a.pdf'
my_pdf=canvas.Canvas('temp.pdf')


existing_pdf = PdfFileReader(open(f"{selected_file}", "rb"))

page_list=[]
for i in range(existing_pdf.numPages):
	page = existing_pdf.getPage(i)

	page_list.append(page)


for i in range(existing_pdf.numPages):
	my_pdf.setFillColor('#FF0000')


	my_pdf.drawCentredString(200,800,'PAGE NUMBER '+str(my_pdf.getPageNumber()))
	my_pdf.showPage()
my_pdf.save()
water_pdf = PdfFileReader(open("temp.pdf", "rb"))
output = PdfFileWriter()
for i in range(existing_pdf.numPages):
	page_list[i].mergePage(water_pdf.getPage(i))
	output.addPage(page_list[i])


outputStream = open("water_marked.pdf", "wb")
output.write(outputStream)
outputStream.close()
