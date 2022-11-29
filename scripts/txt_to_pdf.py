from fpdf import FPDF

pdf = FPDF()

pdf.add_page()
pdf.add_font('DejaVu', '', '', uni=True)
pdf.set_font('DejaVu', size = 15)

pdf.cell(200, 10, )