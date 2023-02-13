import streamlit as st
import PyPDF2
from langchain import OpenAI, PromptTemplate, LLMChain

def extract_pdf_contents(path):
    #This function takes a path to a pdf file as an input and returns the contents of the pdf file as a string.
    read_pdf = PyPDF2.PdfReader(path)
    page = read_pdf.pages[0]
    page_content = page.extract_text()
    return page_content

def provide_answer(pdf_contents, input_text):

    #This function takes a question as an input and returns a response based on the prompt already given to the model.
    augmented_prompt = """You are an Accounts Payable Manager who is responsible for reviewing and approving invoices.
    You are reviewing the following invoice and are asked a question about the invoice. Here are the contents of the invoice you are reviewing: {pdf_contents}
    All information after the purchase order number is in a tabular format.
    If the question requires you to perform any calculations, perform the calculations first before providing an answer.
    Explain your reasoning for the answer you provide on the invoice.
    Question: {question}"""

    try:
        #st.session_state["state"] is a Python dictionary that stores the state of the app. It is used to store the prompt and the response.

        prompt_template = PromptTemplate(
            input_variables=["pdf_contents", "question"],
            template=augmented_prompt
        )

        llm_chain = LLMChain(
            prompt=prompt_template,
            llm=OpenAI(
                model_name="text-davinci-003", 
                temperature=0
            ),
            verbose=True
        )

        st.session_state["read"] = llm_chain.predict(pdf_contents=pdf_contents, question=input_text)
    
    except:
        st.write("There was an error.")


