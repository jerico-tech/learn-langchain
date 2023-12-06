import gradio as gr


# 处理程序
def greet(name):
    return "Hello " + name + "!"


# 接口创建函数
# fn设置处理函数，inputs设置输入接口组件，outputs设置输出接口组件；这三个都是必填函数
demo = gr.Interface(
    fn=greet,
    # 自定义输入框，具体设置方法查看官方文档
    inputs=gr.Textbox(lines=3, placeholder="Name Here ...", label="my input"),
    outputs="text")

if __name__ == '__main__':
    app, local_url, share_url = demo.launch()