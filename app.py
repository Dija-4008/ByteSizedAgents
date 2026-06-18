import streamlit as st
import requests

# 1. Give your storefront a name
st.title("Your Next Client finder")
st.write("Welcome! Type a message below to talk to my marketing AI agent.")

# 2. Get the secret password safely from Streamlit's backend settings
BIND_API_KEY = st.secrets["BAND_API_KEY"]

# 3. Create a box where people can type
user_message = st.text_input("Ask marketing agent something:")

# 4. When they press Enter, send it to Bind AI
if user_message:
    with st.spinner("Agent is thinking..."):
        try:
            # Connect to Bind AI's servers
            # 1. The correct Band.ai "phone number" (API Endpoints)
            url = "https://api.band.ai/v1/chat/completions" 
            
            # 2. Your identification headers
            headers = {
                "Authorization": f"Bearer {BAND_API_KEY}", # This uses your Band.ai API key
                "Content-Type": "application/json"
            }
            
            # 3. The exact message package Band.ai expects
            data = {
                "model": "band-agent", # Instructs Band to route this to your agent
                "messages": [{"role": "user", "content": user_message}]
            }
            # Send the question and get the answer
            response = requests.post(url, json=data, headers=headers)
            result = response.json()
            
            # Show the robot's answer on the screen!
            agent_reply = result["choices"][0]["message"]["content"]
            st.success("Agent Response:")
            st.write(agent_reply)
            
        except Exception as e:
            st.error("Oops! Something went wrong connecting to the agent.")
