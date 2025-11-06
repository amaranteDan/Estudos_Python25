import shutil
import os
from datetime import datetime

def gerar_relatorio_html(arquivo="relatorio.html"):
    # Informações de disco
    uso = shutil.disk_usage("/")
    total_gb = uso.total // (1024**3)
    usado_gb = uso.used // (1024**3)
    livre_gb = uso.free // (1024**3)

    # Caminho do Python
    python_path = shutil.which("python3") or "Não encontrado"

    # Tamanho do terminal
    terminal_size = shutil.get_terminal_size()

    # Data/hora do relatório
    agora = datetime.now().strftime("%d/%m/%Y %H:%M:%S")

    # HTML simples
    conteudo = f"""
    <html>
    <head>
        <meta charset="UTF-8">
        <title>Relatório do Sistema</title>
        <style>
            body {{ font-family: Arial, sans-serif; margin: 20px; }}
            h1 {{ color: #2E86C1; }}
            table {{ border-collapse: collapse; width: 50%; }}
            td, th {{ border: 1px solid #ccc; padding: 8px; }}
            th {{ background-color: #f2f2f2; }}
        </style>
    </head>
    <body>
        <h1>📊 Relatório do Sistema</h1>
        <p><b>Gerado em:</b> {agora}</p>
        <table>
            <tr><th>Item</th><th>Valor</th></tr>
            <tr><td>Espaço Total</td><td>{total_gb} GB</td></tr>
            <tr><td>Espaço Usado</td><td>{usado_gb} GB</td></tr>
            <tr><td>Espaço Livre</td><td>{livre_gb} GB</td></tr>
            <tr><td>Python</td><td>{python_path}</td></tr>
            <tr><td>Tamanho do Terminal</td><td>{terminal_size.columns} x {terminal_size.lines}</td></tr>
            <tr><td>Diretório Atual</td><td>{os.getcwd()}</td></tr>
        </table>
    </body>
    </html>
    """

    with open(arquivo, "w", encoding="utf-8") as f:
        f.write(conteudo)

    print(f"✅ Relatório gerado: {arquivo}")

# Executa
if __name__ == "__main__":
    gerar_relatorio_html()
