import tkinter as tk
import os

class UserInput:
    def get_reponse():
        if os.environ.get('DISPLAY','') == '':
            print('no display found. Using :0.0')
            os.environ.__setitem__('DISPLAY', ':0.0')
        def key(event):
            """shows key or tk code for the key"""
            if event.keysym == 'Escape':
                root.destroy()
            if event.char == event.keysym:
                # normal number and letter characters
                print( 'Normal Key %r' % event.char )
            elif len(event.char) == 1:
                # charcters like []/.,><#$ also Return and ctrl/key
                print( 'Punctuation Key %r (%r)' % (event.keysym, event.char) )
            else:
                # f1 to f12, shift keys, caps lock, Home, End, Delete ...
                print( 'Special Key %r' % event.keysym )


        root = tk.Tk()
        print( "Press a key (Escape key to exit):" )
        root.bind_all('<Key>', key)
        # don't show the tk window
        root.withdraw()
        root.mainloop()