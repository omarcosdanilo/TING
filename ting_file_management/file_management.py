import sys


def txt_importer(path_file):
    if ".txt" not in path_file:
        print("Formato inválido", file=sys.stderr)

    try:
        with open(path_file, "r") as file:
            content = file.readlines()

        return [text.strip('\n') for text in content if text != '\n']
    except FileNotFoundError:
        print(f"Arquivo {path_file} não encontrado", file=sys.stderr)
