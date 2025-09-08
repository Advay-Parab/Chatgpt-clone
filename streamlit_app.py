import streamlit as st
import requests
from typing import List, Tuple, Optional
import time
from datetime import datetime

# Configuration
API_BASE = "http://localhost:8000"
TOPICS = ["General", "Weather", "Science", "Tech", "News", "Sports", "Health", "Entertainment"]

# Custom CSS for better styling
def load_css():
    st.markdown("""
    <style>
    .chat-message {
        padding: 1rem;
        border-radius: 0.5rem;
        margin: 0.5rem 0;
        display: flex;
        align-items: center;
    }
    .user-message {
        background-color: #e3f2fd;
        border-left: 4px solid #2196f3;
    }
    .ai-message {
        background-color: #f3e5f5;
        border-left: 4px solid #9c27b0;
    }
    .timestamp {
        font-size: 0.8rem;
        color: #666;
        margin-left: auto;
    }
    .main-header {
        text-align: center;
        color: #1f77b4;
        margin-bottom: 2rem;
    }
    .auth-button {
        margin: 0.5rem;
        padding: 0.5rem 2rem;
    }
    </style>
    """, unsafe_allow_html=True)

# Initialize session state
def init_session_state():
    """Initialize all session state variables"""
    defaults = {
        "logged_in": False,
        "username": "",
        "chat_history": [],
        "current_page": "home",
        "user_token": ""  # Added for authentication token storage
    }
    
    for key, default_value in defaults.items():
        if key not in st.session_state:
            st.session_state[key] = default_value

# Utility functions
def make_api_request(endpoint: str, method: str = "POST", data: dict = None, headers: dict = None) -> Optional[requests.Response]:
    """Make API request with error handling"""
    try:
        url = f"{API_BASE}{endpoint}"
        
        # Default headers
        if headers is None:
            headers = {}
        
        # Add content type for POST requests
        if method == "POST":
            headers["Content-Type"] = "application/json"
        
        with st.spinner("Processing..."):
            if method == "POST":
                response = requests.post(url, json=data, headers=headers, timeout=10)
            elif method == "GET":
                response = requests.get(url, headers=headers, timeout=10)
            else:
                response = requests.request(method, url, json=data, headers=headers, timeout=10)
                
        # Debug information
        st.write(f"Debug - API Response Status: {response.status_code}")
        st.write(f"Debug - API Response Text: {response.text}")
        
        return response
    except requests.exceptions.Timeout:
        st.error("⏰ Request timed out. Please try again.")
    except requests.exceptions.ConnectionError:
        st.error("🔌 Connection error. Make sure the API server is running on http://localhost:8000")
    except requests.exceptions.RequestException as e:
        st.error(f"🚨 Request error: {str(e)}")
    return None

def validate_credentials(username: str, password: str) -> bool:
    """Validate username and password"""
    if not username or not password:
        st.warning("⚠️ Please enter both username and password.")
        return False
    
    if len(username.strip()) < 3:
        st.warning("⚠️ Username must be at least 3 characters long.")
        return False
        
    if len(password) < 6:
        st.warning("⚠️ Password must be at least 6 characters long.")
        return False
    
    return True

def add_to_chat_history(sender: str, message: str):
    """Add message to chat history with timestamp"""
    timestamp = datetime.now().strftime("%H:%M")
    st.session_state.chat_history.append((sender, message, timestamp))

def display_chat_message(sender: str, message: str, timestamp: str):
    """Display a single chat message with styling"""
    if sender == "You":
        st.markdown(f"""
        <div class="chat-message user-message">
            <div>
                <strong>🧑‍💻 You:</strong> {message}
                <div class="timestamp">{timestamp}</div>
            </div>
        </div>
        """, unsafe_allow_html=True)
    else:
        st.markdown(f"""
        <div class="chat-message ai-message">
            <div>
                <strong>🤖 AI:</strong> {message}
                <div class="timestamp">{timestamp}</div>
            </div>
        </div>
        """, unsafe_allow_html=True)

# Test API connection
def test_api_connection():
    """Test if API server is running"""
    try:
        response = requests.get(f"{API_BASE}/health", timeout=5)
        return response.status_code == 200
    except:
        return False

