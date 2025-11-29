import sys
import os

def resource_path(relative_path):
    """ Retorna o caminho correto do arquivo tanto no EXE quanto no código fonte """
    if getattr(sys, 'frozen', False):
        # Quando está congelado (cx_Freeze)
        base_path = sys._MEIPASS if hasattr(sys, '_MEIPASS') else os.path.dirname(sys.executable)
    else:
        # Quando está rodando no Python normal
        base_path = os.path.dirname(__file__)

    return os.path.join(base_path, relative_path)