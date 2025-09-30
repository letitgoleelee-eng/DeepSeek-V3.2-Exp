import gradio as gr

def test_fn(txt):
    return f"입력한 내용: {txt}"

demo = gr.Interface(fn=test_fn, inputs="text", outputs="text")

if __name__ == "__main__":
    demo.launch()
