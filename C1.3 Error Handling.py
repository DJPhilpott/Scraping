from urllib.request import urlopen
from urllib.error import HTTPError
from bs4 import BeautifulSoup

def getTitle(url):
	#Can get a 404 from the server, or not find the server at all
	#In the first case, will receive an HTML error that can be caught as an except
	#In the second case, can check to see if the attributes of the created object are Null
	try:
		html = urlopen(url)
	except HTTPError as e:
		print(e)
		return None
		#then return null, break, or do some kind of Plan B
		#If there is not a return or break in the except case, need an else case to continue

	#If page is pulled successfully, still might not get expected content, so check desired tags to see if they exist
	try:
		bsObj = BeautifulSoup(html.read())
		title = bsObj.body.h1
	except AttributeError as e:
		return None
	return title


title = getTitle("http://www.pythonscraping.com/exercises/exercise1.html")
if title == None:
	#check if no title could be pulled
	#Due to other error checking already occuring, this is most likely due to not being able to contact server at all
	print("Title could not be found")
else:
	print(title)


#Efficient form to build a cascade of functions that perform generic tasks and exception handling


