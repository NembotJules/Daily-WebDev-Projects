import pyttsx3, PyPDF2

pdf = PyPDF2.PdfReader(open("COURS D'INVESTIGATION NUMERIQUE PARTIE 1.pdf", 'rb'))
speaker = pyttsx3.init()

for page in range(len(pdf.pages)):
    text = pdf.pages[page].extract_text()
    clean_text = text.strip().replace('\n', ' ')
    print(clean_text)

speaker.save_to_file(clean_text, 'read.mp3')
speaker.runAndWait()

speaker.stop()