import pandas as pd
from reportlab.lib.pagesizes import A4
from reportlab.lib import colors
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle, Paragraph, Spacer
from reportlab.lib.styles import getSampleStyleSheet
import webbrowser
import os

# --- Read Student Data ---
# Use the existing DataFrame 'df' instead of reading the CSV again
data = df.copy()

# --- Analyze Data ---
total_students = len(data)
average_marks = data['Marks'].mean()
max_marks = data['Marks'].max()
min_marks = data['Marks'].min()

# --- PDF Generation ---
pdf_filename = "studentrecordcollege_Report.pdf"
doc = SimpleDocTemplate(pdf_filename, pagesize=A4)
elements = []
styles = getSampleStyleSheet()

# --- Title ---
title = Paragraph("📘 <b>Student Report</b>", styles['Title'])
elements.append(title)
elements.append(Spacer(1, 12))

# --- Table Data ---
table_data = [list(data.columns)] + data.values.tolist()
table = Table(table_data, repeatRows=1, hAlign='LEFT')

# --- Table Styling ---
table.setStyle(TableStyle([
    ('BACKGROUND', (0, 0), (-1, 0), colors.darkblue),
    ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
    ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
    ('GRID', (0, 0), (-1, -1), 0.5, colors.black),
    ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
    ('FONTSIZE', (0, 0), (-1, -1), 9),
    ('BACKGROUND', (0, 1), (-1, -1), colors.beige),
]))
elements.append(table)
elements.append(Spacer(1, 20))

# --- Summary Section ---
summary = f"""
<b>Summary:</b><br/>
Total Students: {total_students} <br/>
Average Marks: {average_marks:.2f} <br/>
Maximum Marks: {max_marks} <br/>
Minimum Marks: {min_marks} <br/>
"""
elements.append(Paragraph(summary, styles['Normal']))

# --- Build PDF ---
doc.build(elements)
print(f"✅ Report generated successfully: {pdf_filename}")

# --- Open PDF Automatically ---
# This part might not work directly in Colab, but the file will be generated.
# webbrowser.open_new_tab(os.path.abspath(pdf_filename))