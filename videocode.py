from goprocam import GoProCamera, constants
import time
from datetime import datetime

gopro = GoProCamera.GoPro()

def make_video():
 ct = round(time.time() * 1000)
 gopro.shoot_video(duration = 120)
 gopro.downloadLastMedia(custom_filename = "120sec_24fps.MP4")
 print("120sec_24fps.MP4")
 filename = gopro.getMediaInfo(option = "file")
 #print("Filename: "+filename)
 size = gopro.getMediaInfo(option = "size")
 #print("File Size: "+size) 
 dt = round(time.time() * 1000) 
 timedelay = dt - ct
 print("Latency: " +str(timedelay)+ " ms")
 now = datetime.now()
 print('Current DateTime:', now)
 #gopro.overview()
 res = gopro.parse_value("video_res", gopro.getStatus(constants.Status.Settings, constants.Video.RESOLUTION))
 print("Current Video Resolution: " + res)
 fr = gopro.parse_value("video_fr", gopro.getStatus(constants.Status.Settings, constants.Video.FRAME_RATE))
 print("Current video Framerate: " + fr)
 
make_video()

