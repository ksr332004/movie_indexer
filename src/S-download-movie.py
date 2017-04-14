# -*- coding: utf-8 -*-
__author__ = 'Seran'

from pytube import YouTube

def file_info_print(yt):
    # 다운받는 영상 이름
    print('===  File Name  ===')
    print(yt.filename)
    # 다운받는 영상에 대한 정보 출력
    print('===   File Info. [get_videos()]  ===')
    print(yt.get_videos())
    # 해당 영상에 대한 모든 정보를 출력
    print('===   File Info. [videos]  ===')
    print(yt.videos)

def specific_file_info_print(yt):
    # 특정 확장자에 대한 영상 정보를 추출
    print("===  Select '.flv' file  ===")
    print(yt.filter('flv'))
    # 특정 확장자에 대한 영상 정보 중 최고 화질 영상정보를 추출
    print("===  Select specific '.mp4' file  ===")
    print(yt.filter('mp4')[-1])
    # 특정 화질에 대한 영상정보를 추출
    print("===  Select '480p' file  ===")
    print(yt.filter(resolution='480p'))

def download_progress(_bytes_received, file_size, start):
    p = round(_bytes_received / (file_size * 1.0) * 100, 3)
    if(p % 10 == 0):
        print(str(int(p))+'%')

def download_finish(path):
    print('===  Finish  ===')
    print(str(path).replace("\\", "/"))


# URL 경로 설정
yt = YouTube("https://www.youtube.com/watch?v=PRASD6J5Lfk")

#file_info_print(yt)
#specific_file_info_print(yt)

if len(yt.filter('mp4')) > 0:
    # 다운받는 영상이름 설정
    yt.set_filename('test2')

    s = (''.join(str(yt.filter('mp4')[-1]))).split('-')[1].strip()

    # 특정 확장자와 해상도를 설정한 파일을 변수에 넣어줌
    #video = yt.get('mp4', '720p')
    video = yt.get('mp4', s)

    print('===  Download movie file  ===')
    print('(mp4, ' + s + ') : ' + yt.filename)
    print('===  Downloading...  ===')
    # 해당 영상을 사용자가 지정한 경로에 저장
    video.download('../movie/', on_progress=download_progress, on_finish=download_finish, force_overwrite=True)