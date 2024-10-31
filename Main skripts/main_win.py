#import the needed packges

import vlc
import tkinter as tk
import os

#Var for the array and counting
song = 0
song_count = -1

#Array for song list and skip
media_list = []

# Initialize the main window
window = tk.Tk()

#Initialize VLC
p = vlc.MediaPlayer()

#Title
window.title("Simple VLC Player")

# region The window segments
frame1 = tk.Frame(window, relief="solid")
frame1.grid(row=0, column=0, pady=1)

frame2 = tk.Frame(window, relief="solid")
frame2.grid(row=1, column=0, pady=1)  # Place the frame using grid

frame3 = tk.Frame(window, relief="solid")
frame3.grid(row=0, column=1, rowspan=2, pady=1 , columnspan=3)  # Place the frame using grid

# endregion

# region Top labels and input

#Just Text
label = tk.Label(frame1, text="Path:")
label.grid(row=0, column=0, padx=1, pady=5)

#Input for the Dir
path_song = tk.Entry(frame1, width=80,)
path_song.grid(row=0, column=1, padx=1, pady=5)

# endregion

#Load songs
def player_load_songs():
    #Var 
    global song_count
    global song

    #Reset
    song = 0
    song_count = -1

    #Get the dir
    file_path = path_song.get()

    #Just for Debugging
    print("cheack")

    #Deabug which i should but in as a label but ehhhhhhh iam to bored
    if not os.path.exists(file_path):
        print(f"Directory '{file_path}' does not exist.")
    else:

        #Walk through the file_path
        for root, dirs, files in os.walk(file_path):

            #Just for Debugging
            print("check2")
            for file in files:

                #Just for Debugging
                print(os.path.join(root, file))

                #Add songs to array
                media_list.append(os.path.join(root, file))

                #For counting
                song_count = song_count + 1

                #Stolen idfk what "os.path.basename" is but it works (adds all songs to the list)
                player_song_list.insert(tk.END, os.path.basename(file))

#Function to skip songs
def player_skip_song():

    #Var
    global song
    song = song + 1

    #Just for Debugging
    print(song)

    #Passing the index prevention 
    if song > song_count:
        print("no next")
        song = 0
    
    #Sets song
    p.set_mrl(media_list[song])
    p.play()

    #Changes now playing song (splits so i only get the file)
    now_playing = media_list[song].split("\\")[-1]
    player_now_playing.config(text=f"now playing: {now_playing}")

    #Resets pause button
    player_pause_button.config(text="⏸ Pause")
    
#Same as skip so i wont comment it
def player_previous_song():
    global song
    song = song - 1
    print(song)
    if song == -1:
        print("out of range")
        song = song_count
    p.set_mrl(media_list[song])
    p.play()
    now_playing = media_list[song].split("\\")[-1]
    player_now_playing.config(text=f"now playing: {now_playing}")
    player_pause_button.config(text="⏸ Pause")

#Main (Play function)
def player_play():
    #Sets songs back to the first
    song = 0

    #Sets song to to the first thats stupid but i dont want to break it and its fast enught (and plays)
    p.set_mrl(media_list[song])
    p.play()

    #Pause icon change
    player_pause_button.config(text="⏸ Pause")

    #Activates stop button when playing
    player_stop_button.config(state=tk.NORMAL)

    #Changes now playing song (splits so i only get the file)
    now_playing = media_list[song].split("\\")[-1]
    player_now_playing.config(text=f"now playing: {now_playing}")

#Stop function
def player_stop():

    #Stops player
    p.stop()

    #Var
    global song_count
    global song

    song = 0
    song_count = -1

    #When stop we need to? Play!
    player_pause_button.config(text="▶ Resume")

    #Stopping when stopping no now with this >:3
    player_stop_button.config(state=tk.DISABLED)

#Pause function
def player_pause():

    #Just read :P
    if p.is_playing():
        p.pause()

        #Just changes the names
        player_pause_button.config(text="▶ Resume")
    #If its not playing its? Right! Stopped so we play!
    else:
        p.play()

        #Just changes the names
        player_pause_button.config(text="⏸ Pause") 

