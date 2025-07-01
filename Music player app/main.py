import tkinter as tk
from PIL import ImageTk ,Image
import pygame

pygame.mixer.init()

# Create the main window
window = tk.Tk()
window.title("My Music Player")
window.geometry("400x400")  

#now playing label
np_label = tk.Label(window, text="Now playing",font=("Times new roman",25))
np_label.pack()

#song title:
song_title_label = tk.Label(window, text="song: ",font=("Times new roman",15))
song_title_label.pack()

songs = ["Royalty","Beliver","Daastan","Natural"]
current_song_index = 0 
song_files = ["music/royalty.mp3", "music/beliver.mp3", "music/daastan.mp3","music/natural.mp3"]
thumbnail_files = [
    "thumbnails/royalty.jpg",
    "thumbnails/beliver.jpg",
    "thumbnails/daastan.jpg","thumbnails/natural.jpg"
]

is_playing = False

# changing imaging:
def update_image(index):
    image = Image.open(thumbnail_files[index])
    image = image.resize((200,200))
    new_img = ImageTk.PhotoImage(image)
    canvas.image = new_img  # Keep reference!
    canvas.create_image(0, 0, anchor=tk.NW, image=new_img)

def toggle_play_pause():
    global current_song_index
    global is_playing
    if not is_playing:

        song_title_label.config(text =songs[current_song_index])
        song_path= song_files[current_song_index]

        pygame.mixer.music.load(song_path)  # load the song
        pygame.mixer.music.play() 
        song_title_label.config(text=songs[current_song_index])
        update_image(current_song_index)
        play_button.config(text="⏸️")

        is_playing = True

    else:
        # Pause the music
        pygame.mixer.music.pause()

        # Update button text
        play_button.config(text="▶️")

        # Music is now paused
        is_playing = False
        
# Images:
canvas = tk.Canvas(window, width=200, height=200, highlightthickness=0)
canvas.pack(pady=5)

royalty = Image.open("thumbnails/royalty.jpg")
royalty = royalty.resize((200, 200))
my_image = ImageTk.PhotoImage(royalty)
canvas.image = my_image  # Keep reference
canvas.create_image(0, 0, anchor=tk.NW, image=my_image)


def play_song_at_index(index):
    global is_playing, current_song_index
    current_song_index = index
    song_title_label.config(text=songs[current_song_index])
    song_path = song_files[current_song_index]
    pygame.mixer.music.load(song_path)
    pygame.mixer.music.play()
    update_image(current_song_index)
    play_button.config(text="⏸️")
    is_playing = True

def next_song():
    global current_song_index
    current_song_index += 1
    if current_song_index >= len(songs):
        current_song_index = 0
    play_song_at_index(current_song_index)

def prev_song():
    global current_song_index
    current_song_index -= 1
    if current_song_index < 0:
        current_song_index = len(songs) - 1
    play_song_at_index(current_song_index)

# Button:
# Buttons on top of image
play_button = tk.Button(canvas, text="▶️", command=toggle_play_pause)
next_button = tk.Button(canvas, text="⏭️", command=next_song)
prev_button = tk.Button(canvas, text="⏮️", command=prev_song)

# Place buttons on the canvas (x, y coordinates)
canvas.create_window(100, 160, window=play_button)  # Centered near bottom
canvas.create_window(160, 160, window=next_button)  # Right side
canvas.create_window(40, 160, window=prev_button)   # Left side


# To run:
window.mainloop()