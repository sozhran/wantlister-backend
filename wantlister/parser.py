from re import search
from selenium import webdriver

def get_marketplace_ids_for_release(release_id: str):
    baseurl = "https://www.discogs.com/sell/release/"
    driver = webdriver.Chrome()
    sell_ids = []
    regexp = r'(?<=sell\/item\/)\S+(?=")'

    url = baseurl + release_id

    driver.get(url)

    source = driver.page_source
    driver.quit()

    for line in source.split("\n"):
        if "item_description_title" in line:
            id = search(regexp, line).group()
            sell_ids.append(id)

    print(sell_ids)

get_marketplace_ids_for_release("1926095")