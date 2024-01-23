import tempfile
import os
import streamlit as st
import PyPDF2

# Specify the output directory and filename
output_dir = "output"
output_filename = "pdf_final.pdf"
output_path = os.path.join(output_dir, output_filename)

def join_pdfs(output_path, documents):
    pdf_final = PyPDF2.PdfMerger()
    
    for document in documents:
        pdf_final.append(document)
    
    with open(output_path, "wb") as output_file:
        pdf_final.write(output_file)

st.header("Join PDF")
st.subheader("Attach PDFs to join")

pdf_attached = st.file_uploader(label="", accept_multiple_files=True)

join = st.button(label="Join PDFs")

if join:
    if pdf_attached is None or len(pdf_attached) <= 1:
        st.warning("You must attach at least two PDFs to join.")
    else:
        os.makedirs(output_dir, exist_ok=True)  # Create the output directory if it doesn't exist
        with tempfile.NamedTemporaryFile(delete=False) as temp_file:
            temp_file.close()
            join_pdfs(temp_file.name, pdf_attached)
        
        st.success("Download from Here")
        
        with open(temp_file.name, "rb") as file:
            pdf_data = file.read()
            
        st.download_button(label="Download PDF", data=pdf_data, file_name=output_filename)
