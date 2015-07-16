from selenium import webdriver
from selenium.webdriver.common.keys import Keys

# You can use Chrome and many other here
driver = webdriver.Firefox()
# Go to the specified url
driver.get("http://www.pumpingstationone.org")
# Check if we have the right title
assert "Pumping Station: One" in driver.title
# We know that post are made like
# <div class="post"><h2><a href="#">Title of the post</a></h2></div>
# So we can use a css selector
titles = driver.find_elements_by_css_selector(".post h2 a")
# Iterate over the titles found
for title in titles:
    # Get the text of the title link
    print(title.text)
# Don't forget to close the driver to close the browser
driver.close()
