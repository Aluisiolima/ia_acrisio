from time import sleep

def efeito_digitacao_show(texto, velocidade=0.015):
    """Efeito de digitação super estiloso"""
    for char in texto:
        print(char, end='', flush=True)
        sleep(velocidade)
    print()