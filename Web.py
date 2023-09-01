#Importing the required libraries
import pandas as pd
import requests
from bs4 import BeautifulSoup

#We are using these headers so that the server does not block our request.

headers={'User-Agent':'Mozilla/5.0 (Windows NT 6.3; Win 64 ; x64) Apple WeKit /537.36(KHTML , like Gecko) Chrome/80.0.3987.162 Safari/537.36'}

#Now hitting the Url

url = 'https://www.ambitionbox.com/list-of-companies?page=1'
#This will give us the whole webpage as html code and now we can extract the data that we need
webpage = requests.get(url, headers=headers).text


Soup = BeautifulSoup(webpage, 'lxml')
#Now extratcing the data that we need. (In this case we need all the names of the companies and their rating and reviews)
company  = Soup.find_all('div', class_='companyCardWrapper__companyDetails')
#Here we have got the main company div container where all the details of the compnay are stored.
print(len(company))

#Now we will use this compnay div container to find the names, rating and reviews of the various companies.

names =[]
rating = []
reviews = []

#Traversing thorugh the company's list
for i in company:
    names.append((i.find('h2').text.strip()))
    rating.append((i.find('span', class_='companyCardWrapper__companyRatingValue').text.strip()))
    reviews.append((i.find('span', class_='companyCardWrapper__interLinking').text.strip()))
    
#Printing all the data that we extracted from the webtie.
print(names)
print(rating)
print(reviews)
