import av
import av.datasets
import subprocess
import cv2

#利用pyav获取视频中的关键帧的帧号
videopath='test.mp4'
container1 = av.open(videopath)
container2 = av.open(videopath)
# Signal that we only want to look at keyframes.
stream = container1.streams.video[0]
stream.codec_context.skip_frame = 'NONKEY'

Key_Frame=[]
Key_Frame_time=[]
Key_Frame_time_1=[]

time=60
max=0
location=0

Pts=abs(next(container2.decode(video=0)).pts-next(container2.decode(video=0)).pts)

for frame in container1.decode(stream):
    Key_Frame.append(int(frame.pts/Pts))


#利用opencv获取视频的帧率


video = cv2.VideoCapture(videopath)
fps = video.get(cv2.CAP_PROP_FPS)
print("Frames per second using video.get(cv2.CAP_PROP_FPS) : {0}".format(fps))

video.release()

time_fps=time*fps

'''#将关键帧的帧序列号转换为时间
for i in Key_Frame:
    Key_Frame_time.append('{0:02d}:{1:02d}:{2:02d}{3:.3f}'.format(int(i / (3600 * fps)),int(i / (60 * fps) % 60),int(i / fps % 60),(i % fps*1/fps)))
for i in Key_Frame_time:
    list_str=list(i)
    list_str.pop(8)
    list_str=''.join(list_str)
    Key_Frame_time_1.append(list_str)
'''

#找出关键帧最密集的一分钟的起始帧号
for i in Key_Frame:
    begin=i
    last=i+time_fps
    index=Key_Frame.index(i)
    a=0
    while begin<last and index<len(Key_Frame)-1:
        a+=1
        index+=1
        begin=Key_Frame[index]
    if a>=max:
        max=a
        location=Key_Frame.index(i)
print(Key_Frame[location])


'''#将视频按关键帧所在的时间点每秒进行切分
for i in Key_Frame_time_1:
    start=i
    length='00:00:01'
    Index=Key_Frame_time_1.index(i)
    subprocess.call('ffmpeg -ss %s -i test.mp4 -t %s -c:v libx264 -c:a aac -strict experimental -b:a 96k E:\\video\\%s.mp4' % (start, length, Index))
'''

#将起始帧号转换为起始时间
begin=Key_Frame[location]
time_begin='{0:02d}:{1:02d}:{2:02d}{3:.3f}'.format(int(begin / (3600 * fps)),int(begin / (60 * fps) % 60),int(begin / fps % 60),(begin % fps*1/fps))
time_begin_1=list(time_begin)
time_begin_1.pop(8)
time_begin_1=''.join(time_begin_1)

#对视频进行切分
length='00:01:00'
subprocess.call('ffmpeg -ss %s -t %s -accurate_seek -i %s -codec copy  -avoid_negative_ts 1 02.mp4' % (time_begin_1,length,videopath))
