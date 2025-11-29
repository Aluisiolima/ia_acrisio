from cx_Freeze import setup, Executable

setup(
    name="Ia Acrisio",
    version="1.0",
    description="Uma IA esperimental criada pelo alunos do 1º Ano Desenvolvimento de Sistema CETI Acriso Veras",
    options={
        "build_exe": {
            "include_files": [
                ("data/", "data/")   # (origem, destino)
            ]
        }
    },
    executables=[Executable("main.py")]  # arquivo principal
)
