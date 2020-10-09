import pafy #importing pafy
import youtube_dl

#getting url of yoiutube video to be downloaded
url = 'https://youtu.be/7gLXKYfZPYc'
video = pafy.new(url)

#getting all available streams
streams = video.streams

#printing all available streams
for i  in streams:
	print(i)

#get best resolution ragardless of format
best = video.getbest()

print(best.resolution, best.extension)
best.download()
print('video downloaded successfully')