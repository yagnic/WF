import os
import PyPDF2
import streamlit as st
from tqdm import tqdm
from collections import defaultdict
import re
import pandas as pd
import statistics
import matplotlib.pyplot as plt



MSCI = ['A','AA','AAA','B','BB','BBB','CCC']


def get_msci(complete_new_text_list):
    try:
        ratings = []
        for com in complete_new_text_list:

            if "MSCI" in com:

                for rating in MSCI:
                    if rating in com:
                        for sent in com.split("."):
                            if rating in sent:

                                sent = sent.replace("“","")
                                sent = sent.replace("”","")
                                pattern = r'\b(?:AA |A |BB |BBB |CCC |AAA )\b'
                                matches = re.findall(pattern, sent)
                                ratings.extend(matches)

        return statistics.mode(ratings)
    except Exception as e:
        return False
    


    
    

def get_net_zero(complete_new_text_list):
    try:
        ratings = []
        for com in complete_new_text_list:


            if "net zero" in com.lower():

                for sent in com.split("."):



                    sent = sent.replace("“","")
                    sent = sent.replace("”","")

                    pattern = r'by (\d+)'
                    matches = re.findall(pattern, sent)

                    ratings.extend(matches)
        ratings = [int(rating)for rating in ratings]
        return max(ratings)
    except Exception as e:
        print(e)
        return False
    


    
    

def get_interim_emissions(complete_new_text_list):
    try:
        ratings = []
        for com in complete_new_text_list:

            if "interim" in com.lower():
                print(com)

                for sent in com.split("."):



                    sent = sent.replace("“","")
                    sent = sent.replace("”","")

                    pattern = r'by (\d+)'
                    matches = re.findall(pattern, sent)

                    ratings.extend(matches)
        ratings = [int(rating)for rating in ratings]
        return max(ratings)
    except Exception as e:
        print(e)
        return False
    


    
    

def get_renewable_target(complete_new_text_list):
    try:
        ratings = []
        for com in complete_new_text_list:

            if "renewable" in com.lower():

                for sent in com.split("."):



                    sent = sent.replace("“","")
                    sent = sent.replace("”","")

                    pattern = r'by (\d+)'
                    matches = re.findall(pattern, sent)

                    ratings.extend(matches)
        ratings = [int(rating)for rating in ratings]
        if max(ratings)>2000:
            return max(ratings)
        else:
            return False
    except Exception as e:
        print(e)
        return False
    


    
    

def get_circularity_target(complete_new_text_list):
    
    try:
        ratings = []
        for com in complete_new_text_list:

            if "circularity" in com.lower():
               

                for sent in com.split("."):



                    sent = sent.replace("“","")
                    sent = sent.replace("”","")

                    pattern = r'by (\d+)'
                    matches = re.findall(pattern, sent)

                    ratings.extend(matches)
        ratings = [int(rating)for rating in ratings]
        return max(ratings)
    except Exception as e:
        print(e)
        return False
    


    
    

def get_diversity_target(complete_new_text_list):
    
    try:
        ratings = []
        for com in complete_new_text_list:

            if "diversity" in com.lower() or 'inclusion' in com.lower():
                ratings.append(True)
                
               


        return any(ratings)
    except Exception as e:
        print(e)
        return False


    
    

def get_employee_inclusion_target(complete_new_text_list):
    
    try:
        ratings = []
        for com in complete_new_text_list:

            if "employee health" in com.lower():
                ratings.append(True)
                
               


        return any(ratings)
    except Exception as e:
        print(e)
        return False

def get_supply_chain_target(complete_new_text_list):
    
    try:
        ratings = []
        for com in complete_new_text_list:

            if "supply chain" in com.lower():
                ratings.append(True)
                
               


        return any(ratings)
    except Exception as e:
        print(e)
        return False

def get_SBTP(complete_new_text_list):
    
    try:
        ratings = []
        for com in complete_new_text_list:

            if "SBTP" in com.lower():
                ratings.append(True)
                
               


        return any(ratings)
    except Exception as e:
        print(e)
        return False

def get_CDP(complete_new_text_list):
    
    try:
        ratings = []
        for com in complete_new_text_list:

            if "CDP" in com.lower():
                ratings.append(True)
                
               


        return any(ratings)
    except Exception as e:
        print(e)
        return False

def get_GRI(complete_new_text_list):
    
    try:
        ratings = []
        for com in complete_new_text_list:

            if "GRI" in com.lower():
                ratings.append(True)
                
               


        return any(ratings)
    except Exception as e:
        print(e)
        return False

def get_SASB(complete_new_text_list):
    
    try:
        ratings = []
        for com in complete_new_text_list:

            if "SASB" in com.lower():
                ratings.append(True)
                
               


        return any(ratings)
    except Exception as e:
        print(e)
        return False

def get_TCFD(complete_new_text_list):
    
    try:
        ratings = []
        for com in complete_new_text_list:

            if "TCFD" in com.lower():
                ratings.append(True)
                
               


        return any(ratings)
    except Exception as e:
        print(e)
        return False

def get_ASSURANCE(complete_new_text_list):
    
    try:
        ratings = []
        for com in complete_new_text_list:

            if "assurance" in com.lower():
                ratings.append(True)
                
               


        return any(ratings)
    except Exception as e:
        print(e)
        return False
    
metric_names = [
    "MSCI Sustainlytics",
    "Net Zero Target",
    "Interim Emission Reduction Target",
    "Renewable Electricity Target",
    "Circularity Strategy and Targets",
    "Diversity, Equity, and Inclusion Target",
    "Employee Health and Safety Audits",
    "Supply Chain Audits",
    "SBTP",
    "CDP",
    "GRI",
    "SASB",
    "TCFD",
    "Assurance"
]


metric_functions = [
    get_msci,
    get_net_zero,
    get_interim_emissions,
    get_renewable_target,
    get_circularity_target,
    get_diversity_target,
    get_employee_inclusion_target,
    get_supply_chain_target,
    get_SBTP,
    get_CDP,
    get_GRI,
    get_SASB,
    get_TCFD,
    get_ASSURANCE
]

    
def main():
    st.title("Metrics Extraction")

    uploaded_files = st.file_uploader("Upload PDF files", type="pdf", accept_multiple_files=True)
    if uploaded_files:
        df_dict = {}
        for uploaded_file in uploaded_files:
            df_dict[uploaded_file.name] = {}
            all_metrics = []
            with open(uploaded_file.name, 'wb') as file:
                file.write(uploaded_file.getbuffer())
            complete_text = ""
            with open(uploaded_file.name, 'rb') as file:
                reader = PyPDF2.PdfReader(file)
                num_pages = len(reader.pages)
                for page_num in tqdm(range(num_pages)):
                    page = reader.pages[page_num]
                    text = page.extract_text()
                    complete_text += "\line" + text
                complete_new_text_list = complete_text.split("\line")
                complete_new_text_list = [i.replace("\n","") for i in complete_new_text_list]
                for name, metric in zip(metric_names, metric_functions):
                    metric_result = metric(complete_new_text_list)
                    df_dict[uploaded_file.name][name] = str(metric_result)
                
        df = pd.DataFrame.from_dict(df_dict, orient='index')
        df = df.replace("False", ".")
        df = df.replace("True","✓")
        
        # Display DataFrame
        st.write("## Metrics Summary")
        st.write(df)
        csv = df.to_csv().encode()
        st.download_button(
            label="Download CSV",
            data=csv,
            file_name="metrics_summary.csv",
            mime="text/csv"
        )
        

if __name__ == "__main__":
    main()
