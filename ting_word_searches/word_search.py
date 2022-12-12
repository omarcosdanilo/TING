# from ting_file_management.file_process import process
# from ting_file_management.queue import Queue


def exists_word(word, instance):
    result = []
    occurrencies_index = []

    for data in instance:
        for index in range(len(data["linhas_do_arquivo"])):
            if word.lower() in data["linhas_do_arquivo"][index].lower():
                occurrencies_index.append(index + 1)

        result.append(
            {
                "palavra": word.lower(),
                "arquivo": data["nome_do_arquivo"],
                "ocorrencias": [
                    {"linha": index} for index in occurrencies_index
                ],
            }
        )

    return result if len(occurrencies_index) > 0 else []


def search_by_word(word, instance):
    """Aqui irá sua implementação"""


# fila = Queue()
# process("statics/arquivo_teste.txt", fila)
# if __name__ == "__main__":
#     exists_word("de", fila)
