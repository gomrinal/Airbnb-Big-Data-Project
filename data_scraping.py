from bs4 import BeautifulSoup
import urllib.request
import re
import urllib.request
from os.path import basename
from os.path import dirname
import time


r = urllib.request.urlopen("http://insideairbnb.com/get-the-data.html").read()
soup = BeautifulSoup(r, "lxml")

# show rows of all the tables
tables = soup.findAll('table')[1]
rows = tables.findAll('tr')
row_list = list()
for tr in rows:
    td = tr.find_all('td')
    row = [i.text for i in td]
    row_list.append(row)
#print(row_list)

#show html doms (table) based on the class tag
regex = re.compile('^vancouver')
content_lis = soup.find_all('table', attrs={'class': regex})
#print(content_lis)


table = content_lis[0]
# There are 148 rows for vancouver
len(table.find_all('tr'))

table.findAll('a',attrs={'href': re.compile("^http")})

#find the a tags -147
len(table.findAll('a',attrs={'href': re.compile("^http")}))



file = open('parsed_vancouver_data.txt', 'w')
for link in table.findAll('a',attrs={'href': re.compile("^http")}):
    link_a = link['href']
    print(link_a)
    download_url = link_a
    file_name = basename(link_a)
    print(file_name)
    dir_name = dirname(link_a)
    print(dir_name)
    split_param = "http://data.insideairbnb.com/canada/bc/vancouver/"
    split_url = link_a.split("/")
    new_file_name_list = [split_url[-3], split_url[-2], split_url[-1]]
    new_file_name = "-".join(new_file_name_list)
    print(split_url)
    print(new_file_name)
    urllib.request.urlretrieve(download_url, new_file_name)
    content_lis_link = str(link)
    file.write(content_lis_link)
    file.flush()
file.close()
time.sleep(1) #pause the code for a sec

# to find the pwd
# %pwd 
# http://data.insideairbnb.com/canada/bc/vancouver/


