from email import header
from operator import delitem
import requests
from bs4 import BeautifulSoup as BS
import csv
import time


urls = ['/en--a/', '/en--b/', '/en--c/', '/en--d/', '/en--e/', '/en--f/', '/en--g/', '/en--h/', '/en--i/', '/en--j/', '/en--k/', '/en--l/', '/en--m/', '/en--n/', '/en--o/', '/en--p/', '/en--q/', '/en--r/', '/en--s/', '/en--t/', '/en--u/', '/en--v/', '/en--w/', '/en--x/', '/en--y/', '/en--z/', '/nums--digits/', '/ru--a/', '/ru--b/', '/ru--v/', '/ru--g/', '/ru--d/', '/ru--e/', '/ru--ie/', '/ru--zh/', '/ru--z/', '/ru--i/', '/ru--y/', '/ru--k/', '/ru--l/', '/ru--m/', '/ru--n/', '/ru--o/', '/ru--p/', '/ru--r/', '/ru--s/', '/ru--t/', '/ru--u/', '/ru--f/', '/ru--h/', '/ru--ts/', '/ru--ch/', '/ru--sh/', '/ru--shch/', '/ru--thd/', '/ru--iy/', '/ru--tsf/', '/ru--ee/', '/ru--yu/', '/ru--ya/']

def get_content(url):
    header = {
        'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.71 Safari/537.36', 
        'Accept' : 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9'
    }
    resp = requests.get(f'https://www.ozon.ru/brand{url}', headers=header)
    file_name = url.strip('/') + '.csv'
    time.sleep(3)
    rows = []
    # rows3 = []
    # rows = []
    # rows_text = []
    # rows_link = []

    if resp.status_code == 200:
        page = BS(resp.text, 'html.parser')
        brands = page.find(class_='l4h')
        if brands == None:
            print('ПУСТАЯ СТРАНИЦА', url)
            return
        else:
            print('РАБОТАЕМ', url)
            list_brands = brands.find_all('a', attrs={'class':'l5h'})
            brands_final = list_brands

            for b_text in brands_final:
                b_link = b_text
                b_text = b_text.text
                b_text = b_text.replace(' ','')
                b_text = b_text.replace('\n','')
                b_link = 'https://www.ozon.ru' + b_link.get('href')
                rows.append (
                    [b_text, b_link]
                    )
            if rows == []:
                return
            else:
                if 'en' in url:
                    with open(file_name, 'w', newline='', encoding='utf-8') as f:
                        writer = csv.writer(f, delimiter=';')
                        for sublist in rows:
                            writer.writerow(sublist)
                elif 'ru' in url:
                    with open(file_name, 'w', newline='', encoding='utf-16') as f:
                        writer = csv.writer(f, delimiter=';')
                        for sublist in rows:
                            writer.writerow(sublist)
                            
            print(url, 'ГОТОВА')

def parse_content():
    for url in urls:
        get_content(url)

if __name__ == '__main__':
    parse_content()



        # try:
        #     if rows == []:
        #         return
        #     else:
        #         if 'en' in url:
        #             with open(file_name, 'w', newline='', encoding='utf-8') as f:
        #                 writer = csv.writer(f, delimiter=';')
        #                 for sublist in rows:
        #                     writer.writerow(sublist)
        #         elif 'ru' in url:
        #             with open(file_name, 'w', newline='', encoding='cp1251') as f:
        #                 writer = csv.writer(f, delimiter=';')
        #                 for sublist in rows:
        #                     writer.writerow(sublist)
        # except Exception:
        #     return
        # print(url)
    

    #     rows1 = []
    #     rows2 = []
    #     for i in range(len(rows)):
    #         abc = rows[i]
    #         rows1.append(abc[0])
    #         rows2.append(abc[1])
    #     convert_list_text = ' '.join([str(e) for e in rows1])
    #     convert_list_link = ' '.join([str(e) for e in rows2])        

    # tmp = {'Name': convert_list_text, 'Link': convert_list_link}
    # rows3.append(tmp)   


    # csv_title = ['Name', 'Link']   
    # with open('brands.csv', 'w', newline='', encoding = 'utf-8') as f:
    #     wr = csv.DictWriter(f, fieldnames=csv_title, delimiter = ';')
    #     wr.writeheader()
    #     wr.writerows(rows3)



    #     for brands_text in brands_final:
    #         brands_text = brands_text.text
    #         brands_text = brands_text.replace(' ', '')
    #         brands_text = brands_text.replace('\n', '')
    #         rows_text.append(
    #             [brands_text]
    #             )
    #     #print(rows_text)
    #     for brands_link in brands_final:
    #         brands_link = 'https://www.ozon.ru/brand' + brands_link.get('href')
    #         rows_link.append (
    #             [brands_link]
    #             )
    #     #print(rows_link)

    # tmp = {'Name': rows_text, 'Link': rows_link}
    # rows.append(tmp)

    # csv_title = ['Name', 'Link']   
    # with open('brands.csv', 'w', newline='', encoding = 'utf-8') as f:
    #     wr = csv.DictWriter(f, fieldnames=csv_title, delimiter = ';')
    #     wr.writeheader()
    #     wr.writerows(rows)




    
    #     for link in brands_final:
    #         rows.append (
    #             [link.text, link.get('href')]
    #             )
    #     rows1 = []
    #     rows2 = []
    #     for i in range(len(rows)):
    #         abc = rows[i]
    #         rows1.append(abc[0])
    #         rows2.append(abc[1])
    #     convert_list_text = ' '.join([str(e) for e in rows1])
    #     convert_list_link = ' '.join([str(e) for e in rows2])        

    #     tmp = {'Name': convert_list_text, 'Link': convert_list_link}
    #     rows3.append(tmp)   

    # csv_title = ['Name', 'Link']   
    # with open('brands.csv', 'w', newline='', encoding = 'utf-8') as f:
    #     wr = csv.DictWriter(f, fieldnames=csv_title, delimiter = ';')
    #     wr.writeheader()
    #     wr.writerows(rows3)

    

