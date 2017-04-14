# -*- coding: utf-8 -*-
__author__ = 'Seran'

from D_functions import *
import os
import sys

reload(sys)
sys.setdefaultencoding('utf-8')


TEXT_FILE_PATH = "C:/workspaces/movie-indexer/src/"
MOVIE_FILE_PATH = "C:/workspaces/movie-indexer/movie/"
IMAGES_FILE_PATH = "C:/workspaces/movie-indexer/images/"

DO_WRITE_FILE_NAME = 'F'
DO_DOWNLOAD_FILE = 'F'
DO_EXTRACT_IMAGE = 'F'

if __name__ == "__main__":
    # yt = "https://www.youtube.com/watch?v=BzYnNdJhZQw"
    # m_name = "test1"
    yt = "https://www.youtube.com/watch?v=PRASD6J5Lfk"
    m_name = "test2"

    file_info_print(yt)

    if(DO_WRITE_FILE_NAME == 'T'):
        if(os.path.isfile(TEXT_FILE_PATH + "file_name_index.txt")):
            with open("file_name_index.txt", "a") as f:
                f.write("[ Original file name : %s ], [ Changed file name : %s ]\n" % (get_file_info(yt)['filename'], m_name))
        else:
            with open("file_name_index.txt", "w") as f:
                f.write("[ Original file name : %s ], [ Changed file name : %s ]\n" % (get_file_info(yt)['filename'], m_name))

    if(DO_DOWNLOAD_FILE == 'T'):
        # file_size : 고화질을 다운받으려면 -1, 저화질을 다운받으려면 0
        if(download_file(yt, -1, m_name, MOVIE_FILE_PATH)):
            DO_EXTRACT_IMAGE = 'T'

    if(DO_EXTRACT_IMAGE == 'T'):
         m_path = MOVIE_FILE_PATH + m_name + ".mp4"
         i_path = IMAGES_FILE_PATH + m_name + '/'
         i_name = "frame"
         f_term = 24

         if(os.path.isdir(i_path) == False):
             os.makedirs(i_path)

         video_capture(m_path, i_path, i_name, f_term, 1)