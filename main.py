import pyttsx3
import PyPDF2

# get book source
book = open('twenty-thousand-leagues-under-the-sea.pdf', 'rb')

# read the book
pdfReader = PyPDF2.PdfFileReader(book)

# get the page numbers
pages = pdfReader.numPages
# print(pages)

# init speech to text
speaker = pyttsx3.init()
# loop through pages
for num in range(3, pages):
    # select start page no
    page = pdfReader.getPage(3)

    # extract the text form pdf
    text = page.extractText()

    # Speak the text
    speaker.say(text)

    # run speaker
    speaker.runAndWait()