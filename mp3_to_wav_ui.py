import logging
import logging.config
CON_LOG='log.conf'
logging.config.fileConfig(CON_LOG)
logging=logging.getLogger()
from tkinter import *
from tkinter.filedialog import askopenfilename,askopenfilenames,askdirectory,asksaveasfilename
from tkinter import scrolledtext
#from handle import baidu_speech_merge
import threading
from mp3_to_wav import mp3_to_wav

def _ui():
    root=Tk()
    root.title("mp3转wav工具")
    ww = 100
    wh = 100
    # x=(sw-ww)/2
    # y=((sh-wh)/3)*2
    x = 900
    y = 600
    root.geometry("%dx%d+%d+%d" % (x, y, ww, wh))

    title = Label(root, text="   mp3转wav工具", compound=CENTER, font=("微软雅黑", 20))
    title.grid(row=0, columnspan=3, sticky=E + W)

    result_path = StringVar()
    result_path_label = Label(root, text="文件路径", foreground="white", background="blue")
    result_path_label.grid(sticky=E, padx=20, pady=20)
    result_path_entry = Entry(root, textvariable=result_path, width=70)
    result_path_entry.grid(row=1, column=1, sticky=W)

    def select_result_path():
        path_ = askdirectory()
        result_path.set(path_)
        logging.info("路径： " + str(path_))

    Button(root, text="结果路径选择", command=select_result_path).grid(row=1, column=2)

    def click():
        # logging.info("点击开始合成按钮，开始语料的合成")
        # path_excel=excel_path_entry.get()
        # logging.info("获取到的Excel路径: "+str(path_excel))

        path_result = result_path_entry.get()
        logging.info("路径： " + str(path_result))

        # #添加一个线程
        # th=threading.Thread(target=I_do,args=(deviceid,email,wake_path,jiaohu_path,excel_path,device_version))
        # th.setDaemon(True)  #设置守护线程，主线程结束后，该线程也要结束
        # th.start()

        # th=threading.Thread(target=baidu_speech_merge,args=(text,path_excel,path_result))
        th = threading.Thread(target=mp3_to_wav, args=(path_result,))
        th.setDaemon(True)
        th.start()
        # baidu_speech_merge(text,path_excel,path_result)

    click_btn = Button(root, text="开始转换", command=click)
    click_btn.grid(row=4)

    root.mainloop()

if __name__=="__main__":
    _ui()