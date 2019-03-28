from Tkinter import *
import ttk
import tkFont
import os

mainWindow = Tk()
mainWindow.title('DK Machine')
if mainWindow.winfo_screenwidth() == 480 and mainWindow.winfo_screenheight() == 320:
    mainWindow.wm_attributes("-fullscreen", True)
mainWindow.geometry('%dx%d+%d+%d' % (480, 320, 0, 0))

# root.rowconfigure(6, {'minsize': 40})
# root.columnconfigure(8, {'minsize': 40})

primary_font = tkFont.Font(family='Roboto', size=12)  # , weight='bold')
main_text = tkFont.Font(family='Roboto', size=14)  # , weight='bold')
secondary_font_roboto = tkFont.Font(family='Roboto', size=25)
small_font_roboto = tkFont.Font(family='Roboto', size=15)
smaller_font_roboto = tkFont.Font(family='Roboto', size=11)
test_font = tkFont.Font(family='Ubuntu Mono', size=25)
info_font = tkFont.Font(family='Ubuntu Mono', size=11)

btn_capture_text = tkFont.Font(family='Roboto', size=8)

primary_color = '#2D9CDB'
accept_color = '#6FCF97'
reject_color = '#C51C3A'

background_color = "white"
background_highlight_color = "#B2D7E3"

btn_numbers_bg = '#6FCF97'
btn_capture_no = '#EB5757'
mainWindow['bg'] = background_color


def can_capture():
    cmd = 'if raspistill -n true 2>/dev/null; then \necho 1 \nelse \necho 0 \nfi'
    if int(os.popen(cmd).readlines()[0]) == 1:
        return True
    return False


def capture(file_name):
    if can_capture():
        os.system('raspistill -q 100 -o ' + str(file_name) + '.jpg')
    else:
        os.system('echo working > ' + str(file_name) + '.txt')


class Wdg(object):
    def __init__(self, x, y, width, height, place):
        self.x, self.y, self.width, self.height = x, y, width, height
        if place:
            self.place(x=x, y=y, width=width, height=height)

    def do_place(self, x=-1, y=-1):
        x, y = self.x if x == -1 else x, self.y if y == -1 else x
        self.place(x=x, y=y, width=self.width, height=self.height)


class Frm(Frame, Wdg):
    def __init__(self, x, y, width, height, master, bg=background_color, place=True):
        Frame.__init__(self, master, bg=bg)
        Wdg.__init__(self, x, y, width, height, place)


root = Frm(0, 0, 480, 320, mainWindow)


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


class InputScreen(object):
    inst = None

    @staticmethod
    def prepare():
        def makeInput(value):
            if value == 'clear':
                InputScreen.inst.result['text'] = ''
            elif value == '<':
                InputScreen.inst.result['text'] = InputScreen.inst.result['text'][:-1]
            else:
                InputScreen.inst.result['text'] = str(int(InputScreen.inst.result['text'] + str(value)))
            if InputScreen.inst.result['text'] == '':
                InputScreen.inst.result['text'] = '0'

        InputScreen.inst = Frm(0, 0, 480, 320, mainWindow)
        InputScreen.inst.title = Lbl(69, 10, 342, 41, 'Empty Input Screen', InputScreen.inst)
        Btn(10, 62, 49, 41, '7', lambda: makeInput('7'), InputScreen.inst, bg=btn_numbers_bg)
        Btn(10, 113, 49, 41, '4', lambda: makeInput('4'), InputScreen.inst, bg=btn_numbers_bg)
        Btn(10, 165, 49, 41, '1', lambda: makeInput('1'), InputScreen.inst, bg=btn_numbers_bg)
        Btn(10, 217, 49, 41, 'clear', lambda: makeInput('clear'), InputScreen.inst, bg=btn_numbers_bg)
        Btn(69, 62, 49, 41, '8', lambda: makeInput('8'), InputScreen.inst, bg=btn_numbers_bg)
        Btn(69, 113, 49, 41, '5', lambda: makeInput('5'), InputScreen.inst, bg=btn_numbers_bg)
        Btn(69, 165, 49, 41, '2', lambda: makeInput('2'), InputScreen.inst, bg=btn_numbers_bg)
        Btn(69, 217, 49, 41, '0', lambda: makeInput('0'), InputScreen.inst, bg=btn_numbers_bg)
        Btn(128, 62, 49, 41, '9', lambda: makeInput('9'), InputScreen.inst, bg=btn_numbers_bg)
        Btn(128, 113, 49, 41, '6', lambda: makeInput('6'), InputScreen.inst, bg=btn_numbers_bg)
        Btn(128, 165, 49, 41, '3', lambda: makeInput('3'), InputScreen.inst, bg=btn_numbers_bg)
        Btn(128, 217, 49, 41, '<', lambda: makeInput('<'), InputScreen.inst, bg=btn_numbers_bg)
        InputScreen.inst.result = Lbl(245, 62, 225, 41, '0', InputScreen.inst, bg='gray')
        Btn(363, 268, 107, 41, 'Done', InputScreen.do_cb, InputScreen.inst)
        InputScreen.inst.place_forget()

    @staticmethod
    def get(title, cb, val='0'):
        if InputScreen.inst is None:
            InputScreen.prepare()
        InputScreen.inst.cb = cb
        InputScreen.inst.result['text'] = str(val)
        InputScreen.inst.title['text'] = title
        root.place_forget()
        InputScreen.inst.do_place()

    @staticmethod
    def do_cb():
        InputScreen.inst.place_forget()
        root.do_place()
        if InputScreen.inst.cb is not None:
            InputScreen.inst.cb(int(InputScreen.inst.result['text']))


def mainScreen():
    for s in root.place_slaves():
        s.destroy()
    Btn(69, 113, 107, 94, 'New Test', lambda: InputScreen.get('How many samples?', sampleScreen))
    Btn(186, 113, 107, 94, 'History', None)
    Btn(304, 113, 107, 94, 'Settings', None)


def sampleScreen(numberOfSamples=0):
    for s in root.place_slaves():
        s.destroy()

    Lbl(69, 10, 342, 42, 'Capture samples (0/' + str(numberOfSamples) + ')')

    sample_number = 1
    frame = Frm(69, 62, 49, 145, root)
    Lbl(0, 0, 49, 42, '#' + str(sample_number), frame)
    conc = None

    def updateConc(newVal):
        conc['text'] = newVal

    conc = Btn(0, 52, 49, 42, '0', lambda: InputScreen.get('Concentration ?', updateConc, conc['text']), frame)
    Btn(0, 104, 49, 42, 'Capture', lambda: capture(sample_number), frame, bg=btn_capture_no, font=btn_capture_text)


InputScreen.prepare()
mainScreen()
if __name__ == "__main__":
    mainWindow.mainloop()
