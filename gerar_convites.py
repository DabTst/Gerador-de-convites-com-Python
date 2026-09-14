import fitz #PyMuPDF
import csv
import os

#caminhos
template_path = "Copia_de_SaraEscolhodo.pdf"
csv_path = "convidados.csv"
output_dir = "convites_gerados"


#criar pasta de saída if not exist
os.makedirs(output_dir, exist_ok = True)

#abrir csv
with open(csv_path, newline='', encoding='utf-8') as csvfile:
    reader = csv.DictReader(csvfile)


    for row in reader:
        nome = row['Nome']
        pessoas = row['NumeroDePessoas']
        mesa = row['Mesa']

        #abrir pdf base
        #Salvo na mesma pasta que os convites

        doc = fitz.open(template_path)
        page = doc[0]

        # Inserir os textos (ajustar coordenadas conforme o PDF)
        page.insert_text((130, 205), nome, fontsize=10, fontname="helv", color=(0, 0, 0))
        page.insert_text((90, 363), f"{pessoas}", fontsize=10, fontname="helv", color=(0, 0, 0))
        page.insert_text((200, 363), f"{mesa}", fontsize=10, fontname="helv", color=(0, 0, 0))

        # Salvar convite com nome do convidado
        safe_name = nome.replace(" ", "_").replace("/", "_")
        output_path = os.path.join(output_dir, f"{safe_name}_convite.pdf")
        doc.save(output_path)
        doc.close()

print('Convites gerados com sucesso')
