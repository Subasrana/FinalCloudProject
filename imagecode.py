import time
from datetime import datetime
from goprocam import GoProCamera, constants

gopro = GoProCamera.GoPro()

def takePhoto():
 ct = round(time.time() * 1000)
 #print("Image capture start time: "+str( ct))
 gopro.take_photo(timer=1)
 
 gopro.downloadLastMedia()
 
 filename = gopro.getMediaInfo(option = "file")
 #print("Filename: "+filename)
 size = gopro.getMediaInfo(option = "size")
 #print("File Size: "+size)
 
 dt = round(time.time() * 1000)
 #print("Download Image Time: " +str(dt))
 
 timedelay = dt - ct
 print("Latency: " +str(timedelay)+ " ms")
 
 now = datetime.now()
 print('Current DateTime:', now)
 
 

takePhoto()

#gopro.listMedia(True)
