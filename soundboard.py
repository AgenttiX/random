"""
Soundboard

Created by Mika "AgenttiX" Mäki at Assembly Summer 2016
"""

import tkinter
import vlc
import os
import time
import threading
# import objgraph


class Soundboard:
    def __init__(self):

        # INSERT SOUND DATA HERE (and rememeber the commas)
        self.__sounds = [
            # ["Soundname", "soundfile.mp3"],
            ["Pling", "pling.mp3"],
            ["Siren", "siren.mp3"],
            ["Song", "song.flac"]
        ]

        self.__stopall = False

        self.__cwd = os.getcwd()

        self.__mainWindow = tkinter.Tk()
        self.__mainWindow.title("Soundboard")

        for index, sound in enumerate(self.__sounds):
            button = tkinter.Button(self.__mainWindow, text=sound[0], command=lambda lsound = sound[1]: self.create_thread(lsound))
            button.grid(row=index, column=0, sticky="w")

        self.__mainWindow.mainloop()

        self.__stopall = True
        time.sleep(0.5)

    def create_thread(self, soundfile):
        sound_thread = threading.Thread(target=self.play_sound, args=(soundfile,))
        sound_thread.start()

    def play_sound(self, soundfile):
        player = vlc.MediaPlayer("file://" + self.__cwd + "/" + soundfile)
        player.play()
        time.sleep(0.1)
        while player.is_playing():
            time.sleep(0.1)
            if self.__stopall:
                break
        player.stop()
        player.release()

        # print(objgraph.show_most_common_types())


def main():
    Soundboard()

main()
