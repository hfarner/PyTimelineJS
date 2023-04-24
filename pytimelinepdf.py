import pdfkit
import os
import platform


# Chemin d'accès de la page HTML que vous souhaitez convertir en PDF
html_file_path = './web-exemple.html'

# Chemin d'accès pour le fichier PDF de sortie
pdf_file_path = './web-exemple.pdf'

# Options pour le format de la page et le zoom du HTML
options = {
    'page-size': 'A4',
    'orientation': 'Landscape',
    'margin-top': '0.75in',
    'margin-right': '0.75in',
    'margin-bottom': '0.75in',
    'margin-left': '0.75in',
    'zoom': '1.5'
}

# Convertir la page HTML en PDF avec les options spécifiées
pdfkit.from_file(html_file_path, pdf_file_path, options=options)
