import random
import time
from datetime import datetime

class IA_EPT_CETI:
    def __init__(self, dados_ept: dict, quiz_perguntas: list[dict], perguntas_sugeridas: list[str]):
        self.nome = "IA EDUCACIONAL - CETI Acrísio Veras"
        self.versao = "Dia D EPT 2025 - Versão Show! 🎉"
        self.evento = "Dia D da Educação Profissional e Tecnológica"
        self.historico = []
        self.contador_perguntas = 0
        self.modo_apresentacao = False
        self.visitante_nome = None
        self.pontuacao_quiz = 0
        self.quiz_ativo = False
        self.pergunta_atual_quiz = 0

        self.dados_ept = dados_ept
        self.quiz_perguntas = quiz_perguntas
        self.perguntas_sugeridas = perguntas_sugeridas

    # 🎮 SISTEMA DE QUIZ SHOW
    def iniciar_quiz_show(self):
        """Inicia o quiz de forma espetacular"""
        self.quiz_ativo = True
        self.pontuacao_quiz = 0
        self.pergunta_atual_quiz = 0
        
        saudacao = f", {self.visitante_nome}" if self.visitante_nome else ""
        
        print(f"\n{'🎯' * 20}")
        print(f"🚀 BEM-VINDO{saudacao} AO QUIZ SHOW DO CETI! 🚀")
        print(f"{'🎯' * 20}")
        print("📝 Responda as perguntas e mostre que você é expert!")
        print("💡 Digite A, B, C ou D para responder")
        print("🏆 Ganhe pontos e suba no ranking!")
        print(f"{'🎯' * 20}")
        
        time.sleep(1)
        self.proxima_pergunta_quiz()

    def proxima_pergunta_quiz(self):
        """Apresenta a próxima pergunta com estilo"""
        if self.pergunta_atual_quiz < len(self.quiz_perguntas):
            pergunta_data = self.quiz_perguntas[self.pergunta_atual_quiz]
            
            print(f"\n{'📝' * 10}")
            print(f"❓ PERGUNTA {self.pergunta_atual_quiz + 1}/{len(self.quiz_perguntas)}:")
            print(f"   {pergunta_data['pergunta']}")
            print(f"{'📝' * 10}")
            
            for opcao in pergunta_data['opcoes']:
                print(f"   {opcao}")
            
            print(f"{'🎯' * 10}")
            return True
        else:
            self.finalizar_quiz_show()
            return False

    def verificar_resposta_quiz(self, resposta):
        """Verifica a resposta com feedback animado"""
        if not self.quiz_ativo:
            return "❌ Nenhum quiz ativo. Digite 'quiz' para começar a diversão! 🎮"
        
        pergunta_data = self.quiz_perguntas[self.pergunta_atual_quiz]
        resposta = resposta.upper().strip()
        
        if resposta in ['A', 'B', 'C', 'D']:
            if resposta == pergunta_data['resposta']:
                self.pontuacao_quiz += 2  # Bonus por acerto!
                resultado = f"🎉 🎊 🥳 ACERTOU! {pergunta_data['explicacao']}"
                # Efeito especial para acerto
                print("✨ ", end="")
                for _ in range(3):
                    print("⭐", end="", flush=True)
                    time.sleep(0.3)
                print(" ✨")
            else:
                resultado = f"❌ OPA! A resposta correta era {pergunta_data['resposta']}.\n💡 {pergunta_data['explicacao']}"
            
            self.pergunta_atual_quiz += 1
            
            if self.pergunta_atual_quiz < len(self.quiz_perguntas):
                resultado += f"\n\n📊 Pontuação atual: {self.pontuacao_quiz} pontos"
                resultado += f"\n🎯 Próxima pergunta chegando..."
                time.sleep(1)
                self.proxima_pergunta_quiz()
            else:
                self.finalizar_quiz_show()
            
            return resultado
        else:
            return "❌ Digite A, B, C ou D para responder! 🎯"

    def finalizar_quiz_show(self):
        """Final espetacular do quiz"""
        self.quiz_ativo = False
        total_perguntas = len(self.quiz_perguntas)
        percentual = (self.pontuacao_quiz / (total_perguntas * 2)) * 100
        
        print(f"\n{'🎊' * 15}")
        print("🏆 🏆 🏆 QUIZ CONCLUÍDO! 🏆 🏆 🏆")
        print(f"{'🎊' * 15}")
        
        time.sleep(1)
        print(f"📊 PONTUAÇÃO FINAL: {self.pontuacao_quiz}/{(total_perguntas * 2)}")
        print(f"📈 DESEMPENHO: {percentual:.1f}%")
        
        # Sistema de ranking
        if percentual == 100:
            print("🎖️  RANK: LENDA DO CETI! 🥇")
            print("💫 Você é praticamente um professor da casa!")
        elif percentual >= 80:
            print("🎖️  RANK: EXPERT DO CETI! 🥈")
            print("👏 Conhece nossa escola como a palma da mão!")
        elif percentual >= 60:
            print("🎖️  RANK: CONHECEDOR! 🥉")
            print("👍 Sabe bastante sobre nós!")
        else:
            print("🎖️  RANK: INICIANTE!")
            print("📚 Continue aprendendo sobre nossa escola!")
        
        print(f"{'🎯' * 15}")
        
        if self.visitante_nome:
            print(f"\n👋 {self.visitante_nome}, foi incrível jogar com você!")
            print("🔄 Digite 'quiz' para uma revanche!")

    # 🎯 FUNÇÃO PRINCIPAL SUPER PODEROSA
    def processar_pergunta(self, pergunta):
        self.contador_perguntas += 1
        pergunta_original = pergunta
        pergunta = pergunta.lower().strip()
        
        # Registrar no histórico
        self.historico.append({
            'timestamp': datetime.now().strftime("%H:%M:%S"),
            'pergunta': pergunta_original,
            'numero': self.contador_perguntas
        })
        
        # 🎮 COMANDOS ESPECIAIS DO SHOW
        if pergunta == 'quiz' and not self.quiz_ativo:
            self.iniciar_quiz_show()
            return "🎮 Quiz show iniciado! Responda a pergunta acima! 🚀"
        
        if self.quiz_ativo and pergunta in ['a', 'b', 'c', 'd', 'A', 'B', 'C', 'D']:
            return self.verificar_resposta_quiz(pergunta)
        
        if pergunta in ['pontuacao', 'score', 'placar', 'pontos']:
            if self.quiz_ativo:
                return f"📊 Pontuação atual: {self.pontuacao_quiz} pontos"
            else:
                return "🎯 Nenhum quiz ativo. Digite 'quiz' para começar!"
        
        if pergunta in ['ajuda', 'help', 'comandos']:
            return self.mostrar_ajuda_show()
        
        # 👤 CAPTURAR NOME DO VISITANTE
        nome_capturado = self.capturar_nome_visitante(pergunta)
        if nome_capturado:
            return nome_capturado
        
        # 👋 SAUDAÇÕES PERSONALIZADAS
        if any(palavra in pergunta for palavra in ['oi', 'olá', 'ola', 'bom dia', 'boa tarde', 'boa noite', 'e aí', 'hey', 'opa']):
            return self.saudacao_personalizada_show()
        
        # 👋 DESPEDIDAS PERSONALIZADAS
        if any(palavra in pergunta for palavra in ['tchau', 'obrigado', 'obrigada', 'sair', 'adeus', 'até logo', 'flw', 'valeu']):
            return self.despedida_personalizada_show()
        
        # 🎓 MODALIDADES DE ENSINO
        if any(palavra in pergunta for palavra in ['modalidade', 'modalidades', 'tipos de ensino', 'ensinos', 'o que oferecem']):
            return f"🎓 {self.dados_ept['modalidades_ensino']}"
        
        if any(palavra in pergunta for palavra in ['ensino médio', 'ensino medio', 'regular', 'médio regular', 'medio regular']):
            return f"📚 {self.dados_ept['ensino_medio_regular']}"
        
        if any(palavra in pergunta for palavra in ['aee', 'atendimento educacional', 'especializado', 'inclusão', 'inclusao', 'deficiência', 'deficiencia']):
            return f"♿ {self.dados_ept['aee']}"
        
        if any(palavra in pergunta for palavra in ['ept', 'educação profissional', 'educacao profissional']):
            return f"💼 {self.dados_ept['ept']}"
        
        # 💻 CURSOS TÉCNICOS
        if any(palavra in pergunta for palavra in ['curso', 'cursos']):
            if 'informática' in pergunta or 'informatica' in pergunta:
                return f"💻 {self.dados_ept['curso_informatica']}"
            elif 'administração' in pergunta or 'administracao' in pergunta:
                return f"📊 {self.dados_ept['curso_administracao']}"
            elif 'desenvolvimento' in pergunta and 'sistema' in pergunta:
                return f"🔧 {self.dados_ept['curso_desenvolvimento']}"
            else:
                return f"🎯 {self.dados_ept['cursos_tecnico']}"
        
        # 🏫 INFRAESTRUTURA
        if any(palavra in pergunta for palavra in ['infraestrutura', 'estrutura', 'instalações', 'instalacoes', 'laboratório', 'laboratorio', 'lab']):
            return f"🏫 {self.dados_ept['infraestrutura']}"
        
        # 👥 EQUIPE E GOVERNANÇA
        if any(palavra in pergunta for palavra in ['diretora', 'joseane']):
            return f"👩‍💼 {self.dados_ept['diretora']}"
        
        if any(palavra in pergunta for palavra in ['coordenador', 'josé', 'josé reis', 'josieliton']):
            return f"👨‍🏫 {self.dados_ept['coordenador_ept']}"
        
        if any(palavra in pergunta for palavra in ['coordenadora', 'pedagógica', 'lúcia', 'regina']):
            return f"👩‍🏫 {self.dados_ept['coordenadora_pedagogica']}"
        
        if any(palavra in pergunta for palavra in ['supervisora', 'jozilene']):
            return f"👩‍💼 {self.dados_ept['supervisora']}"
        
        if any(palavra in pergunta for palavra in ['gerente', '18gre', '18 gre']):
            return f"📋 {self.dados_ept['gerente_18gre']}"
        
        if any(palavra in pergunta for palavra in ['governador', 'governo', 'rafael', 'fonteles']):
            return f"🏛️ {self.dados_ept['governador_piaui']}"
        
        if any(palavra in pergunta for palavra in ['secretário', 'secretario', 'washington']):
            return f"🏛️ {self.dados_ept['secretario_educacao']}"
        
        if any(palavra in pergunta for palavra in ['secretária', 'secretaria', 'maria josé']):
            return f"👩‍💼 {self.dados_ept['secretaria_escola']}"
        
        # ℹ️ INFORMAÇÕES GERAIS
        if any(palavra in pergunta for palavra in ['turma', 'responsável', 'desenvolvedor', 'criador', 'alunos responsaveis']):
            return f"👨‍🎓 {self.dados_ept['turma_responsavel']}"
        
        if any(palavra in pergunta for palavra in ['colaboradores', 'funcionários', 'quantos trabalham', 'equipe']):
            return f"👥 {self.dados_ept['colaboradores_escola']}"
        
        if any(palavra in pergunta for palavra in ['instagram', 'facebook', 'rede social', 'social', '@']):
            return f"📱 {self.dados_ept['redes_sociais']}"
        
        if any(palavra in pergunta for palavra in ['alunos', 'quantos alunos', 'total de alunos']):
            return f"📊 {self.dados_ept['total_alunos']}"
        
        if any(palavra in pergunta for palavra in ['horário', 'horario', 'funcionamento']):
            return f"⏰ {self.dados_ept['horarios_aula']}"
        
        if any(palavra in pergunta for palavra in ['contato', 'telefone', 'email', 'endereço', 'endereco']):
            return f"📞 {self.dados_ept['contato']}"
        
        if any(palavra in pergunta for palavra in ['inscrever', 'inscrição', 'inscricao', 'matricular', 'vestibular']):
            return f"📝 {self.dados_ept['inscricao']}"
        
        if any(palavra in pergunta for palavra in ['preço', 'preco', 'custo', 'mensalidade', 'gratuito', 'pago']):
            return "🎓 **TODOS OS CURSOS SÃO 100% GRATUITOS!**\n✅ Sem mensalidade\n✅ Material didático fornecido\n✅ Acesso a toda infraestrutura\n✅ Transporte escolar disponível"
        
        if any(palavra in pergunta for palavra in ['resultado', 'conquista', 'prêmio', 'premio']):
            return f"🏆 {self.dados_ept['resultados']}"
        
        # ❓ SE NÃO ENCONTRAR
        else:
            return self.resposta_nao_encontrada_show()

    def capturar_nome_visitante(self, pergunta):
        """Captura o nome do visitante de forma inteligente"""
        if any(palavra in pergunta for palavra in ['meu nome é', 'me chamo', 'sou o', 'sou a', 'pode me chamar de']):
            if 'meu nome é' in pergunta:
                self.visitante_nome = pergunta.split('meu nome é')[-1].strip().title()
            elif 'me chamo' in pergunta:
                self.visitante_nome = pergunta.split('me chamo')[-1].strip().title()
            elif 'sou o' in pergunta:
                self.visitante_nome = pergunta.split('sou o')[-1].strip().title()
            elif 'sou a' in pergunta:
                self.visitante_nome = pergunta.split('sou a')[-1].strip().title()
            elif 'pode me chamar de' in pergunta:
                self.visitante_nome = pergunta.split('pode me chamar de')[-1].strip().title()
            
            if self.visitante_nome:
                return f"🎉 🥳 UAU! Prazer em conhecê-lo(a), {self.visitante_nome}!\n\nÉ uma honra ter você aqui no Show do Conhecimento do CETI! 😊\n\nComo posso ajudar?"
        return None

    def saudacao_personalizada_show(self):
        """Saudação super personalizada"""
        saudacao_nome = f", {self.visitante_nome}" if self.visitante_nome else ""
        return f"""🎊 OLÁ{saudacao_nome}! SEJA MUITO BEM-VINDO(A)! 🎊

🤖 Eu sou a IA do CETI Acrísio Veras!
🎓 Aqui temos: Regular, Técnico e AEE
💡 Posso tirar TODAS suas dúvidas!
🎮 Digite 'quiz' para um desafio divertido!

✨ Vamos começar essa aventura do conhecimento? 😊"""

    def despedida_personalizada_show(self):
        """Despedida emocionante"""
        saudacao_nome = f", {self.visitante_nome}" if self.visitante_nome else ""
        return f"""🎓 🥺 OBRIGADO pela visita{saudacao_nome}!

Foi incrível conversar com você! 
Espero que tenha aprendido bastante sobre nossa escola.

🚀 **VENHA FAZER PARTE DO CETI!**
📝 Inscrições abertas o ano todo!

💫 Volte sempre que quiser conversar! 😊"""

    def mostrar_ajuda_show(self):
        """Sistema de ajuda completo"""
        return f"""🆘 **CENTRAL DE AJUDA - CETI SHOW** 🆘

🎮 **COMANDOS ESPECIAIS:**
• 'quiz' - Iniciar jogo de perguntas
• 'pontuação' - Ver sua pontuação no quiz
• 'ajuda' - Mostrar esta mensagem

🎓 **PERGUNTAS POPULARES:**
{chr(10).join([f"• {p}" for p in random.sample(self.perguntas_sugeridas, 5)])}

💡 **DICA:** Me chame pelo nome! Diga "meu nome é [seu nome]"
✨ **CURIOSIDADE:** Desenvolvido pelos alunos do 1º Ano - Desenvolvimento de Sistemas!

{self.visitante_nome + ', ' if self.visitante_nome else ''}Estou aqui para ajudar! 😊"""

    def resposta_nao_encontrada_show(self):
        """Resposta criativa quando não entende"""
        sugestoes = "\n".join([f"• {p}" for p in random.sample(self.perguntas_sugeridas, 3)])
        
        if self.visitante_nome:
            return f"""🤔 {self.visitante_nome}, que pergunta interessante!

Não consegui entender completamente, mas posso ajudar com:

{sugestoes}

🎮 Ou que tal um desafio? Digite 'quiz'!
💭 Pode reformular sua pergunta também! 😊"""
        else:
            return f"""🤔 Hmm, não entendi essa...

Mas posso te ajudar com:

{sugestoes}

🎮 Digite 'quiz' para um jogo divertido!
💡 Ou tente fazer a pergunta de outra forma! 😊"""

    # 📊 RELATÓRIO FINAL SHOW
    def mostrar_relatorio_show(self):
        """Relatório final espetacular"""
        print(f"\n{'📊' * 20}")
        print("🏆 RELATÓRIO FINAL - SHOW DO CONHECIMENTO 🏆")
        print(f"{'📊' * 20}")
        print(f"🤖 Sistema: {self.nome}")
        print(f"🎯 Versão: {self.versao}")
        print(f"📈 Perguntas respondidas: {self.contador_perguntas}")
        
        if self.visitante_nome:
            print(f"👤 Estrela do Show: {self.visitante_nome}")
        
        print(f"\n🎪 ESTATÍSTICAS DO SHOW:")
        
        temas = {
            '🎓 Modalidades': 0, '💻 Cursos': 0, '🏫 Infraestrutura': 0,
            '👥 Equipe': 0, '📝 Inscrições': 0, '🎮 Quiz': 0, '❓ Outros': 0
        }
        
        for item in self.historico:
            pergunta = item['pergunta'].lower()
            if any(p in pergunta for p in ['modalidad', 'regular', 'aee', 'ept']):
                temas['🎓 Modalidades'] += 1
            elif any(p in pergunta for p in ['curso', 'técnico', 'tecnico']):
                temas['💻 Cursos'] += 1
            elif any(p in pergunta for p in ['infraestrutura', 'laboratório', 'sala']):
                temas['🏫 Infraestrutura'] += 1
            elif any(p in pergunta for p in ['diretora', 'coordenador', 'professor', 'equipe']):
                temas['👥 Equipe'] += 1
            elif any(p in pergunta for p in ['inscri', 'matrícula', 'vestibular']):
                temas['📝 Inscrições'] += 1
            elif any(p in pergunta for p in ['quiz', 'pontuação', 'pergunta']):
                temas['🎮 Quiz'] += 1
            else:
                temas['❓ Outros'] += 1
        
        for tema, quantidade in temas.items():
            if quantidade > 0:
                print(f"   {tema}: {quantidade}")
        
        print(f"\n{'🎉' * 5} SHOW CONCLUÍDO COM SUCESSO! {'🎉' * 5}")
        print("O CETI AGRADECE SUA VISITA! VOLTE SEMPRE! 🎓")