# region Setting up buttons and labels and all that stuff (the rest that need the Vars from the top)

player_now_playing = tk.Label(frame1, text="waiting for song...")
player_now_playing.grid(row=1, column=0, columnspan=2, pady=5)

player_song_list_text = tk.Label(frame3, text="Song list:")
player_song_list_text.grid(row=0, column=0, columnspan=2, pady=5)

player_song_list = tk.Listbox(frame3, width=50)
player_song_list.grid(row=1, column=0)

player_play_button = tk.Button(frame2, text="▶ Play", width=10, height=2, command=player_play)
player_play_button.grid(row=2, column=0, padx=1, pady=5)

player_skip_button = tk.Button(frame2, text="⏭ Skip", width=10, height=2, command=player_skip_song)
player_skip_button.grid(row=2, column=3, padx=1, pady=5)

player_previous_button = tk.Button(frame2, text="⏮ Previous", width=10, height=2, command=player_previous_song)
player_previous_button.grid(row=2, column=1, padx=1, pady=5)

player_pause_button = tk.Button(frame2, text="⏸ Pause", width=10, height=2, command=player_pause)
player_pause_button.grid(row=2, column=2, padx=1, pady=5)

player_stop_button = tk.Button(frame2, text="■ Stop", width=10, height=2, command=player_stop, state=tk.DISABLED)
player_stop_button.grid(row=2, column=4, padx=1, pady=5)

player_load_button = tk.Button(frame1, text="Load", width=5, height=1, command=player_load_songs)
player_load_button.grid(row=0, column=2, padx=1, pady=5)

# endregion

# region colors! :3

#colors

background_one =    "#16425B"
background_two =    "#16425B"

text_one =          "#D9DCD6"
text_two =          "#D9DCD6"

input_one =         "#2F6690"
input_two =         "#2F6690"

input_bg_one =      "#81C3D7"
input_bg_two =      "#81C3D7"

button =            "#3A7CA5"

button_text =       "#D9DCD6"

window.config(                  bg=background_one)

frame1.config(                  bg=background_one)
label.config(                   bg=background_one,  fg=text_one)
path_song.config(               bg=input_bg_one,    fg=input_one,   selectbackground=input_one, selectforeground=input_bg_one)
player_now_playing.config(      bg=background_one,  fg=text_one)

frame2.config(                  bg=background_one)
player_load_button.config(      bg=button,      fg=button_text)
player_stop_button.config(      bg=button,      fg=button_text)
player_pause_button.config(     bg=button,      fg=button_text)
player_skip_button.config(      bg=button,      fg=button_text)
player_previous_button.config(  bg=button,      fg=button_text)
player_play_button.config(      bg=button,      fg=button_text)

frame3.config(                  bg=background_two)
player_song_list_text.config(   bg=background_two,  fg=text_two)
player_song_list.config(        bg=input_bg_two,    fg=input_two,   selectbackground=input_two, selectforeground=input_bg_two)

#presetup
    #window.config(bg='#023047')
    #
    #frame1.config(bg='#023047')
    #label.config(bg='#023047', fg='#8ECAE6')
    #path_song.config(bg='#8ECAE6', fg='#023047', selectbackground='#023047', selectforeground='#8ECAE6')
    #player_now_playing.config(bg='#023047', fg='#8ECAE6')
    #
    #frame2.config(bg='#023047')
    #player_load_button.config(bg='#219ebc', fg='#8ECAE6')
    #player_stop_button.config(bg='#219ebc', fg='#8ECAE6')
    #player_pause_button.config(bg='#219ebc', fg='#8ECAE6')
    #player_skip_button.config(bg='#219ebc', fg='#8ECAE6')
    #player_previous_button.config(bg='#219ebc', fg='#8ECAE6')
    #player_play_button.config(bg='#219ebc', fg='#8ECAE6')
    #
    #frame3.config(bg='#fb8500')
    #player_song_list_text.config(bg='#fb8500', fg='#FFCF57')
    #player_song_list.config(bg='#ffb703', fg='#fb8500', selectbackground='#FFCF57', selectforeground='#fb8500')

# endregion

# Run the Tkinter event loop
window.mainloop()
