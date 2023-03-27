import urllib.request
import re
from PIL import Image

def download_html(url):  # 获取某网站的html源代码
    request_header = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:109.0) Gecko/20100101 Firefox/111.0",
    }
    req = urllib.request.Request(url=url, headers=request_header)
    response = urllib.request.urlopen(req)
    html = response.read().decode("utf-8")
    return html


url = "https://mxd.web.sdo.com/web6/news/newsList.asp?CategoryID=273"
html = download_html(url)
url_partten = "id=[0-9]+\&CategoryID=273\" target=\"_blank\">周日"
target_urls = re.findall(url_partten, html)
target_id = 0
for url in target_urls:
    id = int(url[3:9])
    if id > target_id:
        target_id = id
target_url = "https://mxd.web.sdo.com/web6/news/newsContent.asp?id={id}&CategoryID=273".format(id=target_id)
target_html = download_html(target_url)
jpg_partten = "https://fu5.web.sdo.com/10036/[0-9]+/[0-9]+\.jpg"
jpg_url = re.findall(jpg_partten,target_html)
urllib.request.urlretrieve(jpg_url[0],'target.jpg')
img = Image.open('target.jpg')
img.show()
