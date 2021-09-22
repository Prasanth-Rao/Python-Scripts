# Convert Word Document to PDF
# !pip install pypiwin32  (this is a pre installed library if not found install it)

import win32com.client

# Access MS Word application to read the file
word = win32com.client.Dispatch("Word.Application")
word.visible = 0

# File Paths
pdfDoc = "path\\to\\pdf\\samplepdf.pdf"
wordDoc = "path\\to\\word\\NewDoc.docx"

# open pdf file and write it in word document
wordObj = word.Documents.Open(pdfDoc)
wordObj.SaveAs(wordObj, FileFormat=16) # file format for docx

# for more file formats refer the link "https://docs.microsoft.com/en-us/office/vba/api/word.wdsaveformat"

wordObj.Close()
word.Quit()
