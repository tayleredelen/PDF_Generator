from fpdf import FPDF
import pandas as pd

pdf = FPDF(orientation="P", unit="mm", format="A4")

df = pd.read_csv("topics.csv")

for index, row in df.iterrows():
    pdf.add_page()
    pdf.set_font(family="Times", style="B", size=24)
    pdf.set_text_color(100, 100, 100)
    # makes text gray
    pdf.cell(w=0, h=12, txt=row["Topic"], align="L", ln=1)
    pdf.line(x1=10, y1=21, x2=200, y2=21)
#     x1 value = distance from left border to left edge of pdf in defined unit (mm)
#     y1 value = distance from left border to top of pdf in defined unit (mm)
#     x2 value = distance from right border to right edge of pdf in defined unit (mm)
#     y2 value = distance from right border to top of pdf in defined unit (mm)

    for i in range(row["Pages"] - 1):
        pdf.add_page()
    # range is Python type, resembles lists

pdf.output("topics.pdf")