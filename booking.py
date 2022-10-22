import requests
from bs4 import BeautifulSoup
import csv
import os
from datetime import datetime


starttime = datetime.now()

urls = [
    'https://www.booking.com/searchresults.en-gb.html?label=gen173nr-1BCAEoggI46AdIM1gEaFCIAQGYAQm4ARfIAQzYAQHoAQGIAgGoAgO4AuzvyZoGwAIB0gIkNDVhMjMyMjgtZmVlOS00YTk2LWI2MWUtZWNjZTVkNzU3ZTM12AIF4AIB&sid=d38aceb99259b2907d730c9c8059ee2a&aid=304142&ss=Smolyan&lang=en-gb&sb=1&src_elem=sb&src=searchresults&group_adults=2&no_rooms=1&group_children=0&sb_travel_purpose=leisure&offset=0',
    'https://www.booking.com/searchresults.en-gb.html?label=gen173nr-1BCAEoggI46AdIM1gEaFCIAQGYAQm4ARfIAQzYAQHoAQGIAgGoAgO4AuzvyZoGwAIB0gIkNDVhMjMyMjgtZmVlOS00YTk2LWI2MWUtZWNjZTVkNzU3ZTM12AIF4AIB&sid=d38aceb99259b2907d730c9c8059ee2a&aid=304142&ss=Smolyan&lang=en-gb&sb=1&src_elem=sb&src=searchresults&group_adults=2&no_rooms=1&group_children=0&sb_travel_purpose=leisure&offset=25',
    'https://www.booking.com/searchresults.en-gb.html?label=gen173nr-1BCAEoggI46AdIM1gEaFCIAQGYAQm4ARfIAQzYAQHoAQGIAgGoAgO4AuzvyZoGwAIB0gIkNDVhMjMyMjgtZmVlOS00YTk2LWI2MWUtZWNjZTVkNzU3ZTM12AIF4AIB&sid=d38aceb99259b2907d730c9c8059ee2a&aid=304142&ss=Smolyan&lang=en-gb&sb=1&src_elem=sb&src=searchresults&group_adults=2&no_rooms=1&group_children=0&sb_travel_purpose=leisure&offset=50',
    'https://www.booking.com/searchresults.en-gb.html?label=gen173nr-1BCAEoggI46AdIM1gEaFCIAQGYAQm4ARfIAQzYAQHoAQGIAgGoAgO4AuzvyZoGwAIB0gIkNDVhMjMyMjgtZmVlOS00YTk2LWI2MWUtZWNjZTVkNzU3ZTM12AIF4AIB&sid=d38aceb99259b2907d730c9c8059ee2a&aid=304142&ss=Smolyan&lang=en-gb&sb=1&src_elem=sb&src=searchresults&group_adults=2&no_rooms=1&group_children=0&sb_travel_purpose=leisure&offset=75',
]

headers = {
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Safari/537.36',
}

# count = 1
# for url in urls:
#     req = requests.get(url, headers=headers)
#     src = req.text
#     with open(f'html/{count}_index.html', 'w', encoding='utf-8') as file:
#         file.write(src)
#     count +=1

dir_name = r'C:\Python\booking\html'
list = os.listdir(dir_name)

with open(f'booking.csv', 'w', newline='', encoding='utf-8') as file:
    writer = csv.writer(file)
    writer.writerow(
        (
            "Title",
            'Image Link',
            'URL',
            'Distance',
            'Short Description',
            'Reviews',
            'Review total',
            'Full Description',
            'Facilities',
        )
    )

for item in list:
    with open(fr'C:\Python\booking\html\{item}', encoding='utf-8') as file:
        src = file.read()
    soup = BeautifulSoup(src, 'lxml')
    all_item = soup.find_all('div', class_='b978843432')
    for tov_item in all_item:
        title = soup.find('div', class_='fcab3ed991 a23c043802').text
        image_link = soup.find('div', class_='c90a25d457').find('a').find('img').get('src')
        url_item = soup.find('div', class_='c90a25d457').find('a').get('href')
        distance = soup.find('div', class_='a1fbd102d9').find('span', class_='cb5ebe3ffb').text
        short_description = soup.find('div', class_='a1b3f50dcd b2fe1a41c3 a7c67ebfe5 d19ba76520 d14b211b4f').find('div', class_='b1e6dd8416 aacd9d0b0a').find('div', class_='a1b3f50dcd f7c6687c3d ef8295f3e6').find('div', class_='d8eab2cf7f').text
        rewiews = None
        rewiew_total = soup.find('div', class_='d8eab2cf7f c90c0a70d3 db63693c62').text

        req = requests.get('url_item', headers=headers)
        src1 = req.text


        soup1 = BeautifulSoup(src1, 'lxml')
        full_description = soup1.find('div', id_='property_description_content').text.strip()
        facilities = soup1.find('div', class_='hotel-facilities__list').text.strip()



    print(all_item)