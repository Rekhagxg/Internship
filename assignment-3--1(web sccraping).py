#!/usr/bin/env python
# coding: utf-8

# # 1. Write a python program which searches all the product under a particular product from www.amazon.in. The product to be searched will be taken as input from user. For e.g. If user input is ‘guitar’. Then search for guitars.
# 2. In the above question, now scrape the following details of each product listed in first 3 pages of your search results and save it in a data frame and csv. In case if any product has less than 3 pages in search results then scrape all the products available under that product name. Details to be scraped are: "Brand
# Name", "Name of the Product", "Price", "Return/Exchange", "Expected Delivery", "Availability" and “Product URL”. In case, if any of the details are missing for any of the product then replace it by “-“.
# 

# In[46]:


get_ipython().system('pip install selenium')


# In[2]:


import time
import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


# In[44]:


#connect to driver
driver=webdriver.Chrome(r"/Users/rekhagrg/Downloads/chromedriver")


# In[45]:


driver.get('https://www.amazon.in')


# In[46]:


#find the search input element(guitar)
search=driver.find_element(By.ID,"twotabsearchtextbox")
search.send_keys('guitars')


# In[47]:


#search button 
search=driver.find_element(By.ID,"nav-search-submit-button")
search.click()


# In[48]:



brand=[]
product_name=[]
price=[]
Returnorexchange=[]
Expected_Delivery=[]
Availability=[]
product_URL=[]


# In[49]:


start=0
end=3

for page in range(start,end):
    url=driver.find_elements(By.XPATH,'//a[@class="a-link-normal s-underline-text s-underline-link-text s-link-style a-text-normal"]')
    for i in url:
        product_URL.append(i.get_attribute('href'))
    next_button=driver.find_elements(By.XPATH,"/html/body/div[1]/div[2]/div[1]/div[1]/div/span[1]/div[1]/div[67]/div/div/span/a[3]")
    


# In[51]:


product_URL


# In[52]:


# Loop through each product URL
for url in product_URL:
    driver.get(url)
    time.sleep(0.1)

    # Scrape brand name
    try:
        brand_name = driver.find_element(By.ID, "bylineInfo")
        brand.append(brand_name.text)
    except NoSuchElementException:
        brand.append("-")

    # Scrape product name
    try:
        product = driver.find_element(By.ID, "productTitle")
        product_name.append(product.text)
    except NoSuchElementException:
        product_name.append("-")

    # Scrape price
    try:
        pri = driver.find_element(By.CLASS_NAME, "a-price-whole")
        price.append(pri.text)
    except NoSuchElementException:
        price.append("-")

    # Scrape return or exchange
    try:
        retur = driver.find_element(By.ID, "RETURNS_POLICY")
        Returnorexchange.append(retur.text)
    except NoSuchElementException:
        Returnorexchange.append("-")

    # Scrape expected delivery
    try:
        deliv = driver.find_element(By.XPATH, '/html/body/div[2]/div[2]/div[5]/div[3]/div[1]/div[3]/div/div[1]/div/div/div/form/div/div/div/div/div[3]/div/div[2]/div[9]/div[1]/div/div/div[1]/span/span')
        Expected_Delivery.append(deliv.text)
    except NoSuchElementException:
        Expected_Delivery.append("-")

    # Scrape availability
    try:
        avaib = driver.find_element(By.ID, "availability")
        Availability.append(avaib.text)
    except NoSuchElementException:
        Availability.append('-')


# In[55]:


print(len(brand),len(product_name),len(price))


# In[53]:


# Create a DataFrame with the scraped data
data = {'Brand Name': brand,
    'Product Name': product_name,
    'Price': price,
    'Return/Exchange': Returnorexchange,
    'Expected Delivery': Expected_Delivery,
    'Availability': Availability,
    'Product URL': product_URL}
df = pd.DataFrame(data)
df


# In[ ]:





# In[54]:


# Save the DataFrame to a CSV file
df.to_csv('data.csv',index=False)


# In[ ]:





# # Write a python program to access the search bar and search button on images.google.com and scrape 10 images each for keywords ‘fruits’, ‘cars’ and ‘Machine Learning’, ‘Guitar’, ‘Cakes’

