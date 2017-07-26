#說明:此為抓取vg官網的每日一卡,鑒於每日一卡的網址並非都相同,且每日卡的數量可能不相同,得必須每日一定時間(9:30)抓取
#最後取出來的為jpg,且名字為"vgd_today072601.jpg"(舉例)
#需安裝套件 requests,bs4,datetime,workalendar
import requests
from bs4 import BeautifulSoup
import datetime
from workalendar.asia import Japan
cal = Japan()
if cal.is_working_day(datetime.datetime.now()): #確認是否為日本節日,工作日為True(會執行)
    res = requests.get('http://cf-vanguard.com/todays-card/')
    soup = BeautifulSoup(res.text, "html.parser")
    everyday_cardlist=soup.find_all("img", {"alt":"【カードファイト!! ヴァンガード】今日のカード"})
    for i in range(len(everyday_cardlist)):
        img_res = requests.get("http://cf-vanguard.com"+everyday_cardlist[i]['src']).content
        with open(r'C:\Users\User\Desktop\VG\vg_todays_card\\'+'vgd_today'+str(datetime.datetime.now())[:10].replace("-","")+'0'+str(i+1)+'.jpg', 'wb') as handler:
            handler.write(img_res)
        del img_res