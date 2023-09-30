import os
import tkinter as tk
from tkinter import filedialog
import pygame

class MusicPlayer:
    def __init__(self, root):
        self.root = root
        self.root.title("Simple Music Player")

        self.playlist = []
        self.current_track = 0

        pygame.mixer.init()

        self.create_ui()
        self.load_playlist()

    def create_ui(self):
        self.track_label = tk.Label(self.root, text="Now Playing:")
        self.track_label.pack(pady=10)

        self.play_button = tk.Button(self.root, text="Play", command=self.play)
        self.play_button.pack()

        self.pause_button = tk.Button(self.root, text="Pause", command=self.pause)
        self.pause_button.pack()

        self.stop_button = tk.Button(self.root, text="Stop", command=self.stop)
        self.stop_button.pack()

        self.next_button = tk.Button(self.root, text="Next", command=self.next_track)
        self.next_button.pack()

        self.add_button = tk.Button(self.root, text="Add to Playlist", command=self.add_to_playlist)
        self.add_button.pack()

        self.playlist_box = tk.Listbox(self.root, selectmode=tk.SINGLE, height=10)
        self.playlist_box.pack(pady=10)

    def load_playlist(self):
        if os.path.exists("playlist.txt"):
            with open("playlist.txt", "r") as file:
                self.playlist = [line.strip() for line in file.readlines()]
                self.update_playlist_box()

    def save_playlist(self):
        with open("playlist.txt", "w") as file:
            file.write("\n".join(self.playlist))

    def update_playlist_box(self):
        self.playlist_box.delete(0, tk.END)
        for track in self.playlist:
            self.playlist_box.insert(tk.END, track)

    def play(self):
        if self.playlist:
            track = self.playlist[self.current_track]
            pygame.mixer.music.load(track)
            pygame.mixer.music.play()

            self.track_label.config(text=f"Now Playing: {os.path.basename(track)}")

    def pause(self):
        pygame.mixer.music.pause()

    def stop(self):
        pygame.mixer.music.stop()

    def next_track(self):
        self.stop()
        self.current_track = (self.current_track + 1) % len(self.playlist)
        self.play()

    def add_to_playlist(self):
        file_path = filedialog.askopenfilename(filetypes=[("MP3 files", "*.mp3")])
        if file_path:
            self.playlist.append(file_path)
            self.update_playlist_box()
            self.save_playlist()

if __name__ == "__main__":
    root = tk.Tk()
    player = MusicPlayer(root)
    root.mainloop()
