import appCore

word_capture=["feliz cumple", "feliz cumpleaños", "felicidades"]

greet_string="Saludo_automatico"

appCore.driver = Driver()
appCore.panel=Panel(driver.driver, driver.getUser(), word_capture, greet_string)
appCore.panel.greetChats()
appCore.driver.closeDriver()