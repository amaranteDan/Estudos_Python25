Top! 😎 Vou montar um **cheatsheet do `shutil`** bem organizado, com funções principais, descrição e exemplo rápido de uso.

---

# 📑 Cheatsheet do módulo `shutil` (Python)

## 🔧 Arquivos

| Função                      | Descrição                                        | Exemplo                                  |
| --------------------------- | ------------------------------------------------ | ---------------------------------------- |
| `shutil.copy(src, dst)`     | Copia arquivo preservando permissões básicas     | `shutil.copy("a.txt", "backup/a.txt")`   |
| `shutil.copy2(src, dst)`    | Copia arquivo com **metadados completos**        | `shutil.copy2("a.txt", "backup/a.txt")`  |
| `shutil.copyfile(src, dst)` | Copia apenas conteúdo (sem permissões/metadados) | `shutil.copyfile("a.txt", "b.txt")`      |
| `shutil.move(src, dst)`     | Move ou renomeia arquivo/diretório               | `shutil.move("a.txt", "arquivos/a.txt")` |

---

## 📂 Diretórios

| Função                                     | Descrição                              | Exemplo                                                                 |
| ------------------------------------------ | -------------------------------------- | ----------------------------------------------------------------------- |
| `shutil.copytree(src, dst)`                | Copia diretório inteiro recursivamente | `shutil.copytree("projeto", "backup_projeto")`                          |
| `shutil.rmtree(path)`                      | Apaga diretório com todo o conteúdo    | `shutil.rmtree("backup_projeto")`                                       |
| `shutil.ignore_patterns("*.pyc", "*.tmp")` | Ignora arquivos na cópia de diretório  | `shutil.copytree("src", "dst", ignore=shutil.ignore_patterns("*.pyc"))` |

---

## 📦 Arquivos compactados

| Função                                     | Descrição                       | Exemplo                                                          |
| ------------------------------------------ | ------------------------------- | ---------------------------------------------------------------- |
| `shutil.make_archive(base, format, root)`  | Cria `.zip`/`.tar` de uma pasta | `shutil.make_archive("meu_backup", "zip", "/home/user/projeto")` |
| `shutil.unpack_archive(file, extract_dir)` | Extrai `.zip`/`.tar`            | `shutil.unpack_archive("meu_backup.zip", "restaurado")`          |

---

## 💽 Disco e sistema

| Função                            | Descrição                                     | Exemplo                                |
| --------------------------------- | --------------------------------------------- | -------------------------------------- |
| `shutil.disk_usage(path)`         | Mostra espaço em disco (total, usado, livre)  | `print(shutil.disk_usage("/"))`        |
| `shutil.which(cmd)`               | Acha caminho de um executável no sistema      | `print(shutil.which("python3"))`       |
| `shutil.chown(path, user, group)` | Muda dono/grupo de arquivo (Unix/Linux)       | `shutil.chown("a.txt", user="daniel")` |
| `shutil.get_terminal_size()`      | Retorna tamanho do terminal (colunas, linhas) | `print(shutil.get_terminal_size())`    |

---

📌 **Resumo prático:**

* `copy*` → copiar arquivos.
* `copytree / rmtree` → copiar/apagar diretórios inteiros.
* `make_archive / unpack_archive` → criar/extrair compactados.
* `disk_usage / which / chown` → utilitários do sistema.

---

👉 Quer que eu monte um **script exemplo** que use **quase todas essas funções juntas** (tipo um mini gerenciador de arquivos com Python)?
