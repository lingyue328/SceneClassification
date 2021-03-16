# 22岁了，人生三分之一过去了---刚取消托管的小朋友。
scene classification   
Modification on https://github.com/GKalliatakis/Keras-VGG16-places365  
Download model from the urls, and ready to go.  
- python vgg16_places_365.py  

Result is a txt file， top 5 classification of each picture.  
Use classify.py can move pics to its category folder.  
  
Others:
test.py cut the video based on critical frame.  
pyscene.py Extract all frames from a video.  
places365 Folder contains files to do scene classification.  
classify.py Move pics to its folder based on classification result.  
  
    
    
  
场景分类  
在https://github.com/GKalliatakis/Keras-VGG16-places365 基础上  
进行了修改和整理了环境配置  
下载模型，然后就可以跑了   
- python vgg16_places_365.py  

结果是txt文件，每个图片的前五类别。  
用classify.py 可以把图片按文件夹分类。  
    
QAQ 找了好久场景分类的与训练模型
  
其它文件：
test.py 是根据关键帧密度剪切视频    
pyscene.py 是提取视频中所有的场景图片  
places365 是进行场景分类的文件夹  
classify.py 是根据识别的结果将图片移动到对应的文件夹中  

