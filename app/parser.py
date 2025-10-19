import re
import pandas as pd

def parse_plano_estudo(texto):
    """
    Parser universal para planos de estudo gerados por IA (ChatGPT, etc.)
    Detecta módulos, recursos, links e títulos automaticamente.
    """

    linhas = [l.strip() for l in texto.split("\n") if l.strip() != ""]
    dados = []

    for linha in linhas:
        padrao_num = re.match(r"(\d+[\.)️⃣]?\s*)(.*)", linha)
        if padrao_num:
            conteudo = padrao_num.group(2)

            link = re.search(r"(https?://\S+)", conteudo)
            link = link.group(1) if link else ""

            titulo_limpo = re.sub(r"https?://\S+", "", conteudo).strip()

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
                "etapa": titulo_limpo,
                "tipo": tipo,
                "recurso": link
            })

    df = pd.DataFrame(dados)
    return df
