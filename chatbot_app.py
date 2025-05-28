import streamlit as st
from langchain_groq import ChatGroq
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain_core.messages import HumanMessage, AIMessage
from langgraph.graph import StateGraph, END
from typing import TypedDict, Annotated
from langgraph.graph.message import add_messages
from dotenv import load_dotenv
import os
import uuid

# Load environment variables
load_dotenv()
GROQ_API_KEY = os.getenv("GROQ_API_KEY")

# Define the state for LangGraph
class State(TypedDict):
    messages: Annotated[list, add_messages]

# Initialize the Groq model with LangChain
llm = ChatGroq(
    model="llama-3.3-70b-versatile",
    temperature=0.7,
    api_key=GROQ_API_KEY
)

# Define the prompt template
prompt = ChatPromptTemplate.from_messages([
    ("system", """You are a helpful and engaging AI assistant named Grok, created by xAI. 
    Provide detailed, accurate, and conversational responses. Elaborate on the topic as requested, 
    ensuring clarity and depth while maintaining a friendly tone. Use markdown for formatting when appropriate."""),
    MessagesPlaceholder(variable_name="messages")
])

# Define the chatbot node function for LangGraph
def chatbot(state: State):
    user_message = state["messages"][-1].content
    response = prompt | llm
    ai_message = response.invoke({"messages": state["messages"]})
    return {"messages": [ai_message]}

# Set up the LangGraph workflow
graph_builder = StateGraph(State)
graph_builder.add_node("chatbot", chatbot)
graph_builder.set_entry_point("chatbot")
graph_builder.set_finish_point("chatbot")
graph = graph_builder.compile()

# Streamlit app configuration
st.set_page_config(page_title="Chat With Us", layout="wide")

# Custom CSS for a vibrant, modern design with updated form, text area, and send button
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Poppins:wght@400;500;600&display=swap');

