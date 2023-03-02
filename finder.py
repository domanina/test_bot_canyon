from playwright.sync_api import sync_playwright

url = "https://www.canyon.com/en-de/road-bikes/race-bikes/ultimate/cf-sl/ultimate-cf-sl-7-di2/3317.html?dwvar_3317_pv_rahmenfarbe=R101_P01"
def run(playwright) -> str:

    browser = playwright.chromium.launch()
    page = browser.new_page()
    page.goto(url)

    name = page.locator("xpath=//h1[contains(@class, 'productDescription__productName')]").inner_text()
    sizes = page.locator("xpath=//li[contains(@class, 'productConfiguration__optionListItem')]")
    xs_size = sizes.locator("xpath=//*[@data-product-size='L']").inner_text()
    inner_texts = xs_size.split("\n")

    message = f"{name} in size {inner_texts[0]}, {inner_texts[2]} - "
    if "Delivery" in inner_texts:
        message += "ORDER NOW!"
    else:
        message += "CANT ORDER NOW"

    browser.close()
    return message

#
# with sync_playwright() as playwright:
#     run(playwright)