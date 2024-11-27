from selenium import webdriver
# from selenium.webdriver.firefox.options import Options
# from selenium.webdriver.firefox.firefox_profile import FirefoxProfile

firefox_options = webdriver.FirefoxOptions()
# options=Options()
# firefox_profile = FirefoxProfile()
# firefox_profile.set_preference("javascript.enabled", False)
# options.profile = firefox_profile

driver = webdriver.Firefox(options=firefox_options)

driver.get("https://www.amazon.com/dp/B075CYMYK6?psc=1&ref_=cm_sw_r_cp_ud_ct_FM9M699VKHTT47YD50Q6")

# ** De ngam cuu tiep sau :-) ....