body, .stApp {
    background: linear-gradient(135deg, #e0e7ff 0%, #c3cfe2 100%);
    font-family: 'Poppins', sans-serif;
    margin: 0;
    padding: 0;
    overflow: hidden;
}
h1 {
    text-align: center;
    color: #6c5ce7;
    font-size: 40px;
    margin: 20px 0;
    font-weight: 600;
    text-shadow: 1px 1px 3px rgba(0, 0, 0, 0.1);
}
.user-message {
    background: linear-gradient(90deg, #ff6f91, #ff8e53);
    color: white;
    border-radius: 20px 20px 5px 20px;
    padding: 15px 20px;
    margin: 15px 15px 15px 40%;
    max-width: 55%;
    word-wrap: break-word;
    font-size: 16px;
    line-height: 1.5;
    box-shadow: 0 4px 10px rgba(0, 0, 0, 0.1);
    animation: fadeIn 0.3s ease-in;
}
.ai-message {
    background: linear-gradient(90deg, #a29bfe, #74b9ff);
    color: white;
    border-radius: 20px 20px 20px 5px;
    padding: 15px 20px;
    margin: 15px 15px 15px 10px;
    max-width: 55%;
    word-wrap: break-word;
    font-size: 16px;
    line-height: 1.5;
    box-shadow: 0 4px 10px rgba(0, 0, 0, 0.1);
    animation: fadeIn 0.3s ease-in;
}
.welcome-message {
    background: linear-gradient(90deg, #a29bfe, #74b9ff);
    color: white;
    border: 2px solid #6c5ce7;
    border-radius: 20px;
    padding: 20px;
    margin: 15px auto;
    max-width: 70%;
    text-align: center;
    font-size: 16px;
    line-height: 1.5;
    box-shadow: 0 4px 10px rgba(0, 0, 0, 0.1);
    animation: fadeIn 0.5s ease-in;
}
@keyframes fadeIn {
    from { opacity: 0; transform: translateY(10px); }
    to { opacity: 1; transform: translateY(0); }
}
.sidebar .sidebar-content {
    background: #ffffff;
    color: #333;
    border-radius: 15px;
    padding: 25px;
    box-shadow: 0 4px 10px rgba(0, 0, 0, 0.05);
    height: calc(100vh - 40px);
    overflow-y: auto;
}
.sidebar h3 {
    color: #6c5ce7;
    font-size: 24px;
    margin-bottom: 20px;
    font-weight: 600;
}
.sidebar p {
    margin: 5px 0;
    font-size: 14px;
}
.history-item {
    background: #f1f2f6;
    border-radius: 10px;
    padding: 10px 15px;
    margin: 10px 0;
    font-size: 13px;
    border-left: 4px solid #6c5ce7;
}
.history-question {
    color: #ff6f91;
    font-weight: 500;
}
.history-answer {
    color: #333;
}
.input-container {
    position: fixed;
    bottom: 0;
    left: 0;
    right: 0;
    background: #ffffff;
    padding: 15px 20px;
    z-index: 1000;
    box-shadow: 0 -4px 15px rgba(0, 0, 0, 0.1);
}
/* Updated Form Styling */
.stForm {
    max-width: 70%;
    width: 50%;
    margin: 0 auto;
    display: flex;
    align-items: center;
    gap: 15px;
    background: linear-gradient(90deg, #e6e6fa, #f8f9fa);
    border: 2px solid transparent;
    border-image: linear-gradient(90deg, #a29bfe, #74b9ff) 1;
    border-radius: 20px;
    padding: 10px;
    box-shadow: 0 4px 10px rgba(0, 0, 0, 0.1);
}
/* Updated Text Input Styling */
.stTextInput > div > div > input {
    border-radius: 1px;
    padding: 20px 30px;
    border: 2px solid transparent;
    background: linear-gradient(90deg, #f8f9fa, #e6e6fa);
    font-size: 20px;
    font-family: 'Poppins', sans-serif;
    color: #333;
    transition: all 0.3s ease;
    width: 100%;
    height: 100%;
}
.stTextInput > div > div > input:focus {
    outline: none;
    border-image: linear-gradient(90deg, #2196f3, #34c759) 1;
    box-shadow: 0 0 12px rgba(52, 199, 89, 0.4);
}
.stTextInput > div > div > input::placeholder {
    color: #a0a0a0;
    font-style: italic;
}
/* Updated Send Button Styling */
.stButton > button {
    background: linear-gradient(90deg, #ff3d00, #ffd600);
    color: white;
    font-size: 2px;
    font-weight: 25;
    border: 2px solid transparent;
    border-image: linear-gradient(90deg, #ff3d00, #ffd600) 1;
    align-items: center;
    transition: all 0.3s ease;
}
.stButton > button:hover {
    background: linear-gradient(90deg, #ffd600, #ff3d00);
    border-image: linear-gradient(90deg, #ffd600, #ff3d00) 1;
    box-shadow: 0 4px 10px rgba(255, 61, 0, 0.3);
}
</style>
""", unsafe_allow_html=True)

# Initialize session state for chat history
if "chat_history" not in st.session_state:
    st.session_state.chat_history = []
if "messages" not in st.session_state:
    st.session_state.messages = [
        {"role": "assistant", "content": "Hello and Welcome! It’s great to meet you. I’m Grok, your friendly AI assistant from xAI. I’m here to help answer any questions you might have, provide information on a wide range of topics, and engage in conversation. How can I assist you today? Do you have a specific topic in mind or would you like some suggestions to get us started?"}
    ]

# Sidebar for version, tech stack, and chat history
with st.sidebar:
    st.markdown("<h3>Chat With Us</h3>", unsafe_allow_html=True)
    st.markdown("**Version**: 1.0.0")
    st.markdown("**Tech Stack**:")
    st.markdown("- Groq API (Llama-3.3-70b)")
    st.markdown("- LangChain & LangGraph")
    st.markdown("- Streamlit")
    st.markdown("---")
    st.markdown("<h3>Chat History</h3>", unsafe_allow_html=True)
    for chat in st.session_state.chat_history:
        with st.container():
            st.markdown(
                f'<div class="history-item"><p class="history-question">You: {chat["question"]}</p><p class="history-answer">AI: {chat["answer"]}</p></div>',
                unsafe_allow_html=True
            )

# Main chat interface
st.markdown("<h1>Chat With Us</h1>", unsafe_allow_html=True)

# Chat container
with st.container():
    st.markdown('<div class="chat-container">', unsafe_allow_html=True)
    for idx, message in enumerate(st.session_state.messages):
        if idx == 0 and message["role"] == "assistant":
            st.markdown(
                f'<div class="welcome-message">{message["content"]}</div>',
                unsafe_allow_html=True
            )
        elif message["role"] == "user":
            st.markdown(
                f'<div class="user-message">{message["content"]}</div>',
                unsafe_allow_html=True
            )
        else:
            st.markdown(
                f'<div class="ai-message">{message["content"]}</div>',
                unsafe_allow_html=True
            )
    st.markdown('</div>', unsafe_allow_html=True)

# Fixed input form at the bottom
with st.container():
    st.markdown('<div class="input-container">', unsafe_allow_html=True)
    with st.form("chat_form", clear_on_submit=True):
        col1, col2 = st.columns([5, 1])
        with col1:
            user_input = st.text_input("Ask me anything...", key="user_input")
        with col2:
            submit_button = st.form_submit_button("Tap")
    st.markdown('</div>', unsafe_allow_html=True)

# Handle form submission
if submit_button and user_input:
    # Add user message to session state
    st.session_state.messages.append({"role": "user", "content": user_input})
    
    # Show spinner while processing
    with st.spinner("Grok is thinking..."):
        # Invoke LangGraph with the user message
        state = {"messages": [HumanMessage(content=user_input)]}
        result = graph.invoke(state)
        ai_response = result["messages"][-1].content
        
        # Add AI response to session state
        st.session_state.messages.append({"role": "assistant", "content": ai_response})
        st.session_state.chat_history.append({"question": user_input, "answer": ai_response})
    
    # Rerun to update the UI
    st.rerun()