import requests

def get_exchange_rates(url):

    response = requests.get(url)

    try:
        if response.status_code == 200:
            exchange_rates = response.json()
            return exchange_rates
    except:
        print("Помилка при отриманні курсів валют")
        return None

if __name__ == "__main__":

    url = "https://bank.gov.ua/NBUStatService/v1/statdirectory/exchange?json"
    exchange_rates = get_exchange_rates(url)

    if exchange_rates:
        for rate in exchange_rates:
            print(f"{rate['exchangedate']}: 1 {rate['cc']} ({rate['txt']}) = {rate['rate']} UAH")
