import pyttsx3
import PyPDF2
from tkinter.filedialog import askopenfilename
book = askopenfilename()
reader = PyPDF2.PdfReader(book)
pages = len(reader.pages)
player = pyttsx3.init() 
for i in range(pages):
    page = reader.pages[i]
    text = page.extract_text()
    player.say(text)
player.runAndWait()