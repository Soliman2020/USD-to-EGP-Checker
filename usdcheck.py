import os, time, bs4, requests

print('USD to EGP Currency Checker.\nUpdates every second.')

url = 'https://www.xe.com/currencyconverter/convert/?Amount=1&From=USD&To=EGP'
while True:	
	webPage = requests.get(url, headers={'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/15.3 Safari/605.1.15'})
	webPage.raise_for_status()
	
	soup = bs4.BeautifulSoup(webPage.text, 'html.parser')
	
	t = time.localtime()
	current_time = time.strftime("%H:%M:%S", t)

	element = soup.select('#__next > div:nth-child(2) > div.fluid-container__BaseFluidContainer-qoidzu-0.gJBOzk > section > div:nth-child(2) > div > main > form > div:nth-child(2) > div:nth-child(1) > p.result__BigRate-sc-1bsijpp-1.iGrAod')
	elem = element[0].text.strip()
	final = elem[0:8]
	time.sleep(0.5)
	print(f"USD to EGP: {final} Time: {current_time}")

#10:56:05


