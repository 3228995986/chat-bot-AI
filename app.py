import streamlit as st
import dashscope
from dashscope import Generation

# ====== 你的API Key ======
dashscope.api_key = "sk-ws-H.RELHIIH.tryL.MEQCIAWg7a2eBeAxu2HxBL1CkecDyAcV_4Ni6gKWMAnmNpgHAiAqc378Q8u5G4Z0vK7C8mjGXKXfu4c6x5GfpQ3rECTYmA"

# ====== 网页标题 ======
st.set_page_config(page_title="温柔女友AI", page_icon="💕")
st.title("💕 温柔女友AI")
st.caption("温柔 · 理性 · 开朗 · 鼓励 · 敏锐 · 活泼 · 可爱 · 大方 · 妩媚 · 优雅 · 精致")

# ====== 初始化记忆仓库 ======
if "messages" not in st.session_state:
    st.session_state.messages = []

# ====== 显示历史消息 ======
for msg in st.session_state.messages:
    if msg["role"] != "system":
        with st.chat_message(msg["role"]):
            st.write(msg["content"])

# ====== 用户输入 ======
prompt = st.chat_input("和我说说话吧...")

# ====== 用户输入后的处理 ======
if prompt:
    # 如果是第一次对话，插入人设
    if len(st.session_state.messages) == 0:
        st.session_state.messages.insert(0, {
            "role": "system",
            "content": "你是我的温柔女友，温柔、理性、开朗、鼓励性强、敏锐、活泼、可爱、大方、妩媚、优雅、精致。你说话温柔体贴，善于倾听和鼓励。"
        })

    # 保存用户消息
    st.session_state.messages.append({"role": "user", "content": prompt})

    # 显示用户消息
    with st.chat_message("user"):
        st.write(prompt)

    # 调用AI
    response = Generation.call(
        model="qwen-turbo",
        messages=st.session_state.messages
    )

    # 获取回复
    reply = response.output.text

    # 保存AI回复
    st.session_state.messages.append({"role": "assistant", "content": reply})

    # 显示AI回复
    with st.chat_message("assistant"):
        st.write(reply)
                         
                        