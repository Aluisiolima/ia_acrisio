from src.ia_acrisio import IA_EPT_CETI
from src.utils import animacao_show, mostrar_banner_show, efeito_digitacao_show, resource_path
from time import sleep
from json import loads


def main():
    json = loads(open(resource_path("data/data.json"), "r", encoding="utf-8").read())
    ia = IA_EPT_CETI(json["dados"], json["quiz_perguntas"], json["perguntas_sugeridas"])
    
    # Banner espetacular
    mostrar_banner_show()
    
    # Animação de inicialização
    animacao_show("INICIANDO SISTEMA DE IA DO CETI")
    
    print(f"\n{'🚀' * 20}")
    print("🎯 SISTEMA PRONTO PARA O SHOW!")
    print(f"{'🚀' * 20}")
    
    # Captura do nome
    print("\n🤔 ANTES DO SHOW, QUAL O SEU NOME?")
    try:
        nome_visitante = input("👤 DIGITE SEU NOME: ").strip()
        if nome_visitante:
            ia.visitante_nome = nome_visitante.title()
            print(f"\n🤖 {ia.nome}: 🎉 EBA! {ia.visitante_nome}, prepare-se para o SHOW!")
    except:
        print("\n🤖 Tudo bem, vamos de anônimo! O show deve continuar!")
    
    # Menu interativo
    print(f"\n{'💡' * 10} MENU DO SHOW {'💡' * 10}")
    print("1. 🎮 Modo Quiz Show (Recomendado!)")
    print("2. 💬 Modo Conversa Livre")
    print("3. 🎯 Modo Apresentação Automática")
    
    try:
        opcao = input("\n🎯 ESCOLHA SUA AVENTURA (1, 2 ou 3): ").strip()
        
        if opcao == "1":
            ia.iniciar_quiz_show()
        elif opcao == "3":
            print("\n🎬 INICIANDO APRESENTAÇÃO AUTOMÁTICA...")
            sleep(2)
            # Apresentação automática simplificada
            perguntas_demo = [
                "Quais as modalidades de ensino?",
                "O que é EPT?",
                "Como funciona o AEE?",
                "Quais cursos técnicos oferecem?"
            ]
            for pergunta in perguntas_demo:
                print(f"\n👤 VISITANTE: {pergunta}")
                sleep(1)
                resposta = ia.processar_pergunta(pergunta)
                print(f"🤖 {ia.nome}: ", end="")
                efeito_digitacao_show(resposta)
                sleep(2)
            print(f"\n{'🎬' * 10} FIM DA DEMONSTRAÇÃO {'🎬' * 10}")
        
        # Loop principal de interação
        saudacao_nome = f", {ia.visitante_nome}" if ia.visitante_nome else ""
        print(f"\n{'🎤' * 20}")
        print(f"🤖 {ia.nome}: 🎉 AGORA{saudacao_nome}, O SHOW É SEU!")
        print("💬 PERGUNTE O QUE QUISER SOBRE O CETI!")
        print("🎮 DIGITE 'QUIZ' PARA UM DESAFIO!")
        print("👋 DIGITE 'SAIR' PARA ENCERRAR")
        print(f"{'🎤' * 20}")
        
        while True:
            try:
                pergunta = input("\n🎤 SUA PERGUNTA: ").strip()
                
                if not pergunta:
                    continue
                
                if pergunta.lower() in ['sair', 'exit', 'fim', 'quit', 'tchau']:
                    break
                
                # Processar pergunta com efeito show
                resposta = ia.processar_pergunta(pergunta)
                print(f"\n{'🤖' * 3} {ia.nome}: ", end="")
                efeito_digitacao_show(resposta)
                
                # Feedback motivacional
                if ia.contador_perguntas % 5 == 0:
                    print(f"\n💫 INCRÍVEL! Já respondemos {ia.contador_perguntas} perguntas!")
                    if ia.visitante_nome:
                        print(f"🎯 {ia.visitante_nome}, você é um(a) perguntador(a) nato(a)!")
                    
            except KeyboardInterrupt:
                print(f"\n\n🤖 {ia.nome}: 🎬 Show interrompido! Obrigado a todos!")
                break
            except Exception as e:
                print(f"\n🤖 {ia.nome}: 💥 Oops! Algo saiu do roteiro! Vamos continuar o show! 😊")
    
    except Exception as e:
        print(e)
        # print(f"\n❌ ERRO: O show encontrou um problema técnico!")
        # print("🔧 Reiniciando os sistemas...")
    
    finally:
        # ✅ CORREÇÃO: Chamar o método CORRETO
        print(f"\n{'🎭' * 20}")
        ia.mostrar_relatorio_show()
        print(f"{'🎭' * 20}")
        
        # Mensagem final emocionante
        if ia.visitante_nome:
            print(f"\n💝 {ia.visitante_nome}, O CETI AGRADECE SUA PRESENÇA!")
        print("🎓 EDUCAR É TRANSFORMAR O MUNDO!")
        print("🚀 ATÉ A PRÓXIMA, FUTURO PROFISSIONAL!")

if __name__ == "__main__":
    main()