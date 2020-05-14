#!/usr/bin/env python
# -*- coding:utf-8 -*-

from datetime import datetime
from Crypto.PublicKey import RSA
from Crypto.Signature import PKCS1_v1_5
from Crypto.Hash import SHA256
from base64 import b64encode, b64decode
from urllib.parse import quote_plus
from urllib.parse import urlparse, parse_qs
from urllib.request import urlopen
from base64 import decodebytes, encodebytes

import json


url = "/check/?charset=utf-8&out_trade_no=x21589420742.0634935&method=alipay.trade.page.pay.return&total_amount=11.88&sign=aTpz9svAzezrlFxYMXhQbN6V7xyP6tN7hMJQfvWD6jZ6tfpWlCgcUGmt%2Fk7moijz4QSJEKvOv7UDu7TElsqUoE7qwTBcyfwHnVZRyHu7RbojAY1JTWIngdcuo7dyoDMAsVxqVNzXsCL85SNG72Z0v1HCE39qHAfKjTKyto06DwU4bPQnsrtiNRqRhjh2s9eLiy6L5VoLK5vCegoPLyz6HHhkBb137AdeC5HTx64rgHSMvDGn1%2BQZ5X4%2FFoU7uY%2FIF%2FH8pjvLFg4wP81XomOudi%2FXJx9uTV1pvwMTEoFqBbYta7TF7SJVnQIYKk4ZJJ2Y8mn6JyHQNIXF0%2BVqmdkhrQ%3D%3D&trade_no=2020051422001476430500986531&auth_app_id=2016101000655497&version=1.0&app_id=2016101000655497&sign_type=RSA2&seller_id=2088102178980105&timestamp=2020-05-14+09%3A46%3A21 HTTP/1.1"

o = urlparse(url)
    # 获取到URL的各种参数
query = parse_qs(o.query)
print(query)