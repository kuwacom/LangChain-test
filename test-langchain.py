import requests
from bs4 import BeautifulSoup
from langchain_community.llms import LlamaCpp
from langchain_core.callbacks import CallbackManager, StreamingStdOutCallbackHandler
from langchain_core.prompts import PromptTemplate

# モデルのパスを指定してください
MODEL_PATH = "./models/Llama-3-ELYZA-JP-8B-GGUF/Llama-3-ELYZA-JP-8B-q4_k_m.gguf"

def fetch_html(url):
    response = requests.get(url)
    response.raise_for_status()
    return response.text

def extract_text_from_html(html):
    soup = BeautifulSoup(html, 'html.parser')
    return soup.get_text()

# プロンプトテンプレートを作成
template = """
以下のテキストに基づいて質問に答えてください。

テキスト: {context}

質問: {question}

答え:
"""

prompt = PromptTemplate(template=template, input_variables=["context", "question"])

callback_manager = CallbackManager([StreamingStdOutCallbackHandler()])
# ローカルのllama-cppモデルを初期化
llm = LlamaCpp(
    model_path=MODEL_PATH,
    temperature=0.75,
    n_ctx=2048,
    # top_p=1,
    callback_manager=callback_manager,
    # verbose=True,  # Verbose はコールバックマネージャーに渡す必要性あり
    # n_gpu_layers=-1,
    n_gpu_layers=30
)

llm_chain = prompt | llm

def answer_question_from_url(url, question):
    html = fetch_html(url)
    context = extract_text_from_html(html)
    # プロンプトテンプレートとモデルを使ってLLMチェーンを作成
    response = llm_chain.invoke({"context": context, "question": question})
    return response

if __name__ == "__main__":
    # url = "https://dwango.co.jp/news/5206399155961856/"  # 質問対象のウェブサイトURL
    url = "https://kuwa.dev/"
    question = "このサイトは何について書いてありますか？"
    answer = answer_question_from_url(url, question)
    print("答え:", answer)
