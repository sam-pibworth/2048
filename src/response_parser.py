# import tkinter as tk
import os


class UserInput:
    def get_response():
        while True:
            inp = input("\n")
            os.system('clear')
            if inp in ("w", "a", "s", "d"):
                return {"w": "up", "a": "left", "s": "down", "d": "right"}[inp]
            else:
                print("please input direction")
