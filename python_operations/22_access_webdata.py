import pandas as pd
import requests
from io import StringIO

csv_link="https://www.stats.govt.nz/assets/Uploads/Annual-enterprise-survey/Annual-enterprise-survey-2024-financial-year-provisional/Download-data/annual-enterprise-survey-2024-financial-year-provisional.csv"

response= requests.get(csv_link)
response.raise_for_status() # exception handle

data_source=StringIO(response.text)

data_frame=pd.read_csv(data_source)
print(data_frame)


# to run the file - python E:\Python-DSA\python_operations\22_access_webdata.py