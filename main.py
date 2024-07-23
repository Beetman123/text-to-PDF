
import glob
from fpdf import FPDF
from pathlib import Path


# Create a list of text filepaths
filepaths = glob.glob("textFiles/*.txt")

# create the PDF file
pdf = FPDF(orientation="P", unit="mm", format="A4")

# For each file in filepaths list
for filepath in filepaths:
    #df = pd.read_csv(filepath)
    pdf.add_page()

    # Get the filename without the extension
    filename = Path(filepath).stem

    # add the name to the pdf (capitalized)
    pdf.set_font(family="Times", size=24, style="B")
    pdf.cell(w=50, h=8, txt=f"{filename.title()}")

# create pdf
pdf.output("output.pdf")