from core.browser import start_browser
from core.excel import load_excel
from core.form import fill_form

from selenium.webdriver.common.by import By

import time


URL = "https://rpachallenge.com/"

driver = start_browser()
driver.get(URL)

input(
    "\nBaixe o Excel e coloque challenge.xlsx na raiz do projeto.\n"
    "Pressione ENTER para continuar..."
)

dados = load_excel("challenge.xlsx")


# start challenge
driver.find_element(
    By.XPATH,
    "//button[text()='Start']"
).click()


for index, row in enumerate(dados):

    print(f"[{index + 1}] Preenchendo formulário")

    fill_form(driver, row)

    submit = driver.find_element(
        By.XPATH,
        "//input[@type='submit']"
    )

    submit.click()

    time.sleep(0.8)


print("Challenge concluído!")

driver.save_screenshot("screenshots/final.png")

input("ENTER para fechar")

driver.quit()