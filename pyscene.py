import scenedetect
import subprocess

videopath='test.mp4'
scenepath='./scene'

subprocess.call('scenedetect -i %s -o %s detect-content list-scenes  save-images -n 1' % (videopath,scenepath))