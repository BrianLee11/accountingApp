# EDGAR_API_call_test.py
# testing

# I want to call EDGARD_API
# https://www.sec.gov/search-filings/edgar-application-programming-interfaces
import requests

headers = {
    'User-Agent': 'Jane Doe CompanyX (jane.doe@example.com)'  # Update with your info
}

cik = '0000320193'
url = f'https://data.sec.gov/submissions/CIK{cik}.json'

response = requests.get(url, headers=headers)
data = response.json()

ten_q_filings = [
    filing for filing in data['filings']['recent']['form']
    if filing == '10-Q'
]

print(f"Found {len(ten_q_filings)} 10-Q filings.")
filings = data['filings']['recent']

ten_q_data = []

for i, form in enumerate(filings['form']):
    if form == '10-Q':
        accession_number = filings['accessionNumber'][i].replace('-', '')
        filing_date = filings['filingDate'][i]
        document_url = f"https://www.sec.gov/Archives/edgar/data/{int(cik)}/{accession_number}/index.json"

        ten_q_data.append({
            'accession_number': filings['accessionNumber'][i],
            'filing_date': filing_date,
            'document_url': document_url
        })

for entry in ten_q_data:
    print(entry)
