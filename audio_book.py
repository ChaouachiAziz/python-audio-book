import pyttsx3
import PyPDF2
engine = pyttsx3.init()
book = open('eg.pdf', 'rb')
pdfReader = PyPDF2.PdfFileReader(book)
pages = pdfReader.numPages
for i in range(pages):
    engine.say(pdfReader.getPage(i).extractText())
    engine.runAndWait()