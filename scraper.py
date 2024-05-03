from bs4 import BeautifulSoup
import requests
import csv
import pandas as pd

target=requests.get("https://en.wikipedia.org/wiki/List_of_largest_companies_in_the_United_States_by_revenue")
soup=BeautifulSoup(target.text, 'html.parser')



table=soup.find("table", attrs={"class":"wikitable sortable"})

titles=table.findAll("th")
titles_text=[title.text.strip() for title in titles]

df=pd.DataFrame(columns=titles_text)

data=table.findAll('tr')
for row in data[1:]:
    row_data=row.find_all('td')
    individual_row_data=[data.text.strip()for data in row_data]
    length=len(df)
    df.loc[length]=individual_row_data


print(df)


df.to_csv(r'c:\Users\User\Desktop\Samsaxuri\SCRAPERS\Scraper\amazon_data.csv', index=False)






