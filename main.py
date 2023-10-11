from fpdf import FPDF

pdf = FPDF(orientation="P", unit="mm", format="A4")

pdf.add_page()
# adds pages to document

pdf.set_font(family="Times", style="B", size=12)
# sets font family, style, and size (in points, not mm)

pdf.cell(w=0, h=12, txt="hello", align="L", ln=1, border=1)
pdf.cell(w=0, h=12, txt="hi", align="L", ln=1, border=1)
# adds text thru cells, fields explained:
# width of cell, height of cell
# text inside cell
# alignment of text
# break line (0 is added after width ends)
# border of cell

pdf.add_page()
pdf.set_font(family="Times", style="B", size=12)
pdf.cell(w=0, h=12, txt="goodbye", align="L", ln=1, border=1)
pdf.cell(w=0, h=12, txt="bye", align="L", ln=1, border=1)

pdf.output("output.pdf")