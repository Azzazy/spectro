from Tkinter import *
import ttk
import tkFont

root = Tk()
root.title('DK Machine')
if root.winfo_screenwidth() == 320 and root.winfo_screenheight() == 240:
    root.wm_attributes("-fullscreen", True)
root.geometry('%dx%d+%d+%d' % (320, 240, 0, 0))

# root.rowconfigure(6, {'minsize': 40})
# root.columnconfigure(8, {'minsize': 40})

primary_font = tkFont.Font(family='Roboto', size=12, weight='bold')
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
    def __init__(self, master, text, font=secondary_font, bg=background_color, width=0, height=0, fg='black', fill=X,
                 expand=True, anchor=N, side=LEFT, **kwargs):
        Label.__init__(self, master, text=text)
        self.config(bg=bg, fg=fg, font=font, width=width, height=height)
        self.pack(fill=fill, expand=expand, anchor=anchor, side=side, **kwargs)


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
    MyButton(frame, 'New Test', command=inputScreen, fill=BOTH, width=10, pady=60, padx=(20, 10))
    MyButton(frame, 'History', fill=BOTH, width=10, pady=60, padx=(10, 20))


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

    topFrame = MyFrame(root, TOP)
    MyLabel(topFrame, 'How many samples?')

    botFrame = MyFrame(root, TOP)
    leftFrame = MyFrame(botFrame, LEFT)
    leftFrame1 = MyFrame(leftFrame, LEFT, padx=(10, 5))
    leftFrame2 = MyFrame(leftFrame, LEFT, padx=(0, 5))
    leftFrame3 = MyFrame(leftFrame, LEFT, padx=(0, 10))
    MyButton(leftFrame1, '7', command=lambda: makeInput('7'), type='accept', side=TOP, fill=BOTH, width=1, pady=(0, 5))
    MyButton(leftFrame1, '4', command=lambda: makeInput('4'), type='accept', side=TOP, fill=BOTH, width=1, pady=(0, 5))
    MyButton(leftFrame1, '1', command=lambda: makeInput('1'), type='accept', side=TOP, fill=BOTH, width=1, pady=(0, 5))
    MyButton(leftFrame1, 'clear', command=lambda: makeInput('clear'), type='accept', side=TOP, fill=BOTH, width=1,
             pady=(0, 10))

    MyButton(leftFrame2, '8', command=lambda: makeInput('8'), type='accept', side=TOP, fill=BOTH, width=1, pady=(0, 5))
    MyButton(leftFrame2, '5', command=lambda: makeInput('5'), type='accept', side=TOP, fill=BOTH, width=1, pady=(0, 5))
    MyButton(leftFrame2, '2', command=lambda: makeInput('2'), type='accept', side=TOP, fill=BOTH, width=1, pady=(0, 5))
    MyButton(leftFrame2, '0', command=lambda: makeInput('0'), type='accept', side=TOP, fill=BOTH, width=1, pady=(0, 10))

    MyButton(leftFrame3, '9', command=lambda: makeInput('9'), type='accept', side=TOP, fill=BOTH, width=1, pady=(0, 5))
    MyButton(leftFrame3, '6', command=lambda: makeInput('6'), type='accept', side=TOP, fill=BOTH, width=1, pady=(0, 5))
    MyButton(leftFrame3, '3', command=lambda: makeInput('3'), type='accept', side=TOP, fill=BOTH, width=1, pady=(0, 5))
    MyButton(leftFrame3, '<', command=lambda: makeInput('<'), type='accept', side=TOP, fill=BOTH, width=1, pady=(0, 10))

    rightFrame = MyFrame(botFrame, LEFT, padx=(0, 10))
    result = MyLabel(rightFrame, '0', bg='gray', side=TOP)
    MyButton(rightFrame, 'Done', command=lambda: sampleScreen(int(result['text'])), side=TOP, fill=BOTH, width=1,
             pady=(0, 10))


def sampleScreen(numberOfSamples=0):
    for s in root.pack_slaves():
        s.destroy()

    topFrame = MyFrame(root, TOP)
    MyLabel(topFrame, str(numberOfSamples) + ' samples')
    MyLabel(topFrame, str(root.winfo_screenwidth()))


mainScreen()
if __name__ == "__main__":
    root.mainloop()
