"""
TerminalPlay v 1.0.0

Play video in terminal

Author : Merwin
"""



from moviepy.editor import *
from sty import bg
import platform
import playsound
import threading
import hashlib
import time
import rich
import cv2
import os



class TerminalPlay:

    def __init__(self, file, div=0.5):
        """
        file : str - Name of the video file
        div : float - Reducing the size of video to make it fit in the terminal
        """
        self.file_og = file
        self.fps =  VideoFileClip(self.file_og).fps
        self.div = div
        self.file_hash = self.hash_file(file)
        self.os = platform.system()

        self.max_threads = 30
        self.cur_threads = 0
        
        self.file = "."+self.file_hash+"." +str(div)
        self.c = 0
        
        if not os.path.exists(self.file):
            self.generate_playable()
    


    def generate_playable(self):

        rich.print("[blue]GENERATING PLAYABLE:: THIS MAY TAKE CPU (Will be only ran once for a video)[/blue]")
        
        os.system("mkdir "+self.file)

        a = VideoFileClip(self.file_og)
        b = a.resize(self.div)
        b.write_videofile("."+self.file_og)
        b.audio.write_audiofile(f".{self.file_og}_audio.mp3")

        
        cap = cv2.VideoCapture("."+self.file_og)
  
        if (cap.isOpened()== False):
            print("Error opening video file")
        
        c = 0
        # Read until video is completed
        while(cap.isOpened()):
            ret, frame = cap.read()
            if ret == True:
                while self.cur_threads == self.max_threads:
                    time.sleep(0.05)
                t = threading.Thread(target=self._write_frame, args=(frame,c,))
                t.start()
                self.cur_threads += 1

                c += 1
            else:
                break
                
        cap.release()

        os.remove("."+self.file_og)


    def _write_frame(self, frame, c):
        if self.os == "windows":
            f = open(self.file+f"\{c}", "w")
        else:
            f = open(self.file+f"/{c}", "w")

        f.write(self.print_image(frame))
        f.close()
        self.cur_threads -= 1 


    def play_audio(self):
        try:
            playsound.playsound(f".{self.file_og}_audio.mp3")
            # self.media = vlc.MediaPlayer(f".{self.file_og}_audio.mp3",)
            # if self.media != None:
            #     self.media.play()
        except:
            a = VideoFileClip(self.file_og)
            a.audio.write_audiofile(f".{self.file_og}_audio.mp3")
            playsound.playsound(f".{self.file_og}_audio.mp3")
            # self.media = vlc.MediaPlayer(f".{self.file_og}_audio.mp3",)
            # if self.media != None:
            #     self.media.play()


    def get_frame(self):
            try:
                if self.os == "windows":
                    file = open(f'{self.file}\{c}', 'r')     
                else:
                    file = open(f'{self.file}/{c}', 'r')     
                d = file.read()
                file.close()
                c += 1
                return d
            except:
                return None 


    def reset_get_frame(self):
        self.c = 0


    def print_image(self, frame):
        final_text = ""
        txt = " " 

        for y in frame:
            for x in y:
                if list(x) != [0, 0, 0]:
                    final_text += f"{bg(x[2], x[1], x[0])}{txt}{bg.rs}"
                else:
                    final_text += txt
            final_text += "\n"

        return final_text



    def play(self):
        """
        Plays the video :]
        """
        a = threading.Thread(target=self.play_audio)
        a.daemon = True
        a.start()
        z = 1/self.fps

        for frame in os.listdir(self.file):

            z_1 = time.time()
            if self.os == "windows":
                file = open(f'{self.file}\{frame}', 'r')     
            else:
                file = open(f'{self.file}/{frame}', 'r')     
            d = file.read()
            file.close()
            print(d)
            z_2 = time.time()
            try:
                time.sleep(z-(z_2-z_1))
            except:
                pass
            os.system("clear")
        
        # try:
        #     self.media.stop()
        # except:
        #     pass

    def hash_file(self, filename):
        # make a hash object
        h = hashlib.sha1()

        # open file for reading in binary mode
        with open(filename,'rb') as file:

             # loop till the end of the file
            chunk = 0
            while chunk != b'':
                # read only 1024 bytes at a time
                chunk = file.read(1024)
                h.update(chunk)

        # return the hex representation of digest
        return h.hexdigest()








def main():
    tp = TerminalPlay("test.mp4", div=0.4)    
    tp.play()



if __name__ == "__main__":
    main()
