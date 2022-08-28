from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By


def get_driver():
    """
    This will Initialise the webdriver and return Driver.
    :return:
    """
    # set Options to make browsing Easy!!
    chrome_driver = Options()
    chrome_driver.add_argument("--disable-infobars")
    chrome_driver.add_argument("--no-sandbox")
    chrome_driver.add_argument("--headless")
    chrome_driver.add_argument("--disable-dev-shm-usage")
    chrome_driver.add_argument("--disable-blink-features=AutomationControlled")
    web_driver = webdriver.Chrome("D:\\Download\\chromedriver.exe", options=chrome_driver)
    return web_driver


if __name__ == "__main__":
    print("Creating Driver")
    driver = get_driver()
    driver.get(url="https://www.amazon.de/dp/000101742X")

    # Image is in the left column so take the left-column ID
    left_column = driver.find_element(By.ID, value="leftCol")
    image_tag = left_column.find_element(by=By.TAG_NAME, value="img")
    image_url = image_tag.get_attribute("src")

    product_column = driver.find_element(By.ID, value="centerCol")

    product_title = product_column.find_element(By.ID, value="productTitle")
    title = product_title.text

    product_price = product_column.find_element(By.XPATH, value='//*[@id="a-autoid-3-announce"]/span[2]/span')
    price = product_price.text

    product_description = product_column.find_element(By.XPATH, value='//*[@id="bookDescription_feature_div"]/div'
                                                                      '/div[1]')
    description = product_description.text

    print("The Product title is: " + title)
    print("The Product Image Url: " + image_url)
    print("The Price of the Product is: " + price)
    print("The Product description is: " + description)