# In[ ]:


#Fruits and cars


# In[56]:


import time
import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


# In[57]:


driver = webdriver.Chrome(r"/Users/rekhagrg/Downloads/chromedriver")
driver.get("https://images.google.com/?gws_rd=ssl")


# In[58]:


try:
    accept_all=driver.find_element(By.ID,'L2AGLb')
    accept_all.click()
except:
    pass


# In[59]:


search_box=driver.find_element(By.XPATH,'/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div/div[2]/textarea')
search_box.send_keys('fruits')


# In[60]:


search_click=driver.find_element(By.XPATH,'/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/button')
search_click.click()


# In[61]:


fruit_images=[]


# In[68]:


# get 10 images
fruit_images = []
images = driver.find_elements(By.XPATH, '//img[@class="rg_i Q4LuWd"]')
for image in images[:10]:
    fruit_images.append(image.get_attribute('src'))

# cars 10 images
search_box = driver.find_element(By.XPATH, '//input[@name="q"]')
search_box.send_keys('cars')

search_click = driver.find_element(By.XPATH, '//button[@aria-label="Google Search"]')
search_click.click()

car_images = driver.find_elements(By.XPATH, '//img[@class="rg_i Q4LuWd"]')
cars = []
for car in car_images[:10]:
    cars.append(car.get_attribute('src'))


# In[69]:


len (cars)


# In[63]:


len(fruit_images)


# In[64]:


# Create a DataFrame with the scraped data
df = pd.DataFrame(fruit_images)
df


# In[70]:


# Create a DataFrame with the scraped data
df = pd.DataFrame(cars)
df


# In[65]:


# Save the DataFrame to a CSV file
df.to_csv('fruit_images.csv', index=False)


# In[71]:


# Save the DataFrame to a CSV file
df.to_csv('cars.csv', index=False)


# # Write a python program to search for a smartphone(e.g.: Oneplus Nord, pixel 4A, etc.) on www.flipkart.com and scrape following details for all the search results displayed on 1st page. Details to be scraped: “Brand Name”, “Smartphone name”, “Colour”, “RAM”, “Storage(ROM)”, “Primary Camera”,
# “Secondary Camera”, “Display Size”, “Battery Capacity”, “Price”, “Product URL”. Incase if any of the details is missing then replace it by “- “. Save your results in a dataframe and CSV.

# In[25]:


import time
import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


# In[26]:


#connect to driver
driver=webdriver.Chrome(r"/Users/rekhagrg/Downloads/chromedriver")


# In[27]:


driver.get("https://www.flipkart.com/")


# In[28]:


# Close the login popup if it appears
try:
    close_button = driver.find_element(By.XPATH, "//button[@class='_2KpZ6l _2doB4z']")
    close_button.click()
except NoSuchElementException:
    pass


# In[29]:


search_bar=driver.find_element(By.XPATH,'/html/body/div[1]/div/div[1]/div[1]/div[2]/div[2]/form/div/div/input')
search_bar.send_keys('Oneplus')


# In[30]:


search_click=driver.find_element(By.XPATH,'/html/body/div[1]/div/div[1]/div[1]/div[2]/div[2]/form/div/button')
search_click.click()


# In[109]:


# Initialize empty lists to store the scraped data
phone_url=[]
brand_name=[]
smartphone_name=[]
colour=[]
ram_rom=[]
primary_camera=[]


# In[110]:


# url=driver.find_elements(By.XPATH,'//a[@class="s1Q9rs"]')
# for link in url:
#     phone_url.append(link.get_attribute('href'))


# In[111]:


# phone_url


# In[112]:


# for phone in phone_url:
#     time.sleep(0.1)
#     brand_name.append('Oneplus')
try:
    phone_name = driver.find_elements(By.XPATH, '//a[@class="s1Q9rs"]')
    for name in phone_name:
        smartphone_name.append(name.text)
        brand_name.append('Oneplus')
except:
    smartphone_name.append('-')
        


# In[339]:


#scrape RAM 
try:
    RAM=driver.find_elements(By.XPATH,'//div[@class="_3Djpdu"]')
    for RM in RAM:
        ram_rom.append(RM.text)
except:
    ram_rom.append('-')


# In[114]:


print(ram_rom)


# In[115]:


print(smartphone_name)


# In[116]:


print(len(ram_rom),len(brand_name),len(smartphone_name))


# In[117]:


data={'Brand':brand_name,'Phone Name':smartphone_name,'RAM':ram_rom}


# In[118]:


df=pd.DataFrame(data)
df


# In[ ]:





# # Write a program to scrap geospatial coordinates (latitude, longitude) of a city searched on google maps

# In[477]:


import time
import re
import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


# In[478]:


#connect to driver
driver=webdriver.Chrome(r"/Users/rekhagrg/Downloads/chromedriver")


# In[479]:


# Open Google Maps
driver.get("https://www.google.com/maps")


# In[480]:


accept=driver.find_element(By.XPATH,'/html/body/c-wiz/div/div/div/div[2]/div[1]/div[3]/div[1]/div[1]/form[2]/div/div/button/span')
accept.click()


# In[481]:


# Search for the city
search_box = driver.find_element(By.XPATH,"/html/body/div[3]/div[9]/div[3]/div[1]/div[1]/div/div[2]/form/input[1]")
search_box.send_keys("Southampton, United Kingdom")
search_box.submit()


# In[482]:


search_click=driver.find_element(By.XPATH,"/html/body/div[3]/div[9]/div[3]/div[1]/div[1]/div/div[2]/div[1]/button")
search_click.click()


# In[484]:


try:
    # Get the URL of the current page
    url_string = driver.current_url
    print("URL Extracted:", url_string)

    # Extract latitude and longitude from the URL
    lat_lng = re.findall(r'@(.*)data', url_string)[0]
    lat, lng = lat_lng.split(',')[0], lat_lng.split(',')[1]
    print("Latitude:", lat)
    print("Longitude:", lng)

except NoSuchElementException:
    print("Error: Location details not found.")


# In[486]:


#close the brower
driver.quit()


# # Write a program to scrap all the available details of best gaming laptops from digit.in

# In[218]:


import time
import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


# In[219]:


#connect to driver
driver=webdriver.Chrome(r"/Users/rekhagrg/Downloads/chromedriver")


# In[220]:


driver.get('https://www.digit.in/top-products/best-gaming-laptops-40.html')


# In[228]:


# Initialize empty lists to store the scraped data(Best Gaming laptop under £50,000)
Brand_name=[]
windows=[]
memory=[]


# In[229]:


#scrape brand name
try:
    names = driver.find_elements(By.XPATH,'//div[@class="TopNumbeHeading"]' )
    for name in names:
        Brand_name.append(name.text)
except:
    Brand_name.append("-")


# In[230]:


Brand_name


# In[231]:


#scrape windows
try:
    wind = driver.find_elements(By.XPATH, '//div[@class="product-detail"]')
    for windo in wind:
        windows.append(windo.text)
except:
    windows.append("-")


# In[232]:


windows


# In[233]:


len(windows)


# In[234]:


data={'Brand Name':Brand_name,'Product Detail':windows}
data


# In[235]:


df=pd.DataFrame(data)
df


# # Write a python program to scrape the details for all billionaires from www.forbes.com. Details to be scrapped:
# “Rank”, “Name”, “Net worth”, “Age”, “Citizenship”, “Source”, “Industry”.
# 
# 
# Top 100 billioners

# In[403]:


import time
import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


# In[296]:


#connect to driver
driver=webdriver.Chrome(r"/Users/rekhagrg/Downloads/chromedriver")


# In[297]:


driver.get('https://www.forbes.com/billionaires/')


# In[298]:


try:
    rank_one=driver.find_element(By.XPATH,'/html/body/div[1]/div[2]/div[3]/div[2]/div[2]/div[2]/div[1]/div[1]/div[1]/div[2]/div[1]/div[1]')
    rank_one.click()
    
except:
    pass


# In[299]:


name=[]


# In[300]:


table_row=driver.find_elements(By.XPATH,'//div[@class="TableRow_cell__db-hv Table_cell__houv9"]')
for data in table_row:
    name.append(data.text)


# In[301]:


len(name)


# In[302]:


names = []
age=[]
net_worth=[]
source=[]
country=[]
industry=[]
# names extraction
for i in range(1, len(name), 7):
    name_list= name[i]
    names.append(name_list)
    
for j in range(2,len(name),7):
    net_income=name[j]
    net_worth.append(net_income)
    
for k in range(3,len(name),7):
    age_list=name[k]
    age.append(age_list)
    
for l in range(4,len(name),7):
    country_list=name[l]
    country.append(country_list)
    
for m in range(5,len(name),7):
    source_list=name[m]
    source.append(source_list)
    
for n in range(6,len(name),7):
    industry_list=name[n]
    industry.append(industry_list)


# In[303]:


billionair_df=pd.DataFrame({'NAME':names,'NET WORTH':net_worth,'AGE':age,'COUNTRY':country,'SOURCE':source,'INDUSTRY':industry})
billionair_df


# In[304]:


billionair_df.to_csv('Billionair list')


# # Write a program to extract at least 500 Comments, Comment upvote and time when comment was posted
# from any YouTube Video.

# In[306]:


import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


# In[307]:


driver = webdriver.Chrome(r"/Users/rekhagrg/Downloads/chromedriver")


# In[308]:


driver.get('https://www.youtube.com/watch?v=48h57PspBec')


# In[314]:


comment=[]


# In[315]:


from selenium.common.exceptions import TimeoutException

scroll_pause_time = 2 # Time to pause between each scroll (in seconds)
num_scrolls = 80  # Number of times to scroll (adjust as needed)

for _ in range(num_scrolls):
    comments=driver.find_elements(By.CSS_SELECTOR,'yt-formatted-string#content-text')
    for content in comments:
        comment.append(content.text)
    try:
        driver.execute_script("window.scrollTo(0, document.documentElement.scrollHeight);")
        WebDriverWait(driver, scroll_pause_time).until(EC.presence_of_element_located((By.TAG_NAME, "ytd-comment-thread-renderer")))
    except TimeoutException:
        print("Timed out waiting for comments to load.")
        break


# In[317]:


len(comment)


# In[318]:


comment


# # Write a python program to scrape a data for all available Hostels from https://www.hostelworld.com/ in
# “London” location. You have to scrape hostel name, distance from city centre, ratings, total reviews, overall reviews, privates from price, dorms from price, facilities and property description.

# In[430]:


driver = webdriver.Chrome(r"/Users/rekhagrg/Downloads/chromedriver")


# In[431]:


#Open the website
driver.get('https://www.hostelworld.com/')


# In[432]:


click_2=driver.find_element(By.XPATH,'/html/body/div[3]/div/div/div[2]/div[2]/div/div/div[4]/div/div[2]/div/div[1]/div/div/div/input')
click_2.click()


# In[433]:


click_2.send_keys('London')


# In[435]:


select=driver.find_element(By.XPATH,'/html/body/div[3]/div/div/div[2]/div[2]/div/div/div[4]/div/div[2]/div/div[1]/div/div/ul/li[2]/div')
select.click()


# In[436]:


lets_go=driver.find_element(By.XPATH,'/html/body/div[3]/div/div/div[2]/div[2]/div/div/div[4]/div/div[2]/div/div[6]/button')
lets_go.click()


# In[450]:


name=[]
distance=[]
ratings=[]


# In[451]:


try:
    Hostel_name=driver.find_elements(By.XPATH,'//h2[@class="title title-6"]')
    for NA in Hostel_name:
        name.append(NA.text)
except:
    name.append('-')


# In[452]:


len(name)


# In[453]:


name


# In[454]:


try:
    distan=driver.find_elements(By.XPATH,'//span[@class="description"]')
    for Di in distan:
        distance.append(Di.text)
except:
    distance.append('-')


# In[455]:


len(distance)


# In[456]:


distance


# In[457]:


try:
    rates=driver.find_elements(By.XPATH,'//div[@class="rating rating-summary-container big"]')
    for RT in rates:
        ratings.append(RT.text)
except:
    ratings.append('-')


# In[458]:


len(ratings)


# In[459]:


ratings


# In[460]:


dat={'Name':name,'Distance to city':distance,'Overall Ratings':ratings}
dat


# In[461]:


df=pd.DataFrame(dat)


# In[462]:


df


# In[ ]:




