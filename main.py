from Tkinter import *
import ttk
import tkFont

root = Tk()
root.title('DK Machine')
if root.winfo_screenwidth() == 480 and root.winfo_screenheight() == 320:
    root.wm_attributes("-fullscreen", True)
root.geometry('%dx%d+%d+%d' % (480, 320, 0, 0))

# root.rowconfigure(6, {'minsize': 40})
# root.columnconfigure(8, {'minsize': 40})

primary_font = tkFont.Font(family='Roboto', size=12)  # , weight='bold')
secondary_font = tkFont.Font(family='Ubuntu Mono', size=20)
secondary_font_roboto = tkFont.Font(family='Roboto', size=25)
small_font_roboto = tkFont.Font(family='Roboto', size=15)
smaller_font_roboto = tkFont.Font(family='Roboto', size=11)
test_font = tkFont.Font(family='Ubuntu Mono', size=25)
info_font = tkFont.Font(family='Ubuntu Mono', size=11)
small_font = tkFont.Font(family='Ubuntu Mono', size=13)

primary_color = '#2D9CDB'
accept_color = '#6FCF97'
reject_color = '#C51C3A'

background_color = "white"
background_highlight_color = "#B2D7E3"

root['bg'] = background_color

globalObj = None


class MyLabel(Label):
    def __init__(self, master, text, font=secondary_font, bg=background_color, width=0, height=0, fg='black', pack=True,
                 fill=X,
                 expand=True, anchor=N, side=LEFT, **kwargs):
        Label.__init__(self, master, text=text)
        self.config(bg=bg, fg=fg, font=font, width=width, height=height)
        if pack:
            self.pack(fill=fill, expand=expand, anchor=anchor, side=side, **kwargs)


class MyButton(Button):
    def __init__(self, master, text, command=None, type='normal', height=0, fill=X,
                 expand=True, anchor=N, side=LEFT, font=primary_font, width=15, pack=True, **kwargs):
        Button.__init__(self, master, text=text, command=command, height=height, fg='black', bd=0,
                        font=font, activeforeground='white')
        self['bg'] = self['activebackground'] = \
            {'normal': primary_color, 'accept': accept_color, 'reject': reject_color}[type]
        self['width'] = width
        if pack:
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
    MyButton(frame, 'New Test', command=inputScreen, fill=BOTH, pack=False, width=10, pady=60, padx=(20, 10)).place(
        x=69, y=113, width=107, height=94)
    MyButton(frame, 'History', fill=BOTH, pack=False, width=10, pady=60, padx=(10, 20)).place(x=186, y=113, width=107,
                                                                                              height=94)
    MyButton(frame, 'Settings', fill=BOTH, pack=False, width=10, pady=60, padx=(10, 20)).place(x=304, y=113, width=107,
                                                                                               height=94)


def inputScreen():
    for s in root.pack_slaves():
        s.destroy()
    result = None

    def makeInput(value):
        if value == 'clear':
            result['text'] = ''
        elif value == '<':
            result['text'] = result['text'][:-1]
        else:
            result['text'] = str(int(result['text'] + str(value)))
        if result['text'] == '':
            result['text'] = '0'

    MyLabel(root, 'How many samples?', pack=False).place(x=69, y=10, width=342, height=41)

    MyButton(root, '7', command=lambda: makeInput('7'), type='accept', pack=False).place(x=10, y=62, width=49,
                                                                                         height=41)
    MyButton(root, '4', command=lambda: makeInput('4'), type='accept', pack=False).place(x=10, y=113, width=49,
                                                                                         height=41)
    MyButton(root, '1', command=lambda: makeInput('1'), type='accept', pack=False).place(x=10, y=165, width=49,
                                                                                         height=41)
    MyButton(root, 'clear', command=lambda: makeInput('clear'), type='accept', pack=False).place(x=10, y=217,
                                                                                                 width=49,
                                                                                                 height=41)

    MyButton(root, '8', command=lambda: makeInput('8'), type='accept', pack=False).place(x=69, y=62, width=49,
                                                                                         height=41)
    MyButton(root, '5', command=lambda: makeInput('5'), type='accept', pack=False).place(x=69, y=113, width=49,
                                                                                         height=41)
    MyButton(root, '2', command=lambda: makeInput('2'), type='accept', pack=False).place(x=69, y=165, width=49,
                                                                                         height=41)
    MyButton(root, '0', command=lambda: makeInput('0'), type='accept', pack=False).place(x=69, y=217, width=49,
                                                                                         height=41)

    MyButton(root, '9', command=lambda: makeInput('9'), type='accept', pack=False).place(x=128, y=62, width=49,
                                                                                         height=41)
    MyButton(root, '6', command=lambda: makeInput('6'), type='accept', pack=False).place(x=128, y=113, width=49,
                                                                                         height=41)
    MyButton(root, '3', command=lambda: makeInput('3'), type='accept', pack=False).place(x=128, y=165, width=49,
                                                                                         height=41)
    MyButton(root, '<', command=lambda: makeInput('<'), type='accept', pack=False).place(x=128, y=217, width=49,
                                                                                         height=41)

    result = MyLabel(root, '0', bg='gray', pack=False)
    result.place(x=245, y=62, width=225, height=41)
    MyButton(root, 'Done', command=lambda: sampleScreen(int(result['text'])), pack=False).place(x=363, y=268,
                                                                                                width=107,
                                                                                                height=41)


def sampleScreen(numberOfSamples=0):
    for s in root.pack_slaves():
        s.destroy()

    topFrame = MyFrame(root, TOP)
    MyLabel(topFrame, str(numberOfSamples) + ' samples')
    MyLabel(topFrame, str(root.winfo_screenwidth()))


mainScreen()
if __name__ == "__main__":
    root.mainloop()
