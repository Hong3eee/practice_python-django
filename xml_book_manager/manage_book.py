import xml.etree.ElementTree as ET
import sys


fd = None
xmldoc = None

def printMenu():
	global xmldoc
	while True:
	
		print("\nWelcome! Book Manager Program (xml Version)")
		print("---------Menu---------")
		print("Load xml: l")
		print("Print dom to xml: p")
		print("Quit program: q")
		print("Print book list: b")
		print("Add new book: a")
		print("Search book title: s")
#	print("make HTML: m")
		print("-----------------------")
	
		index = str(input("select menu what you want: "))
		
		if index == 'l':
			xmldoc = loadXml()
		elif index =='p':
			ET.dump(xmldoc)
		elif index =='q':
			sys.exit(0)
		elif index =='b':
			printBooklist()
		elif index =='a':
			addBook()
		elif index =='s':
			searchBook()
#		elif index =='m':
#			pass

		
def loadXml():
	filename = str(input("input file name: "))
	global fd

	fd = open(filename) # 파싱할 파일 받음

	try:
		doc = ET.parse(fd) # xml 파싱
	except Exception:
		print("parse Error Occured!")
		return None
	else:
		return doc

def printBooklist():
	global xmldoc
	root = xmldoc.getroot()

	for node in root.iter("book"):
		print("title ",node.find("title").text)

def addBook():
	global xmldoc
	root = xmldoc.getroot()

	bookelement = ET.Element("book")	# 하위 book Element생성
	
	bookISBN = str(input("insert ISBN :"))
	bookName = str(input("insert BookName :"))
	
	bookelement.set("ISBN",bookISBN)
	title = ET.SubElement(bookelement,"title")
	title.text = bookName

	indent(bookelement)
	root.append(bookelement)	# 생성한 Element 추가

	ET.dump(root)

def indent(elem, level=0):
	i = "\n" + level*"  "
	if len(elem):
		if not elem.text or not elem.text.strip():
			elem.text = i + "  "
		if not elem.tail or not elem.tail.strip():
			elem.tail = i
		for elem in elem:
			indent(elem, level+1)
		if not elem.tail or not elem.tail.strip():
			elem.tail = i
	else:
		if level and (not elem.tail or not elem.tail.strip()):
			elem.tail = i

def searchBook():
	global xmldoc
	root = xmldoc.getroot()
	string = str(input("input string you want to search : "))
	temp =[]

	for node in root.iter("book"):
		if node.find("title").text.find(string)>=0:
			temp.append((node.get("ISBN"),node.find("title").text))

	for isbn,title in temp:
		print("ISBN : ",isbn,"Title : ",title)
	
if __name__=='__main__':
	printMenu()
