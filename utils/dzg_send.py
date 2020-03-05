import requests

class Yun(object):
    '''
    封装单条短信发送工具的工具类
    '''
    def __init__(self,api_key):
        self.api_key = api_key
        self.single_send_url = 'https://sms.yunpian.com/v2/sms/single_send.json'

    # 短信发送方法
    def send_message(self,mobile,code):
        # 提供三个参数
        parmes = {
            'apikey':self.api_key,
            'mobile':mobile,
            'text' : "【毛信宇test】您的验证码是{code}。如非本人操作，请忽略本短信".format(code=code),
        }
        req = requests.post(self.single_send_url,data=parmes)
        print(req)

if __name__ == '__main__':
    # yun_pian = Yun('')
    # yun_pian.send_message(15242836837,'6666')
    pass
