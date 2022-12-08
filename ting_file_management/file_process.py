from ting_file_management.file_management import txt_importer
import sys


def process(path_file, instance):
    for index in range(instance.__len__()):
        if instance.search(index)["nome_do_arquivo"] == path_file:
            return None

    news = txt_importer(path_file)
    nome_do_arquivo = path_file
    quantidade_de_linhas = len(news)

    processed_data = (
        {
            "nome_do_arquivo": nome_do_arquivo,
            "qtd_linhas": quantidade_de_linhas,
            "linhas_do_arquivo": news
        }
    )

    instance.enqueue(processed_data)

    sys.stdout.write(f"{processed_data}")


def remove(instance):
    """Aqui irá sua implementação"""


def file_metadata(instance, position):
    """Aqui irá sua implementação"""
