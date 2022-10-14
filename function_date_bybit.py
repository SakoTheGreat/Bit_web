from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait as wait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException
from bs4 import BeautifulSoup
from time import sleep
from tqdm import tqdm



# driver.maximize_window() otkrit v bolshom okne



sell_purchase = {'purchase': '1', 'sell': '0'}
token = ["USDT", 'BTC']
payment_method = {'Tinkoff': '75', 'Rosbank': '185', 'Raiffeisenbank': '64'}
all_date = {
'price_purchase_usdt': [],
'price_sell_usdt': [],
'price_purchase_btc': [],
'price_sell_btc': [],    
}

driver = Chrome()
link_date = "https://www.bybit.com/fiat/trade/otc/?actionType=" + sell_purchase['purchase'] + '&token=' + token[0] + '&fiat=RUB&paymentMethod=' + payment_method['Tinkoff']
driver.get(link_date)
search_price = driver.find_element(By.CSS_SELECTOR, 'div.trade-table__wrapper span.price-amount')
all_date['price_purchase_usdt'].append({'Tinkoff': search_price.text})
driver.close()

driver = Chrome()
link_date = "https://www.bybit.com/fiat/trade/otc/?actionType=" + sell_purchase['sell'] + '&token=' + token[0] + '&fiat=RUB&paymentMethod=' + payment_method['Tinkoff']
driver.get(link_date)       
search_price = driver.find_element(By.CSS_SELECTOR, 'div.trade-table__wrapper span.price-amount')
all_date['price_sell_usdt'].append({'Tinkoff': search_price.text})
driver.close()


driver = Chrome()
link_date = "https://www.bybit.com/fiat/trade/otc/?actionType=" + sell_purchase['purchase'] + '&token=' + token[0] + '&fiat=RUB&paymentMethod=' + payment_method['Rosbank']
driver.get(link_date)       
search_price = driver.find_element(By.CSS_SELECTOR, 'div.trade-table__wrapper span.price-amount')
all_date['price_purchase_usdt'].append({'Rosbank': search_price.text})
driver.close()


driver = Chrome()
link_date = "https://www.bybit.com/fiat/trade/otc/?actionType=" + sell_purchase['sell'] + '&token=' + token[0] + '&fiat=RUB&paymentMethod=' + payment_method['Rosbank']
driver.get(link_date)       
search_price = driver.find_element(By.CSS_SELECTOR, 'div.trade-table__wrapper span.price-amount')
all_date['price_sell_usdt'].append({'Rosbank': search_price.text})
driver.close()

driver = Chrome()
link_date = "https://www.bybit.com/fiat/trade/otc/?actionType=" + sell_purchase['purchase'] + '&token=' + token[0] + '&fiat=RUB&paymentMethod=' + payment_method['Raiffeisenbank']
driver.get(link_date)       
search_price = driver.find_element(By.CSS_SELECTOR, 'div.trade-table__wrapper span.price-amount')
all_date['price_purchase_usdt'].append({'Raiffeisenbank': search_price.text})
driver.close()


driver = Chrome()
link_date = "https://www.bybit.com/fiat/trade/otc/?actionType=" + sell_purchase['sell'] + '&token=' + token[0] + '&fiat=RUB&paymentMethod=' + payment_method['Raiffeisenbank']
driver.get(link_date)       
search_price = driver.find_element(By.CSS_SELECTOR, 'div.trade-table__wrapper span.price-amount')
all_date['price_sell_usdt'].append({'Raiffeisenbank': search_price.text})
driver.close()

driver = Chrome()
link_date = "https://www.bybit.com/fiat/trade/otc/?actionType=" + sell_purchase['purchase'] + '&token=' + token[1] + '&fiat=RUB&paymentMethod=' + payment_method['Tinkoff']
driver.get(link_date)       
search_price = driver.find_element(By.CSS_SELECTOR, 'div.trade-table__wrapper span.price-amount')
all_date['price_purchase_btc'].append({'Tinkoff': search_price.text})
driver.close()

driver = Chrome()
link_date = "https://www.bybit.com/fiat/trade/otc/?actionType=" + sell_purchase['sell'] + '&token=' + token[1] + '&fiat=RUB&paymentMethod=' + payment_method['Tinkoff']
driver.get(link_date)       
search_price = driver.find_element(By.CSS_SELECTOR, 'div.trade-table__wrapper span.price-amount')
all_date['price_sell_btc'].append({'Tinkoff': search_price.text})
driver.close()

driver = Chrome()
link_date = "https://www.bybit.com/fiat/trade/otc/?actionType=" + sell_purchase['purchase'] + '&token=' + token[1] + '&fiat=RUB&paymentMethod=' + payment_method['Rosbank']
driver.get(link_date)       
search_price = driver.find_element(By.CSS_SELECTOR, 'div.trade-table__wrapper span.price-amount')
all_date['price_purchase_btc'].append({'Rosbank': search_price.text})
driver.close()


driver = Chrome()
link_date = "https://www.bybit.com/fiat/trade/otc/?actionType=" + sell_purchase['sell'] + '&token=' + token[1] + '&fiat=RUB&paymentMethod=' + payment_method['Rosbank']
driver.get(link_date)       
search_price = driver.find_element(By.CSS_SELECTOR, 'div.trade-table__wrapper span.price-amount')
all_date['price_sell_btc'].append({'Rosbank': search_price.text})
driver.close()

driver = Chrome()
link_date = "https://www.bybit.com/fiat/trade/otc/?actionType=" + sell_purchase['purchase'] + '&token=' + token[1] + '&fiat=RUB&paymentMethod=' + payment_method['Raiffeisenbank']
driver.get(link_date)       
search_price = driver.find_element(By.CSS_SELECTOR, 'div.trade-table__wrapper span.price-amount')
all_date['price_purchase_btc'].append({'Raiffeisenbank': search_price.text})
driver.close()

driver = Chrome()
link_date = "https://www.bybit.com/fiat/trade/otc/?actionType=" + sell_purchase['sell'] + '&token=' + token[1] + '&fiat=RUB&paymentMethod=' + payment_method['Raiffeisenbank']
driver.get(link_date)       
search_price = driver.find_element(By.CSS_SELECTOR, 'div.trade-table__wrapper span.price-amount')
all_date['price_sell_btc'].append({'Raiffeisenbank': search_price.text})
driver.close()


print(all_date)