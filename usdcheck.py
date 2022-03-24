import os, time, bs4, requests

print('USD to EGP Currency Checker.\n')

url = 'https://www.xe.com/currencyconverter/convert/?Amount=1&From=USD&To=EGP'

# while True:	
response = requests.get(url, headers={'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/15.3 Safari/605.1.15'})
response.raise_for_status()

soup = bs4.BeautifulSoup(response.text, 'html.parser')

t = time.localtime()
current_time = time.strftime("%H:%M:%S", t)

element = soup.select('p.result__BigRate-sc-1bsijpp-1.iGrAod')
elem = element[0].text.strip()
rate = elem[:8]
# time.sleep(1)
print(f"USD to EGP: {rate} Time: {current_time}")
