import asyncio
from bs4 import BeautifulSoup 
import requests
from io import BytesIO
from PIL import Image
async def download_image(link):
    return Image.open(BytesIO(requests.get(link).content)).convert("RGB")
async def parser(nuklir):
    source=requests.get(f"https://nhentai.net/g/{nuklir}").text
    parsing=BeautifulSoup(source, 'html.parser')
    komik=[]
    id_=""
    for i in parsing.find_all('a',class_='gallerythumb'):
        if i('img'):
            komik.append(download_image('https://i'+i('img')[0]['data-src'][9:-5]+'.jpg'))
    z=await asyncio.gather(*komik)
    return z[0].save(f"{nuklir}.pdf", save_all=True, append_images=z[1:])