"""
AudioController.py

Controls Audio

Date-Created: 2022 NOV 22
Date-Last-Modified: 2022 NOV 22
Author: Piyotr Kao
"""

import pygame

pygame.init()

song_path = "./res/audio/songs/"
sfx_path = "./res/audio/sfx/"

allSongs = [
    song_path + "Silhouette.mp3",
    song_path + "Radiator.mp3",
    ]

allSfx = [
    pygame.mixer.Sound(sfx_path + "gunshot_1.mp3"),
    ]

def play(_id : int = 0, _vol : float = 1.0, _loop : bool = False) -> None:
    """
    Play a song with the given id and volume and whether to loop it or not
    """
    if _id < 0 or _id > len(allSongs):
        print("Song does not exist!")
        return
    pygame.mixer.music.load(allSongs[_id])
    pygame.mixer.music.set_volume(_vol)
    if _loop:
        pygame.mixer.music.play(-1)
    else:
        pygame.mixer.music.play(0)

def play_sfx(_id : int = 0, _vol : float = 1.0) -> None:
    """
    Play a short sound effect with the given id and volume
    """

    if _id < 0 or _id > len(allSfx):
        print("Sound effect does not exist!")
        return
    allSfx[_id].stop()
    allSfx[_id].set_volume(_vol)
    allSfx[_id].play(fade_ms=100) # fade maybe?

def pause() -> None:
    pygame.mixer.music.pause()

def unpause() -> None:
    pygame.mixer.music.unpause()

def stop(fade_ms : int = 0) -> None:
    if (fade_ms > 0):
        pygame.mixer.music.fadeout(fade_ms)
    else:
        pygame.mixer.music.stop()

def stop_all() -> None:
    for s in allSfx:
        s.stop()