import requests
from bs4 import BeautifulSoup
import xlsxwriter


def parse():
    proxies = {
        'http': 'http://proxy.omgtu:8080',
        'https': 'http://proxy.omgtu:8080'
    }
    headers = {
        'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 YaBrowser/24.4.0.0 Safari/537.36'
    }
    url = 'https://hh.ru/search/vacancy?text=Python&area=1249&hhtmFrom=main&hhtmFromLabel=vacancy_search_line'
    page = requests.get(url, proxies=proxies, headers=headers, verify=False)
    print(page.status_code)

    soup = BeautifulSoup(page.text, "html.parser")
    block = soup.findAll('span', class_='serp-item__title-link serp-item__title')

    workbook = xlsxwriter.Workbook('vag.xlsx')
    worksheet = workbook.add_worksheet()

    vag = 0
    description = ''

    for data in block:
        description = data.text
        worksheet.write(vag, 0, description)
        vag += 1

    workbook.close()

parse()
