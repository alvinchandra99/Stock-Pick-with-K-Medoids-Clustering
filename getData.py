import requests
from bs4 import BeautifulSoup
import bs4
import numpy as np
import time
import pandas as pd
import datetime


LQ45 = ["ACES", "ADRO", "AKRA", "ANTM", "ASII", "BBCA", "BBNI", "BBRI", "BBTN",  "BMRI", "BSDE", "BTPS", "CPIN",
        "CTRA", "ERAA", "EXCL", "GGRM", "HMSP", "ICBP", "INCO", "INDF","INKP", "INTP", "ITMG", "JPFA", "JSMR",
         "KLBF", "MDKA", "MIKA",  "MNCN", "PGAS", "PTBA", "PTPP", "PWON", "SCMA", "SMGR", "SMRA", "SRIL", "TBIG", 
         "TKIM", "TLKM", "TOWR", "UNTR", "UNVR", "WIKA"]
total_market_cap = []
total_beta = []
total_PE = []
total_EPS = []
total_harga_sekarang = []
total_cash = []
total_BVPS = []
negative_PE = []
USDtoIDR = 14100

# Fungsi untuk memperbarui databse


def updateData():
    for x in LQ45:
        url = "https://finance.yahoo.com/quote/{}.JK?p={}.JK&.tsrc=fin-srch".format(
            x, x)

        # Mengambil Data Fundamental
        r = requests.get(url)
        soup = bs4.BeautifulSoup(r.text, 'html.parser')
        market_cap = soup.find('div', {'class': 'D(ib) W(1/2) Bxz(bb) Pstart(12px) Va(t) ie-7_D(i) ie-7_Pos(a) smartphone_D(b) smartphone_W(100%) smartphone_Pstart(0px) smartphone_BdB smartphone_Bdc($seperatorColor)'}
                               ).find_all('span', {'class': 'Trsdu(0.3s)'})[0].text
        beta = soup.find('div', {'class': 'D(ib) W(1/2) Bxz(bb) Pstart(12px) Va(t) ie-7_D(i) ie-7_Pos(a) smartphone_D(b) smartphone_W(100%) smartphone_Pstart(0px) smartphone_BdB smartphone_Bdc($seperatorColor)'}
                         ).find_all('span', {'class': 'Trsdu(0.3s)'})[1].text
        PE = soup.find('div', {'class': 'D(ib) W(1/2) Bxz(bb) Pstart(12px) Va(t) ie-7_D(i) ie-7_Pos(a) smartphone_D(b) smartphone_W(100%) smartphone_Pstart(0px) smartphone_BdB smartphone_Bdc($seperatorColor)'}
                       ).find_all('span', {'class': 'Trsdu(0.3s)'})[2].text.replace(',', '.')
        EPS = soup.find('div', {'class': 'D(ib) W(1/2) Bxz(bb) Pstart(12px) Va(t) ie-7_D(i) ie-7_Pos(a) smartphone_D(b) smartphone_W(100%) smartphone_Pstart(0px) smartphone_BdB smartphone_Bdc($seperatorColor)'}
                        ).find_all('span', {'class': 'Trsdu(0.3s)'})[3].text.replace(',', '.')
        harga_sekarang = soup.find('div', {'class': 'D(ib) Va(m) Maw(65%) Ov(h)'}).find_all('span', {
            'class': 'Trsdu(0.3s) Fw(b) Fz(36px) Mb(-4px) D(ib)'})[0].text.replace('.00', '').replace(',', '')

        # Mengambil Data

        url2 = 'https://finance.yahoo.com/quote/{}.JK/key-statistics?p={}.JK'.format(
            x, x)
        r2 = requests.get(url2)
        soup2 = bs4.BeautifulSoup(r2.text, 'html.parser')
        cash = soup2.find('div', {'class': 'Mb(10px) Pend(20px) smartphone_Pend(0px)'}).find_all('div', {
            'class': 'Pos(r) Mt(10px)'})[4].find_all('td', {'class': 'Fw(500) Ta(end) Pstart(10px) Miw(60px)'})[0].text
        BVPS = soup2.find('div', {'class': 'Mb(10px) Pend(20px) smartphone_Pend(0px)'}).find_all('div', {
            'class': 'Pos(r) Mt(10px)'})[4].find_all('td', {'class': 'Fw(500) Ta(end) Pstart(10px) Miw(60px)'})[5].text

        # Filter untuk menghapus .xx
        if len(PE) > 6:
            PE = PE.replace(PE[-3:], '')
        if len(EPS) > 6:
            EPS = EPS.replace(EPS[-3:], '')

        # Jika EPS bernilai USD maka ubah ke IDR
        if float(EPS) > 0 and float(EPS) < 1:
            EPS = float(EPS) * USDtoIDR
            PER = int(harga_sekarang)/float(EPS)

        # Menganti Format kKe Juta
        if cash[-1:] == 'T':
            cash = cash.replace(cash[-1:], '')
            cash = float(cash) * 1000000000
        elif cash[-1:] == 'M':
            cash = cash.replace(cash[-1:], '')
            cash = float(cash) * 1000000
        elif cash[-1:] == 'B':
            cash = cash.replace(cash[-1:], '')
            cash = float(cash)

        # Menganti Format Market Cap
        market_cap = market_cap.replace(market_cap[-1:], '')
        market_cap = float(market_cap) * 1000000000

        # Menambahkan Data Kedalam Array
        total_market_cap.append(market_cap)
        total_beta.append(beta)
        total_PE.append(PE)
        total_EPS.append(EPS)
        total_harga_sekarang.append(harga_sekarang)
        total_cash.append(cash)
        total_BVPS.append(BVPS)

        # Jika EPS bernilai negatif maka beri tanda Y, Jika positif tanda N
        if float(EPS) == 0:
            negative_PE.append("Y")
            print("PE {} bernilai Negativ".format(x))
        else:
            negative_PE.append("N")
            print("Memproses Data {}".format(x))

        time.sleep(0.5)

    d = {'kode_saham': LQ45, 'Market_Cap': total_market_cap, 'Beta': total_beta, 'PE': total_PE,
         'EPS': total_EPS, 'harga_sekarang': total_harga_sekarang, 'Cash': total_cash, 'BVPS': total_BVPS, 'Negative PE': negative_PE}
    df = pd.DataFrame(d)
    return df.to_excel('DataSaham5.xlsx')


def getHistoryPrice():

    now = str(datetime.date.today())
    period2 = str(time.mktime(datetime.datetime.strptime(
        now, "%Y-%m-%d").timetuple())).replace('.0', '')
    period1 = int(period2) - 31536000
    for x in LQ45:
        url = 'https://query1.finance.yahoo.com/v7/finance/download/{}.JK?period1={}&period2={}&interval=1d&events=history&includeAdjustedClose=true'.format(x,
                                                                                                                                                             period1, period2)
        print(url)
        r = requests.get(url, allow_redirects=True)
        open('historyprice/{}.csv'.format(x), 'wb').write(r.content)
        time.sleep(1)
        print('Mendownload Data '+x)