# Page functions
def home_page():
    """Home page with login/register options"""
    st.markdown('<h1 class="main-header">🤖 Welcome to AI Chat Assistant</h1>', unsafe_allow_html=True)
    
    # Test API connection
    #if not test_api_connection():
        #st.error("🔌 Cannot connect to API server. Make sure the server is running on http://127.0.0.1:8000")
       # st.info("💡 To start the API server, run your backend application first.")
    
    col1, col2, col3 = st.columns([1, 2, 1])
    
    with col2:
        st.markdown("### Choose an option to get started:")
        
        col_login, col_register = st.columns(2)
        
        with col_login:
            if st.button("🔓 Login", use_container_width=True, key="home_login"):
                st.session_state.current_page = "login"
                st.rerun()
        
        with col_register:
            if st.button("🧑‍💻 Register", use_container_width=True, key="home_register"):
                st.session_state.current_page = "register"
                st.rerun()
        
        st.markdown("---")
        st.markdown("**✨ Features:**")
        st.markdown("- 💬 Chat with AI assistant")
        st.markdown("- 📚 Multiple topic categories")
        st.markdown("- 🕓 Chat history")
        st.markdown("- 🔒 Secure user authentication")

def register_page():
    """Registration page"""
    st.title("🧑‍💻 Create an Account")
    
    # Back to home button
    if st.button("← Back to Home"):
        st.session_state.current_page = "home"
        st.rerun()
    
    with st.form("register_form", clear_on_submit=True):
        username = st.text_input("Username", placeholder="Enter your username")
        password = st.text_input("Password", type="password", placeholder="Enter your password")
        confirm_password = st.text_input("Confirm Password", type="password", placeholder="Confirm your password")
        
        col1, col2 = st.columns(2)
        
        with col1:
            submitted = st.form_submit_button("🔐 Register", use_container_width=True)
        with col2:
            if st.form_submit_button("Already have account? Login", use_container_width=True):
                st.session_state.current_page = "login"
                st.rerun()
        
        if submitted:
            if password != confirm_password:
                st.error("❌ Passwords don't match!")
                return
                
            if validate_credentials(username, password):
                # Clean the username
                clean_username = username.strip()
                
                response = make_api_request("/users/register", "POST", data={
                    "username": clean_username,
                    "password": password
                })
                
                if response:
                    if response.status_code == 200 or response.status_code == 201:
                        st.success("✅ Registered successfully! Redirecting to login...")
                        time.sleep(2)
                        st.session_state.current_page = "login"
                        st.rerun()
                    else:
                        try:
                            error_msg = response.json().get("detail", response.text)
                        except:
                            error_msg = response.text
                        st.error(f"❌ Registration failed: {error_msg}")

def login_page():
    """Login page"""
    st.title("🔓 Login to Your Account")
    
    # Back to home button
    if st.button("← Back to Home"):
        st.session_state.current_page = "home"
        st.rerun()
    
    with st.form("login_form"):
        username = st.text_input("Username", placeholder="Enter your username")
        password = st.text_input("Password", type="password", placeholder="Enter your password")
        
        col1, col2 = st.columns(2)
        
        with col1:
            submitted = st.form_submit_button("➡️ Login", use_container_width=True)
        with col2:
            if st.form_submit_button("Need an account? Register", use_container_width=True):
                st.session_state.current_page = "register"
                st.rerun()
        
        if submitted and validate_credentials(username, password):
            # Clean the username
            clean_username = username.strip()
            
            response = make_api_request("/users/login", "POST", data={
                "username": clean_username,
                "password": password
            })
            
            if response:
                if response.status_code == 200:
                    # Try to get token from response
                    try:
                        response_data = response.json()
                        token = response_data.get("token", "") or response_data.get("access_token", "")
                        st.session_state.user_token = token
                    except:
                        st.session_state.user_token = ""
                    
                    # Set login state
                    st.session_state.logged_in = True
                    st.session_state.username = clean_username
                    st.success("✅ Logged in successfully! Redirecting to chat...")
                    time.sleep(2)
                    st.session_state.current_page = "chat"
                    st.rerun()
                else:
                    try:
                        error_msg = response.json().get("detail", response.text)
                    except:
                        error_msg = response.text
                    st.error(f"❌ Login failed: {error_msg}")

