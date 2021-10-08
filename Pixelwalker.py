import pyautogui
from pynput.keyboard import *

move_left = Key.left
move_right = Key.right
move_up = Key.up
move_down = Key.down
exit_key = Key.esc


def on_press(key):
    if key == exit_key:
        print("[EXIT]")
        return False
    elif key == move_left:
        pyautogui.moveRel(-1, 0)
    elif key == move_right:
        pyautogui.moveRel(1, 0)
    elif key == move_up:
        pyautogui.moveRel(0, -1)
    elif key == move_down:
        pyautogui.moveRel(0, 1)


def display_controls():
    print("// Pixelwalker")
    print("// - Controls:")
    print("\t ESC = Exit")
    print("\t use the arrow keys to move your mouse 1 pixel in that direction.")
    print("\t Don't hold it down as it is not very efficient yet and will hang on some parts")
    print("-----------------------------------------------------")



def main():
    with Listener(on_press=on_press)as listener:
        print("Pixelwalker Activated!")
        display_controls()
        listener.join()

if __name__ == "__main__":
    main()