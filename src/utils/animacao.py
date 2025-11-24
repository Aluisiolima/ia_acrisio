from time import sleep
def animacao_show(mensagem):
    """Animação especial para o show"""
    print(f"\n✨ {mensagem}", end="", flush=True)
    for i in range(3):
        for char in "🎉🌟⚡🎯🤖":
            print(char, end="", flush=True)
            sleep(0.1)
        print("\b\b\b\b\b     \b\b\b\b\b", end="", flush=True)
    print(" ✅ PRONTO!")