import streamlit as st
from groq import Groq

st.title("AI Powered Finance - Demo")

st.image('ai-powered-finance.jpg', caption='AI Powered Finance',width=400)

client = Groq(
    api_key= os.environ.get("GROQ_API_KEY"),
)

def question_groq(text):
    chat_completion = client.chat.completions.create(
        messages=[
            {
                "role": "user",
                "content": text
            }
        ],
        # model="mixtral-8x7b-32768",
        model="llama3-70b-8192"
    )
    return chat_completion.choices[0].message.content

message_input = st.text_input("Your Prompt:", "")

col1, col2 = st.columns(2)

character = col1.selectbox(
    "Generate answer as Sucession character?",
    ("Logan Roy", "Tom Wambsgans", "Greg Hirsch","Kendall Roy", "Marcia Roy", "Roman Roy", "Shiv Roy"))

reviewer = col2.selectbox(
    "Review it as Lawyer?",
    ("", "Alan Dershowitz", "Gloria Allred", "Harish Salve", "Gerry Spence", "Thurgood Marshall", "Jose Baez", "Joe Jamail"))

isSucession = col1.checkbox("As Sucession")
isLawyer = col2.checkbox("As Lawyer")

if st.button("Send"):
    if isSucession:
        message_input = message_input + f" . Write it as {character} from Sucession."
    if isLawyer:
        message_input = message_input + f" . And review it as the top lawyer {reviewer}."
    if message_input:
        result = question_groq(message_input)
        st.markdown("### "+message_input)
        st.markdown(result)
