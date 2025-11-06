'''
Essa é uma pagina web gerada a partir de um dicionario em Python.

'''

filmes = {
    "drama": ["O Poderoso Chefão", "Um Sonho de Liberdade", "Forrest Gump"],
    "comedia": ["Se Beber, Não Case!", "Superbad - É Hoje", "A Vida é Bela"],
    "acao": ["Mad Max: Estrada da Fúria", "Gladiador", "John Wick"],
    "ficcao": ["Inception", "Matrix", "Interstellar"],
    "policial": ["Dia de Treinamento", "Clube da Luta", "Os Infiltrados"],
    "guerra": ["O Resgate do Soldado Ryan", "Dunkirk", "Corações de Ferro"]
}

with open("filmes.html", "w", encoding="utf-8") as pagina:
    pagina.write("""
                 <!DOCTYPE html>
                 <html lang='pt-br'>
                 <head>
                 <meta charset='UTF-8'>
                    <title>Lista de Filmes por Gênero</title>
                    </head>
                    <body>
                    <h1>Lista de Filmes por Gênero</h1>
                 """)
    for c, v in filmes.items():
        pagina.write(f"<h2>{c.capitalize()}</h2>\n")
        pagina.write("<ul>\n")
        for e in v:
            pagina.write(f"    <li>{e}</li>\n")
        pagina.write("</ul>\n")
    pagina.write("""
                    </body>
                    </html>
                 """)