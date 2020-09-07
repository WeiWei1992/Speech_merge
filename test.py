from aip import AipSpeech
APP_ID= '22120812'
API_KEY= 'gFpnrBKUGt76n5Z0DcPg8UNF'
SECRET_KEY= 'i74V1UateUSyma2gWHmiC1fl34e8ZLrl'

# APP_ID = '14636839'
# API_KEY = 'u34cdKCsR61tzM0r20Qnp3YM'
# SECRET_KEY = 'Rehs5G02EqbrRDDgGdPY9NKY2ZlCX8Oq'

client=AipSpeech(APP_ID,API_KEY,SECRET_KEY)

result  = client.synthesis('你好百度,我是小优', 'zh', 1, {
    'vol':12,
    'per':0,})
print(result)
# 识别正确返回语音二进制 错误则返回dict 参照下面错误码
if not isinstance(result, dict):
    with open('你好百度,我是小优0.mp3', 'wb') as f:
        f.write(result)