from tkinter import *
from tkinter import ttk

class Tkplayer():
    def __init__(self):
        self.root = Tk()
        self.root.geometry('640x480')
        self.root.configure(bg="beige")
        self.root.title("TK Video Player")
        #setting up frames
        self.video_frame = ttk.Frame(
                self.root,
                width=640, height=400, 
                padding=(5,5))
        self.button_frame = ttk.Frame(
                self.root, 
                width=640, height=80, 
                padding=(5,5))
        self.play_button = ttk.Button(self.root, text = 'play', command=self.play_video)
        #place the frame and buttons
        self.video_frame.grid(column=0, row=0, columnspan=3, sticky=(N,S,E,W))
        self.button_frame.grid(column=0, row=1, sticky=(E,W))
        self.play_button.grid(row=1)
        #resize options
        self.root.columnconfigure(0,weight=1)
        self.root.rowconfigure(0, weight=1)
        self.video_frame.columnconfigure(0, weight=1)
        self.video_frame.rowconfigure(0, weight=1)
        self.play_button.columnconfigure(0, weight=0)
        #start application loop
        self.root.mainloop()

    def play_video(self):
        pass


def main():
    tmp = Tkplayer()
    return 0

if __name__ == '__main__':
    main()
