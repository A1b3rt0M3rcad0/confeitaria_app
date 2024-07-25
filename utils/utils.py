def only_float_number(current_text:str) -> bool:
    # Permitir texto vazio, dígitos e ponto decimal se ele não estiver já presente no texto
    if current_text == "" or current_text.isdigit() or (current_text.count('.') == 1 and current_text.replace('.', '').isdigit()):
        return True
    else:
        return False

def only_int_number(char:str, current_text:str) -> bool:
    # Permitir texto vazio, dígitos e ponto decimal se ele não estiver já presente no texto
    if current_text == "" or current_text.isdigit() or char.isdigit():
        return True
    else:
        return False

def not_start_with_space(char: str, current_text: str) -> bool:
    # Permitir a entrada se o texto estiver vazio e o caractere for um espaço (para permitir o primeiro caractere)
    if current_text == '' and char == ' ':
        return True
    # Permitir a inserção de um espaço se ele não for o primeiro caractere ou se o texto é apenas um espaço
    if char == ' ':
        if len(current_text.lstrip()) > 0:
            return True
        else:
            return False
    return True
