import streamlit as st
from langchain.prompts import PromptTemplate
from langchain.llms.ctransformers import CTransformers


st.set_page_config(layout="centered", page_title="Generate Blogs", page_icon="🤖", initial_sidebar_state="collapsed")


# Load the model
def getLlamaResponse(input_text, no_of_words, blog_style):
    with st.spinner('Generating blog...'):
        llm = CTransformers(model = "models\llama-2-7b-chat.ggmlv3.q8_0.bin", model_type = "llama", 
                            config = {'max_new_tokens': 256, 'temperature':0.01})
        
        template = "Write a blog for {blog_style} job profile for a topic {input_text} within {no_of_words} words."
        prompt = PromptTemplate(input_variables=['blog_style', 'input_text', 'no_of_words'], template=template)
        response = llm(prompt.format(blog_style=blog_style, input_text=input_text, no_of_words=no_of_words))
    return response


st.header("Generate Blogs 🤖")

input_text = st.text_input("Enter the Blog Topic")

col1, col2 = st.columns(2)

with col1:
    no_of_words = st.text_input("Enter the number of words")

with col2:
    blog_style = st.selectbox("Writing the Blog for", ('General Audience', 'Researchers', 'Students'), index=0)

submit = st.button("Generate Blog")

if submit:
    st.write(getLlamaResponse(input_text, no_of_words, blog_style))


