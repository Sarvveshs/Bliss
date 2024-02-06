import pyglet,tkinter
pyglet.font.add_file('upheavtt.ttf')

root = tkinter.Tk()
MyLabel = tkinter.Label(root,text="test",font=('Upheaval TT (BRK)',25))
MyLabel.pack()
root.mainloop()