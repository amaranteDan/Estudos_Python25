import os
os.chdir('..')  # Move up one directory level
print(f"Diretorio atual: {os.getcwd()}") 

os.mkdir('novo_diretorio')  # Create a new directory
os.chdir('novo_diretorio')  # Change into the new directory
print(f"Diretorio atual:{os.getcwd()}")

os.makdirs("avo/pai/filho", exist_ok=True)  # Create nested directories

# Função rename
os.makedirs("novo_diretorio", exist_ok=True)
os.rename('novo_diretorio', 'diretorio_renomeado') # Renomeando diretorios

# Cria um diretorio e fecha imediatamente

open("arquivo_teste.txt", "w").close()  # Create an empty file
os.remove("arquivo_teste.txt")  # Remove the file

print(f"Listando diretorios{os.listdir(".")}")

os.path

for a in os.listdir("."):
    if os.path.isdir(a):
        print(f"{a} é um diretorio")
    elif os.path.isfile(a):
        print(a)              

# Verifica se o diretorio existe
if os.path.exists("diretorio_renomeado"):
    print("O diretorio existe")
else:
    print("O diretorio nao existe")
    
# Verificando o caminho absoluto
caminho_absoluto = os.path.abspath("diretorio_renomeado")
print(f"Caminho absoluto: {caminho_absoluto}").abspath('.')  # Get absolute path of current directory
        