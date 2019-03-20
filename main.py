from Tkinter import *
import ttk
import tkFont

root = Tk()
root.title('DK Machine')
# if root.winfo_screenwidth() == 800 and root.winfo_screenheight() == 480:
#     root.wm_attributes("-fullscreen", True)
root.geometry('%dx%d+%d+%d' % (320, 240, 0, 0))

# root.rowconfigure(6, {'minsize': 40})
# root.columnconfigure(8, {'minsize': 40})

primary_font = tkFont.Font(family='Ubuntu', size=12, weight='bold')
secondary_font = tkFont.Font(family='Ubuntu Mono', size=20)
secondary_font_roboto = tkFont.Font(family='Roboto', size=25)
small_font_roboto = tkFont.Font(family='Roboto', size=15)
smaller_font_roboto = tkFont.Font(family='Roboto', size=11)
test_font = tkFont.Font(family='Ubuntu Mono', size=25)
info_font = tkFont.Font(family='Ubuntu Mono', size=11)
small_font = tkFont.Font(family='Ubuntu Mono', size=13)

primary_color = '#2D9CDB'
accept_color = '#378C35'
reject_color = '#C51C3A'

background_color = "white"
background_highlight_color = "#B2D7E3"

root['bg'] = background_color


class MyButton(Button):
    def __init__(self, master, text, command=None, type='normal', height=0, fill=X,
                 expand=True, anchor=N, side=LEFT, font=primary_font, width=15, **kwargs):
        Button.__init__(self, master, text=text, command=command, height=height, fg='black', bd=0,
                        font=font, activeforeground='white')
        self['bg'] = self['activebackground'] = \
            {'normal': primary_color, 'accept': accept_color, 'reject': reject_color}[type]
        self['width'] = width
        self.pack(fill=fill, expand=expand, anchor=anchor, side=side, **kwargs)


class MyFrame(Frame):
    def __init__(self, master, side, bg=background_color, height=0, anchor=N, fill=BOTH, expand=True, width=0,
                 **kwargs):
        Frame.__init__(self, master, bg=bg)
        self['width'] = width
        self['height'] = height
        self.anchor = anchor
        self.fill = fill
        self.expand = expand
        self.side = side
        self.kwargs = kwargs
        self.do_pack()

    def do_pack(self):
        self.pack(anchor=self.anchor, fill=self.fill, expand=self.expand, side=self.side, **self.kwargs)


def mainScreen():
    for s in root.pack_slaves():
        s.destroy()
    frame = MyFrame(root, TOP)
    MyButton(frame, 'New Test', fill=BOTH, width=10, pady=60, padx=(20, 10))
    MyButton(frame, 'History', fill=BOTH, width=10, pady=60, padx=(10, 20))


mainScreen()
if __name__ == "__main__":
    root.mainloop()
