import re
from pytube import YouTube 

def filterData(data,type):
	i = 0
	while i < len(data):
		if(data[i][1] != type):
			data.pop(i)
		else:
			i += 1
	return data

url = input("Enter the video link/url : ")

yt = YouTube(url)

resolutions = yt.streams.filter(res=None)

data = []
for res in resolutions:
	print(res)
	res = str(res)
	vTag = re.findall(".* itag=\"(\d+)\".*",res)[0]
	vMime = re.findall(".* mime_type=\"([^\"]+)\".*",res)[0]
	vType = vMime[:5]
	vFormat = vMime[6:]
	if(vType == "video"):
		vRes = re.findall(".* res=\"([^\"]+)\".*",res)[0]
	else:
		vRes = re.findall(".* abr=\"([^\"]+)\".*",res)[0]
	data.append((vTag,vType,vFormat,vRes))

choice = ""
while(choice != "1" and choice != "2"):
	print("\n In what type of media do you want to download this video :\n")
	
	n = 1
	for d in data:
		if(d[1] == "video"):
			print(" [" + str(n) +"] Video\n")
			n += 1
			break
	for d in data:
		if(d[1] == "audio"):
			print(" [" + str(n) +"] Audio\n")
			break

	choice = input(" Enter a number : ")
	if choice == "1":
		uType = "video"
	elif choice == "2":
		uType = "audio"
	else:
		print("\n Unknown choice ! Please enter the choice again.")

data = filterData(data,uType)
print(data)

resolution = yt.streams.get_by_itag(22)

path = input('Enter the path for download : ')

print("Downloading " + yt.title + "...")

resolution.download(output_path=path)

print("Your video is downloaded !")
