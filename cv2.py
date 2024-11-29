from fpdf import FPDF
from PIL import Image

title = "Paweł Strepikowski"

pdf = FPDF('P', 'mm', (210, 297))

pdf.add_font('Inter', '', 'C:/Users/pawko/OneDrive/Pulpit/python/Main/cv/Inter-Italic-VariableFont_opsz,wght.ttf', uni=True)   
pdf.set_font('Inter', '', 20)

kwadrat = Image.new('RGB', (50,50), (48, 110, 125) )
poziom = Image.new('RGB', (200, 50), (229, 250, 250))
Pion = Image.new('RGB', (50, 250), (126, 180, 196))
background = Image.new('RGB', (20, 250), (255, 255, 255))
kwadrat.save('kwadrat.png')
poziom.save('poziom.png')
Pion.save('Pion.png')
background.save('background.png')


pdf.add_page()
pdf.image('background.png', x = 0, y = 0, w = 210, h = 297, type = '', link = '')
pdf.image('Pion.png', x = 0, y = 0, w = 55, h = 297, type = '', link = '')
pdf.image('Poziom.png', x = 0, y =0, w =210, h = 55, type = '', link = '')
pdf.image('kwadrat.png', x = 0, y = 0, w =55, h = 55, type = '', link = '')
pdf.ln(15)
pdf.cell(15, 40, border=False)
pdf.cell(30,40, border=False)

def name(title, margin):
    pdf.set_font('Inter', '', size=12)
    pdf.set_text_color(255, 255, 255)
    pdf.cell(w = 60, h = 10, text =margin, border=False)
    pdf.set_text_color(255, 255, 255)
    pdf.set_font(size =  12)
    pdf.set_fill_color(14,73,101)
    pdf.cell(35, 10, title, align='C', fill=True, border=False)
    pdf.ln(10) 

def akapit( main, margin2):
    pdf.set_text_color(0, 0, 0)
    pdf.set_font('Inter', '', 7)
    pdf.cell(60, 10, text = margin2, border=False)
    pdf.set_font('Inter', '', 10)
    pdf.cell(130, 10, text = main, border=False)
    pdf.ln(5)


pdf.set_text_color(0, 0, 0)
pdf.cell(70, 10, text='Paweł', border = False, ln = 1, center=True)
pdf.cell(70, 10, text='Strepikowski', border = False, ln = 1, center=True)
pdf.ln(20)

title = "Wykształcenie"
main = "~ Fizyka Techniczna studia I stopnia"
margin1 = 'Dane:'
margin2 = "telefon: 513 794 124"
name( title, margin1)
akapit( main, margin2 )
main = "Politechnika Warszawska Wydział Fizyki (2023-obecnie)"
margin2 = "email: pawel.strepikowski@wp.pl"
akapit( main, margin2)
main=""
margin2=""
akapit( main, margin2)
akapit( main, margin2)
akapit( main, margin2)
akapit( main, margin2)
title = "Doświadczenie"
margin1 = "Umiejętności:"
name(title, margin1)
main = "~ Praktyki w Instytucie Niskich Temperatur i Wysokich ciśnień, o temacie:"
margin2 = "python: średnio zaawansowany"
akapit(main, margin2)
main = ",,Własności cieplne materiałów półprezwodnikowych''"
margin2 = "konsola: podstawy"
akapit(main, margin2)
margin2 = "C: podstawy"
main = ''
akapit(main, margin2)
margin2 = "j. angielski: B2"
main = ''
akapit(main, margin2)

main=""
margin2=""
akapit( main, margin2)
akapit( main, margin2)
margin1 = ""

title = "Mini projekty"
name(title, margin1)
main = "~ Tapeta serce wykonana w matplotlibie"
akapit( main, margin2)
margin2 = ""
main = "~ Programy szkoleniowe wykonane podczas praktyk"
margin2 = ""
akapit( main, margin2)
main = "~ Program analizujący dane pomiarowe wykonany podczas praktyk"
akapit( main, margin2)
main = "~ Program rozpoznający liczby używający tenserflow"
akapit( main, margin2)
main = "~ Program generujący cv jako pdf"
akapit( main, margin2)
main = "~ Program generujący obrazek szachownicy"
akapit( main, margin2)

pdf.set_text_color(0, 0, 0)
pdf.set_font('Inter', '', 7)
pdf.cell(60, 10, text = margin2, border=False)
pdf.set_font('Inter', '', 10)
pdf.cell(52, 10, text = "Programy dostępne na github: ", border=False)
pdf.cell(30, 10, text="https://github.com/Tobos33/My-programs.git", link="https://github.com/Tobos33/My-programs.git")
pdf.ln(5)




pdf.output('pdfcv.pdf')