import fitz  # PyMuPDF

pdf_path = "Copia_de_SaraEscolhodo.pdf"
saida = "teste_posicoes.pdf"

doc = fitz.open(pdf_path)
page = doc[0]

# Gerar pontos de teste verticais
for y in range(50, 800, 20):
    page.insert_text((50, y), f"(50,{y})", fontsize=8, color=(1, 0, 0))  # vermelho
    page.insert_text((150, y), f"(150,{y})", fontsize=8, color=(0, 1, 0))  # verde
    page.insert_text((250, y), f"(250,{y})", fontsize=8, color=(0, 0, 1))  # azul
    page.insert_text((350, y), f"(350,{y})", fontsize=8, color=(0, 0, 0))  # preto

# Gerar pontos de teste horizontais no topo
for x in range(50, 400, 50):
    page.insert_text((x, 40), f"({x},40)", fontsize=8, color=(0.5, 0.5, 0.5))

doc.save(saida)
doc.close()

print(" Arquivo de teste salvo como teste_posicoes.pdf")