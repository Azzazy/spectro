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
main_text = tkFont.Font(family='Roboto', size=14)  # , weight='bold')
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

btn_numbers_bg = '#6FCF97'
btn_capture_no = '#EB5757'
root['bg'] = background_color

globalObj = None


class Wdg(object):
    def __init__(self, x, y, width, height, place):
        self.x, self.y, self.width, self.height = x, y, width, height
        if place:
            self.place(x=x, y=y, width=width, height=height)

    def do_place(self, x=-1, y=-1):
        x, y = self.x if x == -1 else x, self.y if y == -1 else x
        self.place(x=x, y=y, width=self.width, height=self.height)


class Frm(Frame, Wdg):
    def __init__(self, x, y, width, height, master=root, bg=background_color, place=True):
        Frame.__init__(self, master, bg=bg)
        Wdg.__init__(self, x, y, width, height, place)


class Lbl(Label, Wdg):
    def __init__(self, x, y, width, height, text, master=root, bg=background_color, font=primary_font, place=True):
        Label.__init__(self, master, text=text)
        self.config(bg=bg, fg='black', font=font)
        Wdg.__init__(self, x, y, width, height, place)


class Btn(Button, Wdg):
    def __init__(self, x, y, width, height, text, command, master=root, bg=primary_color, font=primary_font,
                 place=True):
        Button.__init__(self, master, text=text, command=command, fg='black', bd=0, font=font, activeforeground='white',
                        bg=bg, activebackground=bg)
        Wdg.__init__(self, x, y, width, height, place)


def mainScreen():
    for s in root.place_slaves():
        s.destroy()
    Btn(69, 113, 107, 94, 'New Test', inputScreen)
    Btn(186, 113, 107, 94, 'History', None)
    Btn(304, 113, 107, 94, 'Settings', None)


def inputScreen():
    for s in root.place_slaves():
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

    Lbl(69, 10, 342, 41, 'How many samples?')
    Btn(10, 62, 49, 41, '7', lambda: makeInput('7'), bg=btn_numbers_bg)
    Btn(10, 113, 49, 41, '4', lambda: makeInput('4'), bg=btn_numbers_bg)
    Btn(10, 165, 49, 41, '1', lambda: makeInput('1'), bg=btn_numbers_bg)
    Btn(10, 217, 49, 41, 'clear', lambda: makeInput('clear'), bg=btn_numbers_bg)
    Btn(69, 62, 49, 41, '8', lambda: makeInput('8'), bg=btn_numbers_bg)
    Btn(69, 113, 49, 41, '5', lambda: makeInput('5'), bg=btn_numbers_bg)
    Btn(69, 165, 49, 41, '2', lambda: makeInput('2'), bg=btn_numbers_bg)
    Btn(69, 217, 49, 41, '0', lambda: makeInput('0'), bg=btn_numbers_bg)
    Btn(128, 62, 49, 41, '9', lambda: makeInput('9'), bg=btn_numbers_bg)
    Btn(128, 113, 49, 41, '6', lambda: makeInput('6'), bg=btn_numbers_bg)
    Btn(128, 165, 49, 41, '3', lambda: makeInput('3'), bg=btn_numbers_bg)
    Btn(128, 217, 49, 41, '<', lambda: makeInput('<'), bg=btn_numbers_bg)
    result = Lbl(245, 62, 225, 41, '0', bg='gray')
    Btn(363, 268, 107, 41, 'Done', lambda: sampleScreen(int(result['text'])))


def sampleScreen(numberOfSamples=0):
    for s in root.place_slaves():
        s.destroy()

    Lbl(69, 10, 342, 42, 'Capture samples (0/' + str(numberOfSamples) + ')')
    frame = Frm(69, 62, 49, 145)
    Lbl(0, 0, 49, 42, '#1', frame)
    Btn(0, 52, 49, 42, '0', None, frame)
    Btn(0, 104, 49, 42, 'Capture', None, frame, bg=btn_capture_no)


mainScreen()
if __name__ == "__main__":
    root.mainloop()
