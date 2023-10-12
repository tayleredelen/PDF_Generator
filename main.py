from fpdf import FPDF
import pandas as pd

pdf = FPDF(orientation="P", unit="mm", format="A4")
pdf.set_auto_page_break(auto=False, margin=0)
# pages aren't broken automatically

df = pd.read_csv("topics.csv")

for index, row in df.iterrows():
    pdf.add_page()
    # sets header
    pdf.set_font(family="Times", style="B", size=24)
    pdf.set_text_color(100, 100, 100)
    # makes text gray
    pdf.cell(w=0, h=12, txt=row["Topic"], align="L", ln=1)
    pdf.line(x1=10, y1=21, x2=200, y2=21)
#     x1 value = distance from left border to left edge of pdf in defined unit (mm)
#     y1 value = distance from left border to top of pdf in defined unit (mm)
#     x2 value = distance from right border to right edge of pdf in defined unit (mm)
#     y2 value = distance from right border to top of pdf in defined unit (mm)

    # sets footer
    pdf.ln(265)
    # paramater is height in selected unit (mm) places text at bottom of page
    pdf.set_font(family="Times", style="I", size=8)
    pdf.set_text_color(180, 180, 180)
    pdf.cell(w=0, h=10, txt=row["Topic"], align="R")

    for i in range(row["Pages"] - 1):
        # -1 since page added above for topic
        # range is Python type, resembles lists
        pdf.add_page()

        # sets footer
        pdf.ln(277)
        pdf.set_font(family="Times", style="I", size=8)
        pdf.set_text_color(180, 180, 180)
        pdf.cell(w=0, h=10, txt=row["Topic"], align="R")

pdf.output("topics.pdf")