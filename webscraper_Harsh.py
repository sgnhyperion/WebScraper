import requests
from bs4 import BeautifulSoup
from tabulate import tabulate

headers = {
    'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.0.0 Safari/537.36'
}

amazon_url = "https://www.amazon.in/ASIAN-Mens-Blue-Shorts-Shoes/dp/B07FRZNKS9/ref=sr_1_2?crid=2LEV7FK0WP0YQ&keywords=ASIAN%2B-%2BCOSCO%2BNavy%2BMen%27s%2BSports%2BRunning%2BShoes&nsdOptOutParam=true&qid=1699213199&sprefix=asian%2B-%2Bcosco%2Bnavy%2Bmen%27s%2Bsports%2Brunning%2Bshoes%2Caps%2C264&sr=8-2&th=1&psc=1"
snapdeal_url = "https://www.snapdeal.com/product/asian-cosco-navy-mens-sports/6917529671647200221#bcrumbSearch:asian%20shoe%20men"

# amazon_url = input("Please enter the product url of Amazon: ")
# print()
# snapdeal_url = input("Please enter the product url of Snapdeal: ")
try:
    # Amazon
    r = requests.get(amazon_url, headers=headers)
    soup = BeautifulSoup(r.text,features= 'html.parser')
    
    name = soup.find_all('span',class_="a-size-large product-title-word-break")[0]
    print()
    price = soup.find('span', {'class': 'a-price-whole'})

    if name:
       print((name.text.strip()))
    else:
        print("Amazon Name not found")
    print()
    if price:
        Amazon_price = (price.text)
    else:
        print("Amazon Price not found")
    # Snapdeal
    r2 = requests.get(snapdeal_url, headers=headers)
    soup2 = BeautifulSoup(r2.text, 'lxml')

    price2 = soup2.find('span', class_="payBlkBig")

    if price2:
        Snapdeal_price =  price2.text
    else:
        print("Snapdeal Price not found")

    data = [["Amazon ",Amazon_price],
            ["Snapdeal ",Snapdeal_price]]
    table = tabulate(data, headers=["Website","Price"], tablefmt="fancy_grid")
    print(table)
except Exception as e:
    print("Oops! An error occurred:", str(e))
    print("Please check the URL you've entered or it may be a server issue.")


