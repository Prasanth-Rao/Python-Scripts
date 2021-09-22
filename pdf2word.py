import win32com.client

word = win32com.client.Dispatch("Word.Application")
word.visible = 0

pdfDoc = "D:\\YouTube\\TestingCodes\\samplepdf.pdf"
wordDoc = "D:\\YouTube\\TestingCodes\\NewDoc.docx"

wordObj = word.Documents.Open(pdfDoc)
wordObj.SaveAs(wordObj, FileFormat=16) # file format for docx

wordObj.Close()
word.Quit()