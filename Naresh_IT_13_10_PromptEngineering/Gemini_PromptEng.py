import streamlit as st
import google.generativeai as genai
import base64

# Function to convert a local image file to a base64 string
def get_base64_image(image_path):
    """Converts local file to base64 string for CSS background."""
    try:
        with open(image_path, "rb") as img_file:
            return base64.b64encode(img_file.read()).decode()
    except FileNotFoundError:
        st.error(f"Error: Image file not found at '{image_path}'. Check the path and file name.")
        return None

# --- Background CSS Injection ---
IMAGE_PATH = r"C:\Users\nikhi\PycharmProjects\NARESH_IT\13_NARESH_IT_GENERATIVE_AI\Naresh_IT_13_10_PromptEngineering\huawei-matebook-4120x4120-22555.png"

# Convert image to base64
base64_img = get_base64_image(IMAGE_PATH)

if base64_img:
    # Construct the CSS style
    page_bg_img = f"""
    <style>
    .stApp {{
        background-image: url("data:image/png;base64,{base64_img}");
        background-size: cover; /* Adjusts the size of the background image to cover the entire container */
        background-attachment: fixed; /* Ensures the image stays in place when scrolling */
        background-position: center; /* Centers the image */
    }}
    </style>
    """
    # Inject the CSS using unsafe_allow_html=True
    st.markdown(page_bg_img, unsafe_allow_html=True)
# --- End Background CSS Injection ---


# -------------------------------
# CONFIGURATION
# -------------------------------
st.set_page_config(page_title="Gemini RAG App", page_icon="🤖", layout="centered")
st.title("🤖 Prompt engineering using Gemini ")

# Gemini API Key input (for demo purposes)
api_key = st.text_input("🔑 Enter your Gemini API Key", type="password")

if api_key:
    genai.configure(api_key=api_key)


    # Dummy retriever for demonstration
    def retriever_info(query):
        # Here you could add a vector search, database lookup, or PDF retriever
        return "Explain about indias next future plank"


    # Main RAG function
    def rag_query(query):
        retrieved_info = retriever_info(query)
        augmented_prompt = f"User query: {query}. Retrieved information: {retrieved_info}"

        model_name = "gemini-2.0-flash"  # try "gemini-pro" if flash not available
        model = genai.GenerativeModel(model_name)

        response = model.generate_content(
            augmented_prompt,
            generation_config={
                "temperature": 0.7,
                "max_output_tokens": 2000,
                "top_p": 1,
                "frequency_penalty": 0,
                "presence_penalty": 0,
                "stop_sequences": ["End"]
            }
        )
        return response.text.strip()


    # -------------------------------
    # UI Section
    # -------------------------------
    query = st.text_area("💬 Ask a question:", "Explain about indias next future plank")

    if st.button("🔍 Generate Response"):
        if not query.strip():
            st.warning("Please enter a query first.")
        else:
            with st.spinner("Generating response..."):
                try:
                    answer = rag_query(query)
                    st.success("✅ Response Generated!")
                    st.markdown(f"**Answer:**\n\n{answer}")
                except Exception as e:
                    st.error(f"Error: {e}")
else:
    st.info("Please enter your Gemini API key to start.")

# -------------------------------
# Footer
# -------------------------------
st.markdown("---")
st.caption("Built with ❤️ using Streamlit + Google Gemini API")
