# 🤖 AIA Mentora

Sistema inteligente de recomendação de estudos com IA.

## 🚀 Funcionalidades
- Gera trilhas de estudo automaticamente (usando ChatGPT)
- Converte planos em dados estruturados (parser universal)
- Gera reforços personalizados conforme o feedback do aluno
- Envia lembretes por e-mail, WhatsApp e Telegram

## 🧩 Estrutura
- `parser.py` → transforma o plano do ChatGPT em JSON/CSV
- `reforco.py` → cria reforços didáticos com IA
- `feedback.py` → coleta e analisa respostas dos alunos

## 💻 Como rodar localmente
```bash
git clone https://github.com/seuusuario/aia-mentora.git
cd aia-mentora
pip install -r requirements.txt
streamlit run app/main.py
