import requests
from cachetools import TTLCache, cached
from loguru import lugger

cache = TTLCache(maxsize=100, ttl=3*60*60)

@cached(cache)
def get_exchange_rate(base_currency: str, target_currency:str) -> str:
    """get exchange rate form exchangerate api

    :param base_currency: base currency to exchange
    :type base_currency: str
    :param target_currency: target currency to change to
    :type target_currency: str
    :return: exchange rate
    :rtype: str
    """
    url = f"https://api.exchangerate-api.com/v4/latest/{base_currency}"
    response = requests.get(url)
    data = response.json()
    if response.status_code == 200:
        return data["rates"][target_currency], data["time_last_updated"]
    lugger.success(response)


def convert_currency(amount: int, exchange_rate : int) -> int:
    """Concvert currency to amount of targer_curreny

    :param amount: aoumnt of currency
    :type amount: int
    :param exchange_rate: exchange rate to target currency
    :type exchange_rate: int
    :return: converted amount currency
    :rtype: int
    """
    return amount * exchange_rate
