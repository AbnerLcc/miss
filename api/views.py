from django.shortcuts import render, HttpResponse, redirect
from utils.pay import AliPay
from django.views.decorators.csrf import csrf_exempt
from AliPay import settings

'''
一般都把配置信息放在setting中,且用大写表示
        APPID="2016101000655497",  # 商家id,在商家中心有,注意这里是字符串类型id
        APP_NOTIFY_URL="http://127.0.0.1:8002/page1",  # 如果支付成功就会向该地址发送post请求,修改订单状态
        RETURN_RUL="http://127.0.0.1:8000/check",  # 支付宝成功重定向到网站地址

        # 存放秘钥的文本路径
        APP_PRIVATE_KEY_PATH='keys/app_private_2048.txt',  # 应用私钥,下载文件时生成应用秘钥
        ALIPAY_PUBLIC_KEY_PATH='keys/alipay_public_2048.txt',  # 上传自己生成的公钥到支付宝时生成的公钥,不是自己生成的公钥
'''

import time


# Create your views here.
def index(request, *args, **kwargs):
    if request.method == "GET":
        return render(request, "index.html")
    #  对价格 和商品进行加密,防止自动拼接参数
    #  拼接路径

    else:
        alipay = ali()
        # 注意价格必须是保留两位有效小数,因此需要进行转换
        money = float(request.POST.get('price'))
        # 生成支付的url

        query_params = alipay.direct_pay(
            subject="可爱的娜娜",  # 商品简单描述
            out_trade_no="x2" + str(time.time()),  # 商户订单号
            total_amount=money,  # 交易金额(单位: 元 保留俩位小数)
        )
        pay_url = "https://openapi.alipaydev.com/gateway.do?{0}".format(query_params)

        return redirect(pay_url)


def ali():
    # 沙箱环境地址：https://openhome.alipay.com/platform/appDaily.htm?tab=info
    app_id = "2016101000655497"
    # POST请求，用于最后的检测
    notify_url = "http://127.0.0.1:8002/page2"
    # notify_url = "http://www.wupeiqi.com:8804/page2/"

    # GET请求，用于页面的跳转展示
    return_url = "http://127.0.0.1:8002/page2/"
    # return_url = "http://www.wupeiqi.com:8804/page2/"

    alipay = AliPay(
        appid=settings.APPID,  # 商家id,在商家中心有,注意这里是字符串类型id
        app_notify_url=settings.APP_NOTIFY_URL,  # 如果支付成功就会向该地址发送post请求,修改订单状态
        return_url=settings.RETURN_URL,  # 支付宝成功重定向到网站地址

        # 存放秘钥的文本路径
        app_private_key_path=settings.APP_PRIVATE_KEY_PATH,  # 应用私钥,下载文件时生成应用秘钥
        alipay_public_key_path=settings.ALIPAY_PUBLIC_KEY_PATH,  # 上传自己生成的公钥到支付宝时生成的公钥,不是自己生成的公钥
        debug=True,  # 默认等于false,用于判别往哪里提交数据,false则是真正的支付渠道,true则是沙箱路径提交
    )
    return alipay


@csrf_exempt
def check(request):
    alipay = ali()
    if request.method == "POST":
        # 检测是否支付成功
        # 去请求体中获取所有返回的数据：状态/订单号
        from urllib.parse import parse_qs
        body_str = request.body.decode('utf-8')
        post_data = parse_qs(body_str)

        post_dict = {}
        for k, v in post_data.items():
            post_dict[k] = v[0]
        print(post_dict)

        sign = post_dict.pop('sign', None)
        status = alipay.verify(post_dict, sign)
        print('POST验证', status)
        return HttpResponse('POST返回')

    else:
        params = request.GET.dict()
        sign = params.pop('sign', None)
        status = alipay.verify(params, sign)
        print('66666', status)
        return HttpResponse('支付成功')

# import redis
# from django_redis import get_redis_connection
import time
def index1(request):
    # pool = redis.ConnectionPool(host='127.0.0.1', port=6379, max_connections=10)
    # con = redis.Redis(connection_pool=pool,decode_responses = True)
    #
    # con.hset('k1', 'username', 'alex')
    # ret1 = con.hget('k1', 'username')
    # print(ret1)
    return  HttpResponse(str(time.time()))