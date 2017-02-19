import json
# -*- coding: utf-8 -*-  
import requests
import re
"""This module can query the internet IP address of myself, return ip adress, and the location.
   Version 1.0
"""

def ipquery():
    """Query internet IP address of mine.
    Args:
        None
    Return:
        A String with an internet IP address of myself.
    """
    url = "http://www.ip138.com/ip2city.asp"
    resp = requests.get(url)
    resp.encoding = 'gbk'
    ip_str = re.search(r'\d+\.\d+\.\d+\.\d+', resp.text).group(0)
    return ip_str
    
def locationquery(ip_address):
    """Query internet IP address of mine.
    Args:
        A String with an internet IP address of myself.
    Return:
        Strings with the location of province and the city.
    """
    url2 = 'http://ip.taobao.com/service/getIpInfo.php?ip=' + ip_address
    resp2 = requests.get(url2)
    ip_js = json.loads(resp2.text, encoding='utf-8')
    province_str = ip_js['data']['region']
    city_str = ip_js['data']['city']
    return province_str, city_str
