import logging
import logging.config
CON_LOG='log.conf'
logging.config.fileConfig(CON_LOG)
logging=logging.getLogger()
from tkinter import *
from tkinter.filedialog import askopenfilename,askopenfilenames,askdirectory,asksaveasfilename
from tkinter import scrolledtext
from handle import baidu_speech_merge
import threading
def _ui():
    root=Tk()
    root.title("语料合成工具")

    #屏幕宽度
    sw=root.winfo_screenwidth()
    #屏幕高度
    sh=root.winfo_screenheight()

    #定义屏幕长宽和左上点位置
    ww=100
    wh=100
    # x=(sw-ww)/2
    # y=((sh-wh)/3)*2
    x=900
    y=600

    root.geometry("%dx%d+%d+%d"%(x,y,ww,wh))

    title=Label(root,text="          语料合成工具", compound=CENTER, font=("微软雅黑", 20))
    title.grid(row=0, columnspan=3, sticky=E + W)

    excel_path=StringVar()
    excel_path_label=Label(root,text='语料合成',foreground="white",background="blue")
    excel_path_label.grid(sticky=E,padx=20,pady=20)
    excel_path_entry=Entry(root,textvariable=excel_path,width=70)
    excel_path_entry.grid(row=1,column=1,sticky=W)
    def select_excel_path():
        path_=askopenfilename()
        excel_path.set(path_)
        logging.info("Excel Path: "+str(path_))
    Button(root,text="选择文件",command=select_excel_path).grid(row=1,column=2)

    result_path=StringVar()
    result_path_label=Label(root,text="语料保存路径",foreground="white",background="blue")
    result_path_label.grid(sticky=E,padx=20,pady=20)
    result_path_entry=Entry(root,textvariable=result_path,width=70)
    result_path_entry.grid(row=2,column=1,sticky=W)
    def select_result_path():
        path_=askdirectory()
        result_path.set(path_)
        logging.info("结果保存路径： "+str(path_))
    Button(root,text="结果路径选择",command=select_result_path).grid(row=2,column=2)

    text = scrolledtext.ScrolledText(root, width=80, height=20)
    text.grid(row=3, column=1, columnspan=2, sticky=W)


    def click():
        logging.info("点击开始合成按钮，开始语料的合成")
        path_excel=excel_path_entry.get()
        logging.info("获取到的Excel路径: "+str(path_excel))

        path_result=result_path_entry.get()
        logging.info("结果保存路径： "+str(path_result))

        # #添加一个线程
        # th=threading.Thread(target=I_do,args=(deviceid,email,wake_path,jiaohu_path,excel_path,device_version))
        # th.setDaemon(True)  #设置守护线程，主线程结束后，该线程也要结束
        # th.start()

        th=threading.Thread(target=baidu_speech_merge,args=(text,path_excel,path_result))
        th.setDaemon(True)
        th.start()
        #baidu_speech_merge(text,path_excel,path_result)


    click_btn=Button(root,text="开始合成",command=click)
    click_btn.grid(row=4)



    root.mainloop()


if __name__=="__main__":
    _ui()