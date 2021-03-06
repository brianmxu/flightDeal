# -*- coding: utf-8 -*-
"""
Created on Fri Jan  1 17:27:48 2016

adding additional comment
@author: brianxu
"""

from urllib import urlopen
import urllib2
from bs4 import BeautifulSoup
from bs4.diagnose import diagnose 
import os, csv
def dallasEmail():
    #req = urllib2.Request('http://www.theflightdeal.com/category/flight-deals/dallas/', headers={ 'User-Agent': 'Mozilla/5.0' })
    #html = urllib2.urlopen(req).read()
    #diagnose(html)
    #print html
    
    #ticker = raw_input("Enter the city: ")
    #URL = 'http://finance.yahoo.com/q/hp?s=' + ticker.upper() + '+Historical+Prices'
    #headers =  "'User-Agent': 'Mozilla/5.0'" 
    URL = 'http://www.theflightdeal.com/category/flight-deals/dallas/'
    #page = urlopen(URL)
    hdr = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11',
           'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
           'Accept-Charset': 'ISO-8859-1,utf-8;q=0.7,*;q=0.3',
           'Accept-Encoding': 'none',
           'Accept-Language': 'en-US,en;q=0.8',
           'Connection': 'keep-alive'}
    #page = urllib2.Request(URL,headers=hdr)
    #print page.read()
    
    req = urllib2.Request(URL, headers=hdr)
    
    try:
        page = urllib2.urlopen(req)
    except urllib2.HTTPError, e:
        print e.fp.read()
    
    content = page.read()
    soup = BeautifulSoup(content)
    #print soup.prettify()
    #deal = soup.find_all("div", class_="entry-content")
    deal = soup.find_all("h1", class_="post-title")
    title = deal[0].get_text().encode("utf-8")
    link = deal[0].a["href"].encode("utf-8")
    
    import smtplib
     
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login("bwayhntester@gmail.com", "rovertester")
     
    msg = title + "\n" + link
    server.sendmail("brian.m.xu@gmail.com", "brian.m.xu@gmail.com", msg)
    server.quit()

from apscheduler.scheduler import Scheduler

sched = Scheduler()
sched.daemonic = False
sched.start()

sched.add_cron_job(dallasEmail,  day='1-31', hour = 18, minute = 27)
'''
soup = BeautifulSoup(page)
print soup
deal = soup.find_all("div", class_="entry-content")

print deal
table = {}
'''
'''
for element in range(0, len(price)):
    if element%7 == 0:
        if str(price[element].get_text()).lstrip() != "* Close price adjusted for dividends and splits.":
            current = str(price[element].get_text())         
            table[str(price[element].get_text())]={}
        
for element in range(0,len(price)):
    if element%7 ==1:
        table[str(price[element-1].get_text())]["Open"] = str(price[element].get_text())
    elif element%7 ==2:
        table[str(price[element-2].get_text())]["High"] = str(price[element].get_text())
    elif element%7 ==3:
        table[str(price[element-3].get_text())]["Low"] = str(price[element].get_text())
    elif element%7 ==4:
        table[str(price[element-4].get_text())]["Close"] = str(price[element].get_text())
    elif element%7 ==5:
        table[str(price[element-5].get_text())]["Volume"] = str(price[element].get_text())
    elif element%7 ==6:
        table[str(price[element-6].get_text())]["Adjusted Close"] = str(price[element].get_text())

for item in table:
    print item + ": Open:" + table[item]["Open"] + "\n\t\t" + "High: " + table[item]["High"]
'''
