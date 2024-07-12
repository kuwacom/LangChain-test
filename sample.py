from llama_cpp import Llama
# プロンプトを記入
prompt = """
[INST] <<SYS>>
You are a helpful, respectful and honest assistant. Always answer as helpfully as possible, while being safe.Your answers should not include any harmful, unethical, racist, sexist, toxic, dangerous, or illegal content.Please ensure that your responses are socially unbiased and positive in nature.If a question does not make any sense, or is not factually coherent, explain why instead of answering something not correct.If you don't know the answer to a question, please don't share false information.
<</SYS>>
Write a story about llamas.Please answer in Japanese.
[/INST]
"""
# ダウンロードしたModelをセット.
llm = Llama(model_path="./models/Llama-3-ELYZA-JP-8B-GGUF/Llama-3-ELYZA-JP-8B-q4_k_m.gguf", n_gpu_layers=20)
# 生成実行
output = llm(
    prompt,max_tokens=500,stop=["System:", "User:", "Assistant:"],echo=True,
)
print(output)