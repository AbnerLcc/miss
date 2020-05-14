#!/usr/bin/env python
# -*- coding:utf-8 -*-
import redis


'''创建连接,没使用一次就'''
# conn=redis.StrictRedis(host="192.168.0.108",port=6379,password='123456')
# conn.set('x','nana',ex=10)
# print(conn.get('x'))
# pool=redis.ConnectionPool(host="192.168.0.108",port=6379,max_connections=1000,password='123456')
# con=redis.Redis(connection_pool=pool)
#  con.set(1,2)        # 当set的时候,才会建立socket
                    # 建立连接池,每一次链接都会放在一个列表中,如果超过设置的最大限度就会报错
                    # 当列表中的链接conn被取完之后,就会再次建立连接,如果有就不再创建连接

# con.hset('k1','username','alex')
# con.hset('k1','age',18)
# '''
# redis={
#     k4:{
#         'usename':'alex',
#         'age':18
#     }
# }
# '''
# ret=con.hgetall('k1')
# ret1=con.hget('k2','age')
# print(ret)
# print(ret1)


# con.hmset('a1',{'xiao1':111,"da":str([111,2,4])})
# # print(con.hgetall('k1'))
# # con.hgetall('a1')
# for i in con.hscan_iter('a1'):
#     print(i)
from django_redis import get_redis_connection
con = get_redis_connection("default")

ret=con.hgetall('k1')
ret1=con.hget('k2','age')
print(ret)
print(type(b'dfsdfsf'.decode('utf-8')))
'11'.encode()

from django.middleware.cache import UpdateCacheMiddleware