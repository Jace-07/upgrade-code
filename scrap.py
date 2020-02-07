import lxml.etree
import requests

#target location

url = input('Enter Target url ~> ')

#get the page

page = requests.get(url)


#parse it

tree = lxml.etree.fromstring(page.content)

var_xpath = '//a[text()="link"]/@href'

theXPath = var_xpath #input('enter xpath ~> ')

#grab all of them

resultList = tree.xpath(theXPath)

#now grab one of those links

#page2 = requests.get(resultList[0])

# and dump the headers for this link

print(resultList.headers)
