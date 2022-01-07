import re
from pytube import YouTube 

def filterData(data,j,type):
	global choices
	i = 0
	while i < len(data):
		if(data[i][j] != type):
			data.pop(i)
		else:
			i += 1
	choices = [[],[],[]]
	for d in data:
		choices = addChoices(d[1],d[2],d[3],choices)

	return data

def addChoices(Type,Format,Res,choices):
	if(Type not in choices[0]):
		choices[0].append(Type)
	if(Format not in choices[1]):
		choices[1].append(Format)
	if(Res not in choices[2]):
		choices[2].append(Res)
	return choices
#####################################################

url = input("Enter the video link/url : ")

yt = YouTube(url)

Streams = yt.streams.filter(res=None)

data = []
choices = [[],[],[]]
for strm in Streams:
	print(strm)
	strm = str(strm)
	vTag = re.findall(".* itag=\"(\d+)\".*",strm)[0]
	vType = re.findall(".* type=\"([^\"]+)\".*",strm)[0]
	vFormat = re.findall(".*/([^\"]+)\".*",strm)[0]
	if(vType == "video"):
		vRes = re.findall(".* res=\"([^\"]+)\".*",strm)[0]
	else:
		vRes = re.findall(".* abr=\"([^\"]+)\".*",strm)[0]
	data.append((vTag,vType,vFormat,vRes))
	choices = addChoices(vType,vFormat,vRes,choices)

choice = "0"
while(int(choice) < 1 or int(choice) > len(choices[0])):
	print("\n In what type of media do you want to download this video :\n")
	
	n = 1
	for c in choices[0]:
		print(" [" + str(n) +"] " + c + "\n")
		n += 1

	choice = input(" Enter a number : ")
	if (int(choice) > 0 and int(choice) <= len(choices[0])):
		uType = choices[0][int(choice)-1]
	else:
		print("\n Unknown choice ! Please enter a number again.")

data = filterData(data,1,uType)

choice = "0"
while(int(choice) < 1 or int(choice) > len(choices[1])):
	print("\n In what format do you want to download the " + uType + " :\n")
	
	n = 1
	for c in choices[1]:
		print(" [" + str(n) +"] " + c + "\n")
		n += 1

	choice = input(" Enter a number : ")
	if (int(choice) > 0 and int(choice) <= len(choices[1])):
		uFormat = choices[1][int(choice)-1]
	else:
		print("\n Unknown choice ! Please enter a number again.")

data = filterData(data,2,uFormat)

choice = "0"
while(int(choice) < 1 or int(choice) > len(choices[2])):
	print("\n In what res/abr do you want to download the " + uType + " :\n")
	
	n = 1
	for c in choices[2]:
		print(" [" + str(n) +"] " + c + "\n")
		n += 1

	choice = input(" Enter a number : ")
	if (int(choice) > 0 and int(choice) <= len(choices[2])):
		uRes = choices[2][int(choice)-1]
	else:
		print("\n Unknown choice ! Please enter a number again.")

data = filterData(data,3,uRes)

uTag = int(data[0][0])

strmolution = yt.streams.get_by_itag(uTag)

path = input('Enter the path for download : ')

print("Downloading " + yt.title + "...")

strmolution.download(output_path=path)

print("Your video is downloaded !")
