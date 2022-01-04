from pytube import YouTube 


url = input("Enter the video link/url : ")

yt = YouTube(url)

resolutions = yt.streams.filter(res=None)

for res in resolutions:
	print("1 - " + str(res))


resolution = yt.streams.get_by_itag(22)

path = input('Enter the path for download : ')

print("Downloading " + yt.title + "...")

resolution.download(output_path=path)

print("Your video is downloaded !")