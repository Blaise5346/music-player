import tkinter as tk
from tkinter import filedialog
import pygame

pygame.init()

media_file = None
media_playing = False

def browse_file():
    global media_file
    media_file = filedialog.askopenfilename(title='Choose a Media file')


def play_file():
    global media_file, media_playing
    if media_file and not media_playing:
        pygame.mixer.music.load(media_file)
        pygame.mixer.music.play()
        media_playing = True

def pause_file():
    global media_playing
    if media_playing:
        pygame.mixer.music.pause()
        media_playing = False

def resume_file():
    global media_playing
    if not media_playing:
        pygame.mixer.music.unpause()
        media_playing = True

def stop_file():
    global media_playing
    if media_playing:
        pygame.mixer.music.stop()
        media_playing = False

root = tk.Tk()
root.title("Media Player")
root.geometry('300x200')

browse_button = tk.Button(root, text='Browse', command=browse_file)
browse_button.pack(pady=10)

play_button = tk.Button(root, text='Play', command=play_file)
play_button.pack(pady=10)

pause_button = tk.Button(root, text='Pause', command=pause_file)
pause_button.pack(pady=10)

resume_button = tk.Button(root, text='Resume', command=resume_file)
resume_button.pack(pady=10)

stop_button = tk.Button(root, text='Stop', command=stop_file)
stop_button.pack(pady=10)

root.mainloop()