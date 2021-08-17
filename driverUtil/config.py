from selenium import webdriver


class Browser(object):

    def __init__(self):
        self.driver = None

    def getbrowser(self):
        path = '../geckodriver'
        useragent = "Mozilla/5.0 (Linux; Android 8.0.0; Pixel 2 XL Build/OPD1.170816.004) AppleWebKit/537.36 (KHTML, " \
                    "like Gecko) Chrome/67.0.3396.87 Mobile Safari/537.36 "
        # Firefox
        profile = webdriver.FirefoxProfile()
        profile.set_preference("general.useragent.override", useragent)
        options = webdriver.FirefoxOptions()
        options.set_preference("dom.webnotifications.serviceworker.enabled", False)
        options.set_preference("dom.webnotifications.enabled", False)
        options.add_argument('--headless')
        self.driver = webdriver.Firefox(firefox_profile=profile, options=options, executable_path=path)
        return self.driver

