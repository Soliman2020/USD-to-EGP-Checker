from bs4 import BeautifulSoup
import time, requests

url = 'https://www.xe.com/currencyconverter/convert/?Amount=1&From=USD&To=EGP'

response = requests.get(url, headers={'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/15.3 Safari/605.1.15'})
response.raise_for_status()

soup = BeautifulSoup(response.text, 'html.parser')

t = time.localtime()
current_time = time.strftime("%H:%M:%S", t)

# soup select use css manner
element = soup.select('p.result__BigRate-sc-1bsijpp-1.iGrAod')
elem = element[0].text
rate = round(float(elem[:8]),5)
print(soup.title.text)
print(f"USD = {rate} EGP @ {current_time}")
