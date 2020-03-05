# from redis import Redis
# Re = Redis(host='localhost',port=6379)
# Re.set('james','hahaha',ex=10)
# while True:
#     res = Re.get('james')
#     if res:
#         print('hahaha')
#     else:
#         break
# print('xixixi')

# s = b'123'
# ss = s.decode('utf-8')
# print(s,type(s),ss)
import datetime
times = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
print(times,type(times))