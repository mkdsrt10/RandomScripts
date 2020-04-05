import csv
import requests

header_body = ['finbank_name',
    'finbank_description',
    'finbank_logo',
    'finbank_meta_keyword',
    'product_name',
    'product_image_url',
    'product_slug',
    'popular_offer',
    'valid_till',
    'product_mini_feature',
    'offer_text',
]
header_product_info = ['Annual Fees',
    'Fees and charges',
    'Eligibility',
    'Documents Required',
    "What You'll Love",
    'Processing Time',
    'Offers',
    'Renewal Fees',
    'Documents Required']
csv_header = header_body + header_product_info
slugs = ['hdfc-bank-credit-cards', 'icici-bank-credit-cards', 'rbl-bank-credit-cards', 'indusind-bank-credit-cards', 'citibank-bank-credit-cards', 'moneytap-loan']
csv_file = "datascrap.csv"
data_mod = {}
url = 'https://api.rubique.com/demo/product/showdatabyproduct'
try:
    with open(csv_file, 'w') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=csv_header)
        writer.writeheader()
        for slugm in slugs:
            para = {'product_type': 11, 'seo_slug': slugm}
            r = requests.get(url = url, params = para)
            # print 'm'
            d = r.json()
            if slugm == 'rbl-bank-credit-cards':
                print d
            #for i in range(0, len(
            for dc in d['body']:
                for itmk in header_body:
                    data_mod[itmk] = "asa"
                    data_mod[itmk] = dc[itmk]
                for itmk in dc['product_info'].values():
                    data_mod[itmk['title']] = itmk['info_text']
                writer.writerow(data_mod)

        # for data in dict_data:
        #     writer.writerow(data)
except IOError:
    print("I/O error")
