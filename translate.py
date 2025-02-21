import streamlit as st
import openai

# Set OpenAI API key
openai.api_key = "sk-TNjP_ORsBVIwYouwdCRofJkpBb3zUJNcFdiwXhks_rT3BlbkFJQliMPzxI8AST_0rJ_6bmcxMxzZlEYifnpoQa0jpQ0A"
# Initialize chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

with st.chat_message("assistant"):
    st.write("안녕하세요! 무엇이든 제가 한글로 번역해드릴게요!")

prompt = st.chat_input("번역할 문장")

if prompt:
    # Check for toxicity
    moderation_response = openai.Moderation.create(model="text-moderation-latest", input=prompt)
    flagged = moderation_response["results"][0]["flagged"]
    
    # Translate text if not flagged
    if flagged:
        st.error("유해한 내용이 포함되어 있습니다.")
    else:
        translation_response = openai.ChatCompletion.create(
            model="gpt-4", 
            messages=[{"role": "user", "content": f"{prompt}\n 번역해줘."}]
        )
        translation = translation_response.choices[0].message["content"]
        st.session_state.messages.append((prompt, translation, "No Toxicity"))
        st.write(f"번역: {translation}")

for prompt, translation, status in st.session_state.messages:
    with st.chat_message("user"):
        st.write(prompt)
    with st.chat_message("assistant"):
        st.write(f"{translation} ({status})")
