from bs4 import BeautifulSoup
import requests
import re
import pickle
import feedparser
from time import sleep
#next goal - need to make regex patterns that can match all different types of typos in names
items_dict = {
    'Item\\.? 1\\.01': 'Entry into a Material Definitive Agreement',
    'Item 1\\.02\\.': 'Termination of a Material Definitive Agreement',
    'Item 1\\.03\\.': 'Bankruptcy or Receivership',
    'Item 1\\.04\\.': 'Mine Safety - Reporting of Shutdowns and Patterns of Violations',
    'Item 2\\.01\\.': 'Completion of Acquisition or Disposition of Assets',
    'Item 2\\.02\\.': 'Results of Operations and Financial Condition',
    'Item 2\\.03\\.': 'Creation of a Direct Financial Obligation or an Obligation under an Off-Balance Sheet Arrangement of a Registrant',
    'Item 2\\.04\\.': 'Triggering Events That Accelerate or Increase a Direct Financial Obligation or an Obligation under an Off-Balance Sheet Arrangement',
    'Item 2\\.05\\.': 'Costs Associated with Exit or Disposal Activities', 'Item 2\\.06\\.': 'Material Impairments',
    'Item 3\\.01\\.': 'Notice of Delisting or Failure to Satisfy a Continued Listing Rule or Standard; Transfer of Listing',
    'Item 3\\.02\\.': 'Unregistered Sales of Equity Securities',
    'Item 3\\.03\\.': 'Material Modification to Rights of Security Holders',
    'Item 4\\.01\\.': "Changes in Registrant's Certifying Accountant",
    'Item 4\\.02\\.': 'Non-Reliance on Previously Issued Financial Statements or a Related Audit Report or Completed Interim Review',
    'Item 5\\.01\\.': 'Changes in Control of Registrant',
    'Item 5\\.02\\.': 'Departure of Director or Certain Officers; Election of Directors; Appointment of Certain Officers; Compensatory Arrangements of Certain Officers',
    'Item 5\\.03\\.': 'Amendments to Articles of Incorporation or Bylaws; Change in Fiscal Year',
    'Item 5\\.04\\.': "Temporary Suspension of Trading Under Registrant's Employee Benefit Plans",
    'Item 5\\.05\\.': "Amendment to Registrant's Code of Ethics, or Waiver of a Provision of the Code of Ethics",
    'Item 5\\.06\\.': 'Change in Shell Company Status',
    'Item 5\\.07\\.': 'Submission of Matters to a Vote of Security Holders',
    'Item 5\\.08\\.': 'Shareholder Director Nominations',
    'Item 6\\.01\\.': 'ABS Informational and Computational Material', 'Item 6\\.02\\.': 'Change of Servicer or Trustee',
    'Item 6\\.03\\.': 'Change in Credit Enhancement or Other External Support',
    'Item 6\\.04\\.': 'Failure to Make a Required Distribution', 'Item 6\\.05\\.': 'Securities Act Updating Disclosure',
    'Item 7\\.01\\.': 'Regulation FD Disclosure',
    'Item 8\\.01\\.': 'Other Events', 'Item 9\\.01\\.?': 'Financial Statements and Exhibits'
}


#open file with stored item dictionary
#with open('file_name.pickle','wb') as handle:
     #pickle.dump(items_dict,handle,protocol=pickle.HIGHEST_PROTOCOL)
with open('file_name.pickle', 'rb') as handle:
    unserialized_data = pickle.load(handle)

locations = []
url = 'https://www.sec.gov/Archives/edgar/data/1366527/000110465919046990/a19-17634_18k.htm'
    #'https://www.sec.gov/Archives/edgar/data/51143/000155837019006914/ibm-20190802x8k.htm'


r = requests.get(url)
soup = BeautifulSoup(r.text,'html.parser')
new = re.sub(r'\s+'," ",soup.text)

for key in items_dict.keys():
    found = re.search(key +"\s?"+items_dict[key], new)
    if found:
        locations.append(found.span()[0])

signature = re.search(r'SIGNATURE',new).span()[0]

locations.append(signature)
print(locations)
for i in range(len(locations)-1):
    start = locations[i]
    end = locations[i + 1]
    print(new[start:end])



