# -*- coding: utf-8 -*-
__author__ = 'Seran'

from pytube import YouTube
import cv2

def file_info_print(youtube_url):
    yt = YouTube(youtube_url)
    print('===  File Name  ===')
    print(yt.filename)
    print('===   File information  ===')
    print(yt.get_videos())

def get_file_info(youtube_url):
    yt = YouTube(youtube_url)
    d = {
        'filename' : yt.filename,
        'videos' : yt.get_videos()
    }
    return d

def download_progress(_bytes_received, file_size, start):
    p = round(_bytes_received / (file_size * 1.0) * 100, 3)
    if(p % 10 == 0):
        print(str(int(p))+'%')

def download_finish(path):
    print('===  Download movie file finish  ===')
    p = str(path).replace("\\", "/")
    print(p)

def download_file(youtube_url, file_size, file_name, file_path):

    yt = YouTube(youtube_url)

    if len(yt.filter('mp4')) > 0:
        yt.set_filename(file_name)

        resolution = (''.join(str(yt.filter('mp4')[file_size]))).split('-')[1].strip()
        video = yt.get('mp4', resolution)

        print('===  Download movie file  ===')
        print('(mp4, ' + resolution + ') : ' + yt.filename)

        print('===  Downloading...  ===')
        video.download(file_path, on_progress=download_progress, on_finish=download_finish, force_overwrite=True)

        return True

    else:
        print('===  mp4 파일만 다운 가능 합니다  ===')
        return False

def video_capture(movie_file_path, image_file_path, image_name, frame_term, count):
    vidcap = cv2.VideoCapture(movie_file_path)
    f_total_num = int(vidcap.get(7))

    try:
        print("===  Extract image start  ===")

        while(vidcap.isOpened()):
            if(f_total_num == int(vidcap.get(1))):
                print("===  Extract image finish  ===")
                break

            ret, image = vidcap.read()
            if(int(vidcap.get(1)) % frame_term == 0):
                cv2.imwrite(image_file_path + image_name + "%d.jpg" % count, image)
                count += 1

        vidcap.release()
        return True
    except Exception as e:
        print("===  Extract image error  ===")
        print(e)
        vidcap.release()
        return False