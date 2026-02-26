# Entrez Search Utilities

Small collection of Python scripts for querying NCBI and related bioinformatics APIs.

## Files

- `pubmed_scrape.py` – searches PubMed with E-utilities (`esearch` + `efetch`) and exports article fields to `ncbi_search_results.xlsx`.
- `using_efetch.py` – uses Biopython `Entrez` to search SRA and export metadata to `atherosclerosis_sra_metadata.xlsx`.
- `variant_search` – converts dbSNP RSIDs to chromosome/position using `myvariant`.
- `TASK_PROPOSALS.md` – suggested cleanup and improvement tasks for this repository.

## Requirements

Install Python packages:

```bash
pip install requests pandas biopython tqdm myvariant
```

## Usage

Run scripts directly:

```bash
python pubmed_scrape.py
python using_efetch.py
python variant_search
```

## Notes

- For NCBI Entrez usage, set a valid email address in `using_efetch.py`:

```python
Entrez.email = "your.email@example.com"
```

- API responses can vary by record; some fields may be missing.
- Network access is required for all scripts.
