from Tkinter import *
import ttk
import tkFont
import os
import json

import cv2
import numpy as np
from matplotlib import pyplot as plt
from scipy.interpolate import interp1d

import matplotlib.backends.tkagg as tkagg
from matplotlib.backends.backend_agg import FigureCanvasAgg

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

btn_bg = '#2D9CDB'
btn_numbers_bg = '#6FCF97'
btn_capture_no = '#EB5757'
btn_capture_ok = '#219653'
sample_bg = '#F2F2F2'
btn_red = '#DB2D2D'
btn_green = '#6FDB2D'
btn_blue = '#2F55D9'
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


def write_conc(data):
    with open('conc.txt', 'wb+') as dump:
        dump.write(json.dumps(data))


def read_conc():
    source = open('conc.txt', 'rb').read()
    return json.loads(source)


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
    def __init__(self, x, y, width, height, text, master=root, bg=None, font=primary_font, place=True):
        bg = master['bg'] if bg is None else bg
        Label.__init__(self, master, text=text)
        self.config(bg=bg, fg='black', font=font)
        Wdg.__init__(self, x, y, width, height, place)


class Btn(Button, Wdg):
    def __init__(self, x, y, width, height, text, command, master=root, bg=None, font=primary_font,
                 place=True):
        bg = master['bg'] if bg is None else bg
        Button.__init__(self, master, text=text, command=command, fg='black', highlightthickness=0, bd=0, font=font,
                        activeforeground='white',
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
        Btn(363, 268, 107, 41, 'Done', InputScreen.do_cb, InputScreen.inst, bg=btn_bg)
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


class Sample(Frm):
    def __init__(self, x, y, sample_number, cb):
        def update_conc(new_val):
            self.conc['text'] = new_val
            self.conc['bg'] = self.conc['activebackground'] = sample_bg
            self.conc_done = True
            self.cb()

        def update_btn_capture():
            capture(sample_number)
            self.btn_capture['text'] = 'OK'
            self.btn_capture['bg'] = self.btn_capture['activebackground'] = btn_capture_ok
            self.capture_done = True
            self.cb()

        Frm.__init__(self, x, y, 49, 145, root, bg=sample_bg)
        self.sample_number, self.cb, self.capture_done, self.conc_done = sample_number, cb, False, False
        Lbl(0, 0, 49, 42, '#' + str(sample_number), self)
        self.conc = Btn(0, 52, 49, 52, '0', lambda: InputScreen.get('Concentration ?', update_conc, self.conc['text']),
                        self, bg=btn_capture_no)
        self.btn_capture = Btn(0, 104, 49, 42, 'Capture', update_btn_capture, self, bg=btn_capture_no,
                               font=btn_capture_text)

    def get_conc(self):
        return int(self.conc['text'])

    def is_done(self):
        return self.conc_done and self.capture_done


class SampleCollection(object):
    def __init__(self, number_of_samples, cb):
        self.number_of_samples = number_of_samples
        self.cb = cb
        self.samples = [Sample(69 + sample_number * 59, 62, sample_number + 1, cb) for sample_number in
                        range(number_of_samples)]
        self.position = 0

        def pos_add(x):
            self.position += x

        self.move_right = lambda: [pos_add(-1), self.update_locations()]
        self.move_left = lambda: [pos_add(1), self.update_locations()]

    def update_locations(self):
        if self.number_of_samples < 7: self.position = 0
        if self.position > 0: self.position = 0
        if 6 - self.number_of_samples > self.position: self.position += 1
        for sample in self.samples:
            sample.do_place(69 + (self.position + sample.sample_number - 1) * 59)

    def get_conc(self):
        return map(lambda sample: sample.get_conc(), self.samples)

    def count_done(self):
        return len(filter(lambda sample: sample.is_done(), self.samples))


def mainScreen():
    for s in root.place_slaves():
        s.destroy()
    Btn(69, 113, 107, 94, 'New Test', lambda: InputScreen.get('How many samples?', sampleScreen), bg=btn_bg)
    Btn(186, 113, 107, 94, 'History', None, bg=btn_bg)
    Btn(304, 113, 107, 94, 'Settings', None, bg=btn_bg)


def sampleScreen(number_of_samples=0):
    for s in root.place_slaves():
        s.destroy()

    def done():
        write_conc(samples.get_conc())
        graph_screen()

    def update_controls():
        done_count = samples.count_done()
        title['text'] = 'Capture samples (' + str(done_count) + '/' + str(number_of_samples) + ')'
        if done_count == number_of_samples:
            Btn(363, 268, 107, 41, 'Done', done, bg=btn_bg)

    title = Lbl(69, 10, 342, 42, 'Capture samples (0/' + str(number_of_samples) + ')')
    samples = SampleCollection(number_of_samples, update_controls)

    Btn(421, 62, 49, 145, '>', samples.move_right, bg=btn_bg)
    Btn(10, 62, 49, 145, '<', samples.move_left, bg=btn_bg)


def draw_figure(canvas, figure, loc=(0, 0)):
    figure_canvas_agg = FigureCanvasAgg(figure)
    figure_canvas_agg.draw()
    figure_x, figure_y, figure_w, figure_h = figure.bbox.bounds
    figure_w, figure_h = int(figure_w), int(figure_h)
    photo = PhotoImage(master=canvas, width=figure_w, height=figure_h)
    canvas.create_image(loc[0] + figure_w / 2, loc[1] + figure_h / 2, image=photo)
    tkagg.blit(photo, figure_canvas_agg.get_renderer()._renderer, colormode=2)
    return photo


def opencv_test():
    conc = read_conc()
    max_rgb = [[], [], []]
    for i in range(len(conc)):
        img = cv2.imread('pics/pic' + str(i) + '.jpg')
        img = img[750:1550, 1100:1900]
        # cv2.imshow("cropped", img)
        # cv2.waitKey(0)
        color = ('b', 'g', 'r')
        for i, col in enumerate(color):
            hist = cv2.calcHist([img], [i], None, [256], [0, 256])
            max_rgb[i].append(np.argmax(hist))

    x = conc
    r = max_rgb[0]
    g = max_rgb[1]
    b = max_rgb[2]
    figs = []
    for i in [r, g, b]:
        fig = plt.figure(figsize=(4.6, 1.96))
        fig.add_axes(plt.axes()).scatter(x, i)
        fig.tight_layout()
        figs.append(fig)
    return figs


img = None


def graph_screen():
    for s in root.place_slaves():
        s.destroy()

    def measure_samples():
        pass

    def color_red():
        global img
        img = draw_figure(canvas, figs[0])

    def color_green():
        global img
        img = draw_figure(canvas, figs[1])

    def color_blue():
        global img
        img = draw_figure(canvas, figs[2])

    Lbl(69, 10, 342, 42, 'Choose most suitable color graph')
    Btn(363, 268, 107, 41, 'Measure samples', measure_samples, bg=btn_bg, font=btn_capture_text)
    Btn(10, 268, 49, 42, 'Red', color_red, bg=btn_red, font=btn_capture_text)
    Btn(69, 268, 49, 42, 'Green', color_green, bg=btn_green, font=btn_capture_text)
    Btn(128, 268, 49, 42, 'Blue', color_blue, bg=btn_blue, font=btn_capture_text)
    canvas = Canvas(root)
    canvas.place(x=10, y=62, width=460, height=196)
    figs = opencv_test()


InputScreen.prepare()
mainScreen()
# graph_screen()
if __name__ == "__main__":
    mainWindow.mainloop()
