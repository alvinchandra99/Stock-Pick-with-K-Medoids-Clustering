import requests
from bs4 import BeautifulSoup
import bs4
import numpy as np
import time
import pandas as pd
import datetime

total = []
LQ45 = ["ACES", "ADRO", "AKRA", "ANTM", "ASII", "BBCA", "BBNI", "BBRI", "BBTN",  "BMRI", "BSDE", "BTPS", "CPIN", "CTRA", "ERAA", "EXCL", "GGRM", "HMSP", "ICBP", "INCO", "INDF",
        "INKP", "INTP", "ITMG", "JPFA", "JSMR", "KLBF", "MDKA", "MIKA",  "MNCN", "PGAS", "PTBA", "PTPP", "PWON", "SCMA", "SMGR", "SMRA", "SRIL", "TBIG", "TKIM", "TLKM", "TOWR", "UNTR", "UNVR", "WIKA"]

for x in LQ45:
    url = "https://finance.yahoo.com/quote/{}.JK?p={}.JK&.tsrc=fin-srch".format(
        x, x)
    r = requests.get(url)
    soup = bs4.BeautifulSoup(r.text, 'html.parser')
    nama_perusahaan = soup.find('div', {
                                'class': 'D(ib) Mt(-5px) Mend(20px) Maw(56%)--tab768 Maw(52%) Ov(h) smartphone_Maw(85%) smartphone_Mend(0px)'}).find('h1').text
    panjang = len(nama_perusahaan) - 9
    print(nama_perusahaan[:panjang])
    total.append(nama_perusahaan[:panjang])
    time.sleep(0.2)

d = {'kode_saham': LQ45, 'Nama': total}
df = pd.DataFrame(d)
df.to_excel('namaperusahaan.xlsx')
