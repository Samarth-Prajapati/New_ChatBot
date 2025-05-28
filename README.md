Chat With Us - A Streamlit Chatbot Application
Overview
"Chat With Us" is a modern, interactive chatbot application built using Streamlit, LangChain, LangGraph, and the Groq API. The chatbot, powered by the Llama-3.3-70B model, provides conversational responses to user queries with a vibrant and user-friendly interface. The application features a customizable chat window, a sidebar for chat history, and a polished design with gradient styling and animations.
Features

Conversational AI: Powered by the Groq API (Llama-3.3-70B model) for accurate and engaging responses.
Modern UI: A vibrant design with gradient backgrounds, rounded corners, and fade-in animations.
Chat History: View past conversations in the sidebar.
Customizable Styling: Easily modify the CSS to change colors, sizes, and other visual elements.
Fixed Input Bar: A sleek input form at the bottom for seamless user interaction.

Prerequisites

Python 3.8+: Ensure Python is installed on your system.
Conda: For managing the virtual environment (optional but recommended).
Groq API Key: Obtain an API key from xAI's API page.
Internet Connection: Required for API calls and dependency installation.

Setup Instructions

Clone the Repository (if applicable):If the project is hosted in a repository, clone it:
git clone <repository-url>
cd <repository-directory>


Create a Virtual Environment:Use Conda (recommended) or another virtual environment manager:
conda create -n chatbot_env python=3.8
conda activate chatbot_env


Install Dependencies:Install the required Python packages using the requirements.txt file (assumed to exist based on the project context):
pip install -r requirements.txt

The requirements.txt should include:
streamlit
langchain-groq
langchain-core
langgraph
python-dotenv


Set Up Environment Variables:Create a .env file in the project root directory and add your Groq API key:
GROQ_API_KEY=<your-groq-api-key>

Ensure the .env file is not committed to version control (e.g., add it to .gitignore).

Run the Application:Start the Streamlit app:
streamlit run chatbot_app.py

The app will open in your default web browser at http://localhost:8501.


Usage

Interact with the Chatbot:

Upon launching the app, you’ll see a welcome message from Grok, the AI assistant.
Type your question or message in the text input field at the bottom (labeled "Ask me anything...").
Click the "Tap" button to send your message.
The chatbot will respond, and the conversation will be displayed in the chat window.


View Chat History:

Past conversations are displayed in the sidebar under "Chat History".
Each entry shows the user’s question and the AI’s response.



Customization
The application’s appearance can be customized by modifying the CSS in the chatbot_app.py file:

Form, Text Area, and Button Styling:The CSS for the form (.stForm), text input (.stTextInput > div > div > input), and send button (.stButton > button) is defined in the <style> section of the st.markdown call. Adjust properties like colors, padding, and gradients to match your desired design.
Example: To change the form’s gradient to pink-to-orange:
.stForm {
    background: linear-gradient(90deg, #ff6f91, #ff8e53);
    border-image: linear-gradient(90deg, #ff6f91, #ff8e53) 1;
}


Other Elements:Modify styles for the chat container (.chat-container), messages (.user-message, .ai-message), and sidebar (.sidebar) to further customize the UI.


Troubleshooting

API Key Error:If you encounter an error related to the Groq API key, ensure the GROQ_API_KEY is correctly set in the .env file and that the key is valid. Check your API usage limits at xAI's API page.

Dependency Issues:If a package fails to install, ensure your Python version is compatible (3.8+ recommended). You can also try installing packages individually:
pip install streamlit langchain-groq langchain-core langgraph python-dotenv


Layout Issues:If the form, text area, or button appear misaligned, check the CSS in chatbot_app.py. Use your browser’s developer tools (right-click > Inspect) to debug and adjust styles.


License
This project is licensed under the MIT License - see the LICENSE file for details (if applicable).

Last updated: May 28, 2025
