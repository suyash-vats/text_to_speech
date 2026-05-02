import pyttsx3
import PyPDF2
from tkinter.filedialog import askopenfilename

# here it will select the file if the file is not selected it will exit
book = askopenfilename(title="Select PDF file")

if not book:
    print("No file selected.")
    exit()

try:
    reader = PyPDF2.PdfReader(book)
except Exception as e:
    print("Error opening PDF:", e)
    exit()

pages = len(reader.pages)

engine = pyttsx3.init()

voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)  # here you can change the voice change index if needed
engine.setProperty('rate', 170)

for i in range(pages):
    try:
        page = reader.pages[i]
        text = page.extract_text()

        if text:
            print(f"Reading page {i+1}")
            
            # agar teri file badi hoti to tera code break ho jata so yaha pe file ko samaller chunks kar dega 
            for line in text.split('\n'):
                engine.say(line)
        else:
            print(f"Page {i+1} has no readable text.")

    except Exception as e:
        print(f"Error on page {i+1}:", e)

engine.runAndWait()
