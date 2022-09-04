from bs4 import BeautifulSoup
import requests
url=("https://www.regexsoftware.com/")
data = requests.get(url).text
soup = BeautifulSoup(data,"lxml")
#print(soup.prettify)
for div_tag in soup.find_all("div",{"class":"elementor-element elementor-element-9ba7258 elementor-column elementor-col-25 elementor-top-column"}):
    for div_data in div_tag.find_all("div",{"class":"elementor-heading-title elementor-size-default"}):
        print(div_data) 
