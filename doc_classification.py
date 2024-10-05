import streamlit as st
from langchain.prompts import PromptTemplate
import re

# Function to classify document type
def classify_document(text):
    # Define prompt for LangChain to classify document type
    prompt = f"Classify the following insurance document: {text}. The possible types are Car Insurance, Health Insurance, or Home Insurance."
    response = langchain_classification(prompt)
    return response  # Return classified document type

# Function to extract relevant info based on the document type
def extract_information(text, doc_type):
    extracted_data = {}
    if doc_type == "Car Insurance":
        extracted_data['insurer_name'] = re.search(r"Insurer Name: (.*)", text).group(1)
        extracted_data['address'] = re.search(r"Address: (.*)", text).group(1)
        extracted_data['car'] = re.search(r"Car: (.*)", text).group(1)
        extracted_data['premium'] = re.search(r"Premium: (\d+)", text).group(1)
        extracted_data['start_date'] = re.search(r"Start Date: (.*)", text).group(1)
        extracted_data['end_date'] = re.search(r"End Date: (.*)", text).group(1)
        extracted_data['coverage_amount'] = re.search(r"Coverage Amount: (\d+)", text).group(1)
    elif doc_type =="Health Insurance":
        extracted_data['insurer_name'] = re.search(r"Insurer Name: (.*)", text).group(1)
        extracted_data['address'] = re.search(r"Address: (.*)", text).group(1)
        extracted_data['premium'] = re.search(r"Premium: (\d+)", text).group(1)
        extracted_data['start_date'] = re.search(r"Start Date: (.*)", text).group(1)
        extracted_data['end_date'] = re.search(r"End Date: (.*)", text).group(1)
        extracted_data['coverage_amount'] = re.search(r"Coverage Amount: (\d+)", text).group(1)
    elif doc_type =="Home Insurance":
        extracted_data['insurer_name'] = re.search(r"Insurer Name: (.*)", text).group(1)
        extracted_data['address'] = re.search(r"Address: (.*)", text).group(1)
        extracted_data['premium'] = re.search(r"Premium: (\d+)", text).group(1)
        extracted_data['start_date'] = re.search(r"Start Date: (.*)", text).group(1)
        extracted_data['end_date'] = re.search(r"End Date: (.*)", text).group(1)
        extracted_data['coverage_amount'] = re.search(r"Coverage Amount: (\d+)", text).group(1)
    return extracted_data

# Main function
def main():
    st.title("Insurance Document Classifier & Extractor")

    # Upload document
    uploaded_file = st.file_uploader("Upload an insurance document", type=["txt", "pdf"])
    if uploaded_file is not None:
        # Read file content
        text = uploaded_file.read().decode("utf-8")
        # Step 1: Classify the document type
        doc_type = classify_document(text)
        st.write(f"Document Type: {doc_type}")
        # Step 2: Extract information based on document type
        extracted_info = extract_information(text, doc_type)
        # Step 3: Display extracted information
        st.write("Extracted Information:")
        st.json(extracted_info)

# Utility function to simulate LangChain classification (replace with actual LangChain logic)
def langchain_classification(prompt):
    # This function simulates the LangChain classification logic
    # You would integrate your actual LangChain model here
    if "car" in prompt.lower():
        return "Car Insurance"
    elif "health" in prompt.lower():
        return "Health Insurance"
    else:
        return "Home Insurance"

if __name__ == "__main__":
    main()

