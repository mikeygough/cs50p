from fpdf import FPDF
from fpdf.enums import XPos, YPos

# instantiate pdf
pdf = FPDF(orientation='portrait', format='A4')
pdf.set_margin(0)
pdf.add_page()

# add text
pdf.set_font('helvetica', size=48)
pdf.cell(w=pdf.epw, h=90, txt='CS50 Shirtificate', align='C')


# add image
imgWidth = (pdf.epw * 0.8)
imgXpos = (pdf.epw - imgWidth) / 2.0
imgYpos = 95
pdf.image('shirtificate.png', w=imgWidth, x=imgXpos, y=imgYpos)

# add user text
userText = input("Name: ")

# set font & color
pdf.set_font('helvetica', size=24)
pdf.set_text_color(255, 255, 255)

# set position
pdf.set_y(150)
pdf.cell(w=pdf.epw, txt = f'{userText} Took CS50', align='C')

# save
pdf.output("shirtificate.pdf")