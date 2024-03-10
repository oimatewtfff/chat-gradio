import gradio as gr

from gpt_client import ask_gpt

chat = gr.ChatInterface(
    ask_gpt,
    chatbot=gr.Chatbot(height=550),
    textbox=gr.Textbox(placeholder="Введите свой вопрос", container=False, scale=7),
    title="GPT-3.5",
    theme="soft",
    examples=["Привет", "Проверка связи", "Проверял ли я сейчас связь?"],
    retry_btn=None,
    undo_btn=None,
    clear_btn="Очистить",
)

