import requests
import xml.etree.ElementTree as ET
import pandas as pd

# Function to search NCBI using esearch
def search_ncbi(biosample_query):
    esearch_url = f"https://eutils.ncbi.nlm.nih.gov/entrez/eutils/esearch.fcgi?db=pubmed&term={biosample_query}&retmax=100&retmode=xml"
    response = requests.get(esearch_url)
    root = ET.fromstring(response.content)
    pmids = [id_elem.text for id_elem in root.findall('.//Id')]
    return pmids

# Function to fetch detailed info using efetch
def fetch_details(pmid):
    efetch_url = f"https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=pubmed&id={pmid}&retmode=xml"
    response = requests.get(efetch_url)
    root = ET.fromstring(response.content)
    
    title = root.find('.//ArticleTitle').text if root.find('.//ArticleTitle') is not None else "N/A"
    abstract = root.find('.//AbstractText').text if root.find('.//AbstractText') is not None else "N/A"
    methods = root.find('.//Methods').text if root.find('.//Methods') is not None else "N/A"
    
    # Example logic to identify study types and extract data links
    study_type = "Disease vs Control" if "disease" in abstract.lower() and "control" in abstract.lower() else "Other"
    data_links = "N/A"  # Placeholder for data extraction logic
    
    return {
        "PMID": pmid,
        "Title": title,
        "Abstract": abstract,
        "Methods": methods,
        "Study Type": study_type,
        "Data Links": data_links
    }

# Main function to process search and extraction
def process_ncbi_search(biosample_query):
    pmids = search_ncbi(biosample_query)
    results = []
    
    for pmid in pmids:
        details = fetch_details(pmid)
        results.append(details)
    
    df = pd.DataFrame(results)
    df.to_excel("ncbi_search_results.xlsx", index=False)
    print("Results saved to ncbi_search_results.xlsx")

# Example usage
biosample_query = "single cell RNA transcriptomics"
process_ncbi_search(biosample_query)
