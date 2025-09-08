import PyPDF2

def parse_pdf (caminho_pdf):
    try:
        with open(caminho_pdf, 'rb') as file:
            reader = PyPDF2.PdfFileReader(file)
            text = ' '
            for page in reader.pages:
                text+=page.extractText() + '\n'
        return text
    except: Exception as e:
        print(f"Erro no parse do pdf": {e}")
    return ""
