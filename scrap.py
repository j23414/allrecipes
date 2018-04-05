#! /usr/bin/env python3
# Auth: Jennifer Chang
# Date: 2018/04/05
# -*- coding: utf-8 -*-

from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import numpy as np

# ============================= Functions
    
def scrape_recipe(br, year, idnumber,f):
    try:
        rtitle = br.find_element_by_tag_name('h1').text
    except:
        rtitle = 'NA'

    print('recipe\t'+idnumber+'\t'+rtitle+'\t'+year)
    f.write('recipe\t'+idnumber+'\t'+rtitle+'\t'+year+'\n')
    
    ingred = br.find_elements_by_class_name("checkList__item")
    ingredients = []
    for x in np.arange(len(ingred)-1):
        #if (str(ingred[x].text) == '')
        ingredients.append(str(ingred[x].text.encode('ascii', 'ignore')))
    
    for ingr in ingredients:
        print('ingred\t'+idnumber+'\t'+ingr+'\t'+year)
        f.write('ingred\t'+idnumber+'\t'+ingr+'\t'+year+'\n')
    
# ============================= Main
# Open browser
br=webdriver.Firefox() #opens Firefox browser 
br.get('https://www.allrecipes.com/recipes/728/world-cuisine/latin-american/mexican')
year="Mexico"

# Scrape URLS for recipes
urls = br.find_elements(By.CLASS_NAME, "favorite")   
id = []
for i, e in enumerate(urls):
    id.append(e.get_attribute('data-id'))    
    urls[i] = 'https://allrecipes.com/recipe/' + str(id[i])
urls = np.unique(urls)
id = np.unique(id)

f = open(year+'.txt', 'w')

# Fetch ingredients
for i, url in enumerate(urls):
    br.get(url)
    print('website\t'+url+'\t'+year)
    f.write('website\t'+url+'\t'+year+'\n')
    time.sleep(3)
    scrape_recipe(br, year, id[i],f)

f.close

print("==== Saved to "+year+".txt")