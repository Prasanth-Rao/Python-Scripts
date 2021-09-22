# Convert Word Document to PDF
# !pip install docx2pdf

from docx2pdf import convert

# converting file in same directory
convert("sampledocx.docx")

# converting file and save in different directory
convert("sampledocx.docx", "path\\to\\output\\directory\\output.pdf")

# Bulk conversion
convert("path\\to\\directory\\containing\\docfiles")
