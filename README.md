# 🎭 Memebot

Chatbot geral com múltiplas personalidades cômicas inspiradas em memes e
personagens populares da internet brasileira. Por trás da encenação, cada
persona continua respondendo com precisão a qualquer pergunta — a piada está
no jeito de falar, não no conteúdo da resposta.

Interface em [Streamlit](https://streamlit.io/), respostas via
[Groq](https://groq.com/) (modelos Llama), com streaming de texto.

## Personas disponíveis

| Persona | Inspiração | Vibe |
|---|---|---|
| 🤠 Compadrebot | Compadre Washington (É o Tchan) | Hype man de axé, bordões e camaradagem |
| 🧤 Maicon Jéquebot | Sósia cearense do Michael Jackson | Sotaque cearense fechado + MJ decorado de ouvido |
| 💪 Cariribot | Fisiculturista influencer | Intensidade máxima, "eu quero, eu posso" |
| 🎸 Manoelbot | Cantor viral da Caneta Azul | Português bom demaize |

Escolha a persona pela barra lateral do app; cada uma mantém seu próprio
histórico de conversa.

## Pré-requisitos

- Python 3.10+
- Uma chave de API da [Groq](https://console.groq.com/keys)

## Instalação

```bash
cd Memebot
python -m venv .venv
.venv/Scripts/activate   # Windows
pip install -r requirements.txt
```

## Configuração

Crie um arquivo `.env` na raiz do projeto com:

```
GROQ_API_KEY=sua_chave_aqui
```

## Rodando o app

```bash
streamlit run app.py
```

Acesse `http://localhost:8501` (ou a porta indicada no terminal).

## Estrutura do projeto

```
Memebot/
├── app.py                # App Streamlit: seleção de persona + loop de chat
├── persona.py             # System prompt do Compadrebot
├── persona_maicon.py       # System prompt do Maicon Jéquebot
├── persona_cariani.py      # System prompt do Cariribot
├── persona_manoel.py       # System prompt do Manoelbot
├── requirements.txt        # Dependências (streamlit, groq, python-dotenv)
└── .env                    # Chave da API (não versionado)
```

## Adicionando uma nova persona

1. Crie um `persona_<nome>.py` com uma constante `SYSTEM_PROMPT`.
2. Importe o prompt em `app.py`.
3. Adicione uma nova entrada no dicionário `PERSONAS` com `title`, `icon`,
   `caption` e `placeholder`.

## Aviso

Projeto cômico/paródia, feito por diversão e para uso pessoal. As
personalidades são caricaturas exageradas inspiradas em figuras públicas,
sem intenção de ofender.
