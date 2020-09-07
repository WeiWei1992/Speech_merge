from aip import AipSpeech
APP_ID= '22120812'
API_KEY= 'gFpnrBKUGt76n5Z0DcPg8UNF'
SECRET_KEY= 'i74V1UateUSyma2gWHmiC1fl34e8ZLrl'
import os

# APP_ID = '14636839'
# API_KEY = 'u34cdKCsR61tzM0r20Qnp3YM'
# SECRET_KEY = 'Rehs5G02EqbrRDDgGdPY9NKY2ZlCX8Oq'

import logging
import logging.config
CON_LOG='log.conf'
logging.config.fileConfig(CON_LOG)
logging=logging.getLogger()

client=AipSpeech(APP_ID,API_KEY,SECRET_KEY)
path=os.getcwd()

def baidu_mp3(text,foldpath=None):
    logging.info("开始调用百度接口进行语音合成")
    #file=
    if not foldpath:
        filepath=os.path.join(path,'Result/'+text+'.wav')
    else:
        filepath=os.path.join(foldpath,text+'.wav')
    logging.info("保存生成的wav文件路径： "+str(filepath))
    try:
        result=client.synthesis(text,'zh',1,{
            'vol':12,
            'per':106,
            'aue':5118,
        })
    except Exception as e:
        logging.error("百度接口报错，出现异常，异常信息如下,并返回False")
        logging.error(str(e))
        return False

    if not isinstance(result,dict):
        logging.info("百度接口返回正确，保存成wav,并返回True")
        with open(filepath,'wb') as f:
            f.write(result)
        return True
    else:
        logging.error("百度接口返回错误,并返回False")
        return False


if __name__=="__main__":
    baidu_mp3("你好,小优，106")


# result  = client.synthesis('你好百度,我是小优', 'zh', 1, {
#     'vol':12,
#     'per':0,})
# print(result)
# # 识别正确返回语音二进制 错误则返回dict 参照下面错误码
# if not isinstance(result, dict):
#     with open('你好百度,我是小优12.mp3', 'wb') as f:
#         f.write(result)