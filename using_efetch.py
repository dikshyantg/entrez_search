from Bio import Entrez
import pandas as pd
from tqdm import tqdm  # Optional: to show progress

# Step 1: Setup Entrez
Entrez.email = "your.email@example.com"  # Replace with your email

# Step 2: Search SRA database for atherosclerosis RNA-Seq data
search_term = "disease RNA-Seq"
handle = Entrez.esearch(db="sra", term=search_term, retmax=100)  # Adjust retmax for more results
record = Entrez.read(handle)
handle.close()

# Get list of SRA IDs
sra_ids = record["IdList"]
print(f"Found {len(sra_ids)} records related to {search_term}")

# Step 3: Fetch metadata for each SRA record
sra_metadata_list = []

for sra_id in tqdm(sra_ids, desc="Fetching SRA metadata"):
    handle = Entrez.efetch(db="sra", id=sra_id, rettype="xml")
    sra_record = Entrez.read(handle)
    handle.close()
    
    # Extract relevant fields from SRA record
    sra_metadata = {
        "SRA_ID": sra_id,
        "Title": sra_record['EXPERIMENT_PACKAGE_SET']['EXPERIMENT_PACKAGE'][0]['EXPERIMENT']['TITLE'],
        "Study_Abstract": sra_record['EXPERIMENT_PACKAGE_SET']['EXPERIMENT_PACKAGE'][0]['STUDY']['DESCRIPTOR']['STUDY_ABSTRACT'],
        "Organism": sra_record['EXPERIMENT_PACKAGE_SET']['EXPERIMENT_PACKAGE'][0]['EXPERIMENT']['DESIGN']['SAMPLE_DESCRIPTOR']['TAXON_ID'],
        "Platform": sra_record['EXPERIMENT_PACKAGE_SET']['EXPERIMENT_PACKAGE'][0]['PLATFORM']['ILLUMINA']['INSTRUMENT_MODEL'],
        "Library_Strategy": sra_record['EXPERIMENT_PACKAGE_SET']['EXPERIMENT_PACKAGE'][0]['EXPERIMENT']['DESIGN']['LIBRARY_DESCRIPTOR']['LIBRARY_STRATEGY']
    }
    
    sra_metadata_list.append(sra_metadata)

# Step 4: Convert to pandas DataFrame
sra_metadata_df = pd.DataFrame(sra_metadata_list)

# Step 5: Save DataFrame to Excel
output_file = "atherosclerosis_sra_metadata.xlsx"
sra_metadata_df.to_excel(output_file, index=False)

print(f"Metadata successfully saved to {output_file}")
