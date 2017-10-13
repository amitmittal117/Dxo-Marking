import bs4
import re
from urllib import urlopen as uReq
from bs4 import BeautifulSoup as soup
from openpyxl import Workbook
book = Workbook()
sheet = book.active

my_url = 'https://www.dxomark.com/google-pixel-2-reviewed-sets-new-record-smartphone-camera-quality/'
my_url = 'https://www.dxomark.com/apple-iphone-8-plus-reviewed-best-smartphone-camera-weve-ever-tested/'
# my_url = 'https://www.dxomark.com/samsung-galaxy-note-8-best-smartphone-zoom/'
uClient = uReq(my_url)
page_html = uClient.read()
uClient.close()
page_soup = soup(page_html, "html.parser")
containers_outer_div = page_soup.findAll("div",{"class":"scoreValue"})
containers_name_div = page_soup.findAll("h1",{"class":"entry-title"})
print containers_name_div[-1].string
count=0
# myphone = my_url.split("https://www.dxomark.com/")[-1].split("-reviewed")[0].replace('-',' ')
# print myphone
pre=""
for marking in containers_outer_div:
	if count == 1:
		pre = "Base Rating: "
	elif count == 2:
		pre = "Photo Rating: "
	elif count == 3:
		pre = "Video Rating: "
	if count !=0:
		print pre+" "+containers_outer_div[count].string
	count=count+1