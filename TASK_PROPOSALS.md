# Codebase Task Proposals

## 1) Typo fix task
- **Task**: Update the comment `# Step 1: Setup Entrez` to `# Step 1: Set up Entrez` for correct wording.
- **Why**: "Setup" is a noun; the verb phrase in this context should be "set up".
- **Location**: `using_efetch.py` line 5.

## 2) Bug fix task
- **Task**: URL-encode `biosample_query` before inserting it into the PubMed `esearch` URL in `search_ncbi`.
- **Why**: Queries with spaces/special characters (e.g., `single cell RNA transcriptomics`) are directly interpolated into the URL, which can produce malformed requests or inconsistent results.
- **Location**: `pubmed_scrape.py` line 7.

## 3) Documentation/comment discrepancy task
- **Task**: Align Step 2 comment and actual query term in `using_efetch.py`.
- **Why**: The comment says the script searches for *atherosclerosis RNA-Seq data*, but the code uses `search_term = "disease RNA-Seq"`; this mismatch can mislead users about script behavior.
- **Location**: `using_efetch.py` lines 8-9.

## 4) Test improvement task
- **Task**: Add unit tests for `fetch_details` that mock `requests.get` and validate missing XML field handling.
- **Why**: Current logic assumes parsed XML structure and field text availability; tests should verify fallback behavior (`"N/A"`) and study type classification logic, especially when `AbstractText`/`ArticleTitle` are absent.
- **Location**: `pubmed_scrape.py` lines 14-34.
