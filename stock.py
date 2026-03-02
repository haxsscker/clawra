import akshare as ak
import requests
import pandas as pd

def get_stock_data_custom():
    """
    自定义请求头，绕过服务器封禁检测
    """
    url = "https://82.push2.eastmoney.com/api/qt/clist/get"
    
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
                      "AppleWebKit/537.36 (KHTML, like Gecko) "
                      "Chrome/120.0.0.0 Safari/537.36",
        "Referer": "https://quote.eastmoney.com/center/gridlist.html",
        "Accept": "text/javascript, application/javascript, */*",
        "Accept-Language": "zh-CN,zh;q=0.9,en;q=0.8",
        "Accept-Encoding": "gzip, deflate, br",
        "Connection": "keep-alive",
    }
    
    params = {
        "pn": 1,
        "pz": 50,
        "po": 1,
        "np": 1,
        "ut": "bd1d9ddb04089700cf9c27f6f7426281",
        "fltt": 2,
        "invt": 2,
        "fid": "f3",
        "fs": "m:0+t:6,m:0+t:13,m:0+t:80,m:1+t:2,m:1+t:23",
        "fields": "f1,f2,f3,f4,f5,f6,f7,f8,f9,f10,f12,f13,f14,f15,f16,f17,f18",
        "_": int(__import__('time').time() * 1000)
    }
    
    session = requests.Session()
    
    try:
        response = session.get(
            url,
            headers=headers,
            params=params,
            timeout=15,
            verify=True
        )
        response.raise_for_status()
        return response.json()
        
    except Exception as e:
        print(f"❌ 自定义请求失败：{e}")
        return None

data = get_stock_data_custom()
print(data)