def chat_page():
    """Chat page"""
    # Check if user is logged in
    if not st.session_state.logged_in:
        st.error("⚠️ You need to be logged in to access the chat!")
        col1, col2 = st.columns(2)
        with col1:
            if st.button("🔓 Go to Login", use_container_width=True):
                st.session_state.current_page = "login"
                st.rerun()
        with col2:
            if st.button("🧑‍💻 Go to Register", use_container_width=True):
                st.session_state.current_page = "register"
                st.rerun()
        return
    
    # Chat header with user info and controls
    col1, col2, col3 = st.columns([2, 1, 1])
    with col1:
        st.title(f"💬 Chat - Welcome, {st.session_state.username}!")
    with col2:
        if st.button("🏠 Home"):
            st.session_state.current_page = "home"
            st.rerun()
    with col3:
        if st.button("🚪 Logout"):
            # Clear all session data
            st.session_state.logged_in = False
            st.session_state.username = ""
            st.session_state.chat_history = []
            st.session_state.user_token = ""
            st.session_state.current_page = "home"
            st.success("Logged out successfully!")
            time.sleep(1)
            st.rerun()
    
    # Chat input form
    with st.form("chat_form", clear_on_submit=True):
        col1, col2 = st.columns([3, 1])
        
        with col1:
            message = st.text_area("💭 Your message:", placeholder="Type your message here...", height=100)
        with col2:
            topic = st.selectbox("📚 Topic:", TOPICS)
            st.write("")  # Spacing
            send_button = st.form_submit_button("🚀 Send", use_container_width=True)
    
    # Process chat message
    if send_button and message.strip():
        # Prepare headers
        headers = {"X-Username": st.session_state.username}
        
        # Add token if available
        if st.session_state.user_token:
            headers["Authorization"] = f"Bearer {st.session_state.user_token}"
        
        response = make_api_request("/chat", "POST", data={
            "message": message.strip(),
            "topic": topic
        }, headers=headers)
        
        if response:
            if response.status_code == 200:
                try:
                    response_data = response.json()
                    reply = response_data.get("response", "No response received")
                    add_to_chat_history("You", message.strip())
                    add_to_chat_history("AI", reply)
                    st.rerun()  # Refresh to show new messages
                except Exception as e:
                    st.error(f"❌ Error parsing response: {str(e)}")
            elif response.status_code == 401:
                st.error("❌ Authentication failed. Please login again.")
                st.session_state.logged_in = False
                st.session_state.current_page = "login"
                st.rerun()
            else:
                try:
                    error_msg = response.json().get("detail", response.text)
                except:
                    error_msg = response.text
                st.error(f"❌ Chat failed: {error_msg}")
    elif send_button:
        st.warning("⚠️ Please enter a message before sending.")
    
    # Display chat history
    if st.session_state.chat_history:
        st.markdown("---")
        
        # Chat history header with clear button
        col1, col2 = st.columns([3, 1])
        with col1:
            st.subheader("💬 Chat History")
        with col2:
            if st.button("🗑️ Clear History"):
                st.session_state.chat_history = []
                st.rerun()
        
        # Display messages in reverse order (newest first)
        for sender, msg, timestamp in reversed(st.session_state.chat_history):
            display_chat_message(sender, msg, timestamp)
    else:
        st.info("💡 Start a conversation by typing a message above!")

# Main app
def main():
    # Page config
    st.set_page_config(
        page_title="AI Chat Assistant",
        page_icon="🤖",
        layout="wide",
        initial_sidebar_state="collapsed"  # Hide sidebar by default
    )
    
    # Load CSS and initialize session
    load_css()
    init_session_state()
    
    # Hide sidebar completely
    st.markdown(
        """
        <style>
            .css-1d391kg {display: none;}
            .css-18e3th9 {padding-top: 0;}
        </style>
        """,
        unsafe_allow_html=True
    )
    
    # Debug information (remove this in production)
    with st.sidebar:
        st.write("Debug Info:")
        st.write(f"Logged in: {st.session_state.logged_in}")
        st.write(f"Username: {st.session_state.username}")
        st.write(f"Current page: {st.session_state.current_page}")
        st.write(f"Has token: {bool(st.session_state.user_token)}")
    
    # Route to appropriate page based on session state
    if st.session_state.current_page == "home":
        home_page()
    elif st.session_state.current_page == "register":
        register_page()
    elif st.session_state.current_page == "login":
        login_page()
    elif st.session_state.current_page == "chat":
        chat_page()
    else:
        # Default to home if current_page is not recognized
        st.session_state.current_page = "home"
        home_page()

if __name__ == "__main__":
    main()