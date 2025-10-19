import re
import pandas as pd

def parse_plano_estudo(texto):
    """
    Parser universal aprimorado para planos de estudo gerados por IA.
    Detecta módulos, semanas, duração e links automaticamente.
    """

    linhas = [l.strip() for l in texto.split("\n") if l.strip() != ""]
    dados = []

    modulo_atual = "Módulo 1"
    for linha in linhas:
        # Detecta se é título de módulo/semana
        if re.search(r"(semana|m[oó]dulo)\s*\d+", linha.lower()):
            modulo_atual = linha.strip()
            continue

        # Detecta linhas numeradas
        padrao_num = re.match(r"(\d+[\.)️⃣]?\s*)(.*)", linha)
        if padrao_num:
            conteudo = padrao_num.group(2)

            # Detecta link
            link = re.search(r"(https?://\S+)", conteudo)
            link = link.group(1) if link else ""

            # Remove o link do texto principal
            titulo_limpo = re.sub(r"https?://\S+", "", conteudo).strip()

            # Detecta duração (2h, 3 horas, etc.)
            duracao = re.search(r"(\d+)\s*(h|horas?)", conteudo.lower())
            duracao_horas = int(duracao.group(1)) if duracao else None

            # Detecta tipo de conteúdo
            if any(x in titulo_limpo.lower() for x in ["curso", "aula", "treinamento"]):
                tipo = "Curso"
            elif any(x in titulo_limpo.lower() for x in ["livro", "obra", "manual"]):
                tipo = "Livro"
            elif any(x in titulo_limpo.lower() for x in ["artigo", "paper", "scielo", "revista"]):
                tipo = "Artigo"
            elif any(x in titulo_limpo.lower() for x in ["vídeo", "youtube"]):
                tipo = "Vídeo"
            else:
                tipo = "Outro"

            dados.append({
                "modulo": modulo_atual,
                "etapa": titulo_limpo,
                "tipo": tipo,
                "duracao_horas": duracao_horas,
                "recurso": link
            })

    df = pd.DataFrame(dados)
    return df

