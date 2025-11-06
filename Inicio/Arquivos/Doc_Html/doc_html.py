'''
O objetivo desse exercicio é criar um arquivo HTML simples usando Python. O arquivo HTML conterá uma estrutura básica com título, cabeçalho e parágrafo.
'''

with open("index.html", "w", encoding="utf-8") as pagina:
    pagina.write("<!DOCTYPE html>\n ")
    pagina.write("<html lang='pt-br'>\n")
    pagina.write("<head>\n")
    pagina.write("<meta charset='UTF-8'>\n")
    
    pagina.write("<title>Minha Primeira Página HTML com Python</title>\n")
    pagina.write("</head>\n")
    pagina.write("<body>\n")
    pagina.write("<h1>Olá, Mundo!</h1>\n")
    pagina.write("<p>Esta é minha primeira página HTML gerada com Python.</p>\n")
    for linha in range(10):
        pagina.write(f"    <p>Esta é a linha número {linha}.</p>\n")
    pagina.write("</body>\n")
    pagina.write("</html>\n")    