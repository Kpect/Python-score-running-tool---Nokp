import tkinter as tk
from tkinter import *
from ttkthemes import *
from tkinter.ttk import *
import psutil
import platform
import cpuinfo
import os
import wmi
import time
import multiprocessing
import concurrent.futures
from concurrent.futures import ProcessPoolExecutor
from concurrent.futures import as_completed





print("欢迎使用Nokp,100%使用Python打造
def complex_calculation(n):
    result = 0
    for i in range(n):
        result += i
    return result
def get_cpu_model():
    info = cpuinfo.get_cpu_info()
    return info["brand_raw"]

class WinGUI(Tk):
    def __init__(self):
        super().__init__()
        self.__win()
        self.tk_label_lpxs9jx5 = self.__tk_label_lpxs9jx5(self)
        self.tk_label_lpxs9x5u = self.__tk_label_lpxs9x5u(self)
        self.tk_progressbar_lpxsan9t = self.__tk_progressbar_lpxsan9t(self)
        self.tk_progressbar_lpxsazd5 = self.__tk_progressbar_lpxsazd5(self)
        self.tk_label_lpxsb535 = self.__tk_label_lpxsb535(self)
        self.tk_label_lpxsbemh = self.__tk_label_lpxsbemh(self)
        self.tk_label_frame_lpxscesy = self.__tk_label_frame_lpxscesy(self)
        self.tk_label_lpxscr77 = self.__tk_label_lpxscr77(self.tk_label_frame_lpxscesy) 
        self.tk_label_lpxse6wp = self.__tk_label_lpxse6wp(self.tk_label_frame_lpxscesy) 
        self.tk_button_lpxshdld = self.__tk_button_lpxshdld(self)
        self.tk_label_lpxsiygz = self.__tk_label_lpxsiygz(self)
        self.mainloop()
    
    def __win(self):
        self.title("Nokp")
        self.geometry("382x352")
        self.resizable(width=False, height=False)
        
    def scrollbar_autohide(self, vbar, hbar, widget):
        """自动隐藏滚动条"""
        def show():
            if vbar: vbar.lift(widget)
            if hbar: hbar.lift(widget)
        def hide():
            if vbar: vbar.lower(widget)
            if hbar: hbar.lower(widget)
        hide()
        widget.bind("<Enter>", lambda e: show())
        if vbar: vbar.bind("<Enter>", lambda e: show())
        if vbar: vbar.bind("<Leave>", lambda e: hide())
        if hbar: hbar.bind("<Enter>", lambda e: show())
        if hbar: hbar.bind("<Leave>", lambda e: hide())
        widget.bind("<Leave>", lambda e: hide())
    
    def v_scrollbar(self, vbar, widget, x, y, w, h, pw, ph):
        widget.configure(yscrollcommand=vbar.set)
        vbar.config(command=widget.yview)
        vbar.place(relx=(w + x) / pw, rely=y / ph, relheight=h / ph, anchor='ne')
    
    def h_scrollbar(self, hbar, widget, x, y, w, h, pw, ph):
        widget.configure(xscrollcommand=hbar.set)
        hbar.config(command=widget.xview)
        hbar.place(relx=x / pw, rely=(y + h) / ph, relwidth=w / pw, anchor='sw')
    
    def create_bar(self, master, widget, is_vbar, is_hbar, x, y, w, h, pw, ph):
        vbar, hbar = None, None
        if is_vbar:
            vbar = Scrollbar(master)
            self.v_scrollbar(vbar, widget, x, y, w, h, pw, ph)
        if is_hbar:
            hbar = Scrollbar(master, orient="horizontal")
            self.h_scrollbar(hbar, widget, x, y, w, h, pw, ph)
        self.scrollbar_autohide(vbar, hbar, widget)
    
    def __tk_label_lpxs9jx5(self, parent):
        label = Label(parent, text="单核跑分", anchor="center")
        label.place(x=0, y=10, width=76, height=30)
        return label
    
    def __tk_label_lpxs9x5u(self, parent):
        label = Label(parent, text="多核跑分", anchor="center")
        label.place(x=0, y=60, width=76, height=30)
        return label
    
    def __tk_progressbar_lpxsan9t(self, parent):
        progressbar = Progressbar(parent, orient=HORIZONTAL)
        progressbar.place(x=90, y=10, width=150, height=30)
        return progressbar
    
    def __tk_progressbar_lpxsazd5(self, parent):
        progressbar = Progressbar(parent, orient=HORIZONTAL)
        progressbar.place(x=90, y=60, width=150, height=30)
        return progressbar
    
    def __tk_label_lpxsb535(self, parent):
        label = Label(parent, text="单核得分", anchor="center")
        label.place(x=230, y=10, width=100, height=30)
        return label

    def __tk_label_lpxsbemh(self, parent):
        label = Label(parent, text="多核得分", anchor="center")
        label.place(x=230, y=60, width=100, height=30)
        return label

    
    def __tk_label_frame_lpxscesy(self, parent):
        frame = LabelFrame(parent, text="CPU信息")
        frame.place(x=1, y=90, width=700, height=143)
        return frame   
    
    def __tk_label_lpxscr77(self, parent):
        cpu_name = get_cpu_model()
        label = Label(parent, text="名称："+str(cpu_name), anchor="center")
        label.place(x=10, y=10, width=370, height=30)
        return label
    
    def __tk_label_lpxse6wp(self, parent):
        cpu_core = os.cpu_count()
        label = Label(parent, text="核心数："+str(cpu_core), anchor="center")
        label.place(x=0, y=60, width=370, height=30)
        return label
    
    def __tk_button_lpxshdld(self, parent):
        btn = tk.ttk.Button(parent, text="开始跑分", takefocus=False, command=self.start_benchmark)
        btn.place(x=10, y=250, width=134, height=55)
        return btn
    
    def __tk_label_lpxsiygz(self, parent):
        label = Label(parent, text="Copyright © 2023 Bingzi. All rights reserved.rough ver1.0", anchor="center")
        label.place(x=10, y=310, width=369, height=30)
        return label
        

    def start_benchmark(self):
        print("[Nokp]正在跑分，稍等片刻。")
        self.tk_progressbar_lpxsan9t["value"] = 0
        self.tk_progressbar_lpxsazd5["value"] = 0

        # 单核跑分
        start_time = time.perf_counter()

        with concurrent.futures.ThreadPoolExecutor() as executor:

            results = executor.map(complex_calculation, range(1, 6000))

        end_time = time.perf_counter()
        single_core_score = end_time - start_time
        self.tk_label_lpxsb535.config(text="单核得分：" + str(single_core_score * 10000000))

        # 多核跑分
        multi_core_scores = []
        with ProcessPoolExecutor() as executor:
            tasks = [executor.submit(complex_calculation, i) for i in range(1, 6000]

            for i, task in enumerate(as_completed(tasks)):
                self.tk_progressbar_lpxsazd5["value"] = (i + 1) * 1000 / multiprocessing.cpu_count()
                self.update_idletasks()
                time.sleep(0.05)
                multi_core_scores.append(task.result())

        multi_core_score = sum(multi_core_scores) / len(multi_core_scores)
        self.tk_label_lpxsbemh.config(text="多核得分：" + str(multi_core_score * 10000000))
        print("多"+str(multi_core_score * 10000000)+"单"+str(single_core_score * 10000000))

class Win(WinGUI):
    def __init__(self):
        super().__init__()
        self.__event_bind()
    
    def __event_bind(self):
        pass

if __name__ == "__main__":
    win = Win()
    win.mainloop()
