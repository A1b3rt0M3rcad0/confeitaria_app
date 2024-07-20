import logging
from config.settings import Config


def init_logger():
    # logger
    logger = logging.getLogger(**Config.logger)
    logger.setLevel(logging.DEBUG)  # Definindo o nível de log

    # Criando um manipulador para escrever logs em um arquivo
    file_handler = logging.FileHandler(filename=Config.logger['name'])

    # Criando um manipulador para exibir logs no console
    console_handler = logging.StreamHandler()
    console_handler.setLevel(logging.DEBUG)  # Todos os logs serão exibidos no console

    # Criando um formatador e adicionando-o aos manipuladores
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    file_handler.setFormatter(formatter)
    console_handler.setFormatter(formatter)

    # Adicionando os manipuladores ao logger
    logger.addHandler(file_handler)
    logger.addHandler(console_handler)
    return logger