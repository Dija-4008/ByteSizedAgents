import streamlit as st
import requests

# 1. Give your storefront a name
st.title("Your Next Client finder")
st.write("Welcome! Type a message below to talk to my marketing AI agent.")

# 2. Get the secret password safely from Streamlit's backend settings
# Fixed to say BAND_API_KEY on both sides
BAND_API_KEY = st.secrets["BAND_API_KEY"]

# 3. Create a box where people can type
user_message = st.text_input("Ask marketing agent something:")

# 4. When they press Enter, send it to Band.ai
if user_message:
    with st.spinner("Agent is thinking..."):
        try:
            url = "https://api.band.ai/v1/chat/completions" 
            
            headers = {
                "Authorization": f"Bearer {BAND_API_KEY}", 
                "Content-Type": "application/json"
            }
            
            data = {
                # CHANGE THIS to your Head Agent's ID or API Name from app.band.ai
                "model": "@20rummy05/head", 
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
