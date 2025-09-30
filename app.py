import gradio as gr

def chat_fn(message, history=[]):
    # 실제 모델 연결 대신 테스트용 응답
    return history + [(message, f"DeepSeek 응답: {message[::-1]}")]

demo = gr.ChatInterface(fn=chat_fn, title="DeepSeek V3.2 Exp Test")

if __name__ == "__main__":
    demo.launch()


#01
#def test_fn(txt):
#    return f"입력한 내용: {txt}"

#demo = gr.Interface(fn=test_fn, inputs="text", outputs="text")

#if __name__ == "__main__":
#    demo.launch()
