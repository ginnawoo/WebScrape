from selenium import webdriver
#from parsel import Selector

driver = webdriver.Chrome(r'C:\Program Files (x86)\Google\Chrome\Application\chromedriver')

driver.get('https://www.linkedin.com')

username = driver.find_element_by_class_name('input__input')
username.send_keys('enteryouremail@email.com')

password = driver.find_element_by_id('session_password')
password.send_keys('enteryourpassword')

log_in_button = driver.find_element_by_class_name('sign-in-form__submit-button')
log_in_button.click()



driver.get('https://www.google.com')

search_query = driver.find_element_by_name('q')
search_query.send_keys('site:linkedin.com/in/ AND "university of south florida" AND "software engineer"')


google_search_button = driver.find_element_by_name('btnK')
google_search_button.submit()


linkedin_urls = driver.find_elements_by_class_name('iUh30')
linkedin_urls = [url.text for url in linkedin_urls]
linkedin_urls



# for linkedin_url in linkedin_urls:
#     driver.get(linkedin_url)
#     sel = Selector(driver.page_source)
# driver.quit()

# name = sel.xpath('//*[starts-with(@class,"pv-top-card--list inline-flex align-items-center"")]/text()').extract_first()
# if name:
#     name = name.strip()


# company = sel.xpath('//*[starts-with(@class,"pv-top-card--list pv-top-card--list-bullet mt1")]/text()').extract_first()
# if company:
#     company = company.strip()

# linkedin_url = driver.current_url

# print('\n')
# print('Name: ' + name)
# print('Company: ' + company)
# print('URL: ' + linkedin_url)
# print('\n')