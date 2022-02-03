#!/usr/bin/python
# -*- coding:utf-8 -*-

import threading
import re, requests, time, base64, fire

requests.packages.urllib3.disable_warnings()
session = requests.Session()
result = []
# s = '''city=guangzhou && js_name="js/jquery.js"'''
# o = 'output.txt'
# c = '''befor_router=; isUpgrade=; fofa_token=eyJhbGciOiJIUzUxMiIsImtpZCI6Ik5XWTVZakF4TVRkalltSTJNRFZsWXpRM05EWXdaakF3TURVMlkyWTNZemd3TUdRd1pUTmpZUT09IiwidHlwIjoiSldUIn0.eyJpZCI6MTI3MTcwLCJtaWQiOjEwMDA3NTY5MiwidXNlcm5hbWUiOiJEZW1vbkpvZSIsImV4cCI6MTY0MzU0Njk3NH0.gLzkRFi6qNOMIwr_lRdVclciQh_r2LrACAA4YWhgMDQQR-y5ksXRqEp5B3jNiaEgSw-ndSalQAHuRgECPm_vSA; user={"id":127170,"mid":100075692,"is_admin":false,"username":"DemonJoe","nickname":"DemonJoe","email":"demonjoe@126.com","avatar_medium":"https://nosec.org/missing.jpg","avatar_thumb":"https://nosec.org/missing.jpg","rank_name":"注册用户","rank_level":0,"company_name":"DemonJoe","coins":0,"credits":43,"expiration":"-","login_at":1643503774}; refresh_token=eyJhbGciOiJIUzUxMiIsImtpZCI6Ik5XWTVZakF4TVRkalltSTJNRFZsWXpRM05EWXdaakF3TURVMlkyWTNZemd3TUdRd1pUTmpZUT09IiwidHlwIjoiSldUIn0.eyJpZCI6MTI3MTcwLCJtaWQiOjEwMDA3NTY5MiwidXNlcm5hbWUiOiJEZW1vbkpvZSIsImV4cCI6MTY0Mzc2Mjk3NCwiaXNzIjoicmVmcmVzaCJ9.EFjRRJpUWM6gJgHi6iBYThB9-4F6XQ3Fgn1tBp0D22EAZfhspiaVz652CQ0XmI8edUM7m3FJAUEy94mOBKY89A; Hm_lvt_b5514a35664fd4ac6a893a1e56956c97=1643376671,1643498406,1643503775,1643503786; Hm_lpvt_b5514a35664fd4ac6a893a1e56956c97=1643506790'''

def fofasc(s,o,c):
    try:
        c = c.encode('utf-8')
        sbase64 = (base64.b64encode(s.encode('utf-8'))).decode('utf-8')
        cookies = {'cookie': c}
        for city in open('full_CityDict.txt', 'r'):
            s = s + '&& status_code=200' + '&& city=' + city.strip()
            for i in range(1, 6):
                url = "https://fofa.info/result?&qbase64=" + sbase64 + "&page_size=10&page="+str(i)
                # url = "https://fofa.info/result?qbase64=Y2l0eT0iQ2hlbmdkdSI%3D"
                response = session.get(url, headers=cookies, verify=False).text
                # print(response)
                result = re.findall('''<span class="aSpan"><a href="(.*?)"''', response, re.S )
                print(result)
                if result != []:
                    for rs in result:
                        with open(o, mode="a+") as f:
                            f.write(str(rs) + "\n")
                else:
                    print("已经获取不到任何数据，爬取完毕！")
                    break
                time.sleep(2)
    except KeyboardInterrupt:
        print('用户退出')

if __name__ == '__main__':
    fire.Fire(fofasc)
    # fofasc(s, o, c)