import os
import streamlit as st
from PIL import Image
from invoice_reader.functions import extract_pdf_contents, provide_answer

try:

    OPENAI_APY_KEY = os.getenv("OPENAI_API_KEY")

    # Set path for pdf file
    pdf_path = "./src/Invoice1.pdf"

    # Read pdf file
    pdf_contents = extract_pdf_contents(pdf_path)

    # Set path for image file
    image= Image.open('./src/Invoice1.png')

    # Display the pdf image
    st.image(image=image)
        
    # Initialize state variable
    if "read" not in st.session_state:
        st.session_state["read"] = ""

    # Create an input text box for the user to enter the question
    input_text = st.text_area(label="Enter a question about the invoice:", value="", height=250)

    # Create a submit button
    st.button(
        label="Submit",
        on_click=provide_answer,
        kwargs={"pdf_contents": pdf_contents, "input_text": input_text}
    )

    # Create an output text box that shows the current state of the output
    answer = st.text_area(label="Answer: ", value=st.session_state["read"], height=250)

except:
    st.write("There was an error.")