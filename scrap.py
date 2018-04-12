#! /usr/bin/env python3
# Auth: Jennifer Chang
# Auth: Michael Zeller
# Date: 2018/04/05
# -*- coding: utf-8 -*-

from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import numpy as np

# ============================= Functions
def probe_world_cuisine(year,br):
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
        #f.write('website\t'+url+'\t'+year+'\n') #Avoid writing to file for easier processing
        time.sleep(3)
        scrape_recipe(br, year, id[i],f)
    
    f.close
    
    print("==== Saved to "+year+".txt")
    
def scrape_recipe(br, year, idnumber,f):
    try:
        rtitle = br.find_element_by_tag_name('h1').text
    except:
        rtitle = 'NA'

    print('recipe\t'+idnumber+'\t'+rtitle+'\t'+year)
    #f.write('recipe\t'+idnumber+'\t'+rtitle+'\t'+year+'\n')
    
    ingred = br.find_elements_by_class_name("checkList__item")
    ingredients = []
    for x in np.arange(len(ingred)-1):
        #if (str(ingred[x].text) == '')
        ingredients.append(str(ingred[x].text.encode('ascii', 'ignore')))
    
    for ingr in ingredients:
        print('ingred\t'+rtitle+'\t'+idnumber+'\t'+ingr+'\t'+year)
        f.write('ingred\t'+rtitle+'\t'+idnumber+'\t'+ingr+'\t'+year+'\n')
    
# ============================= Main
# Open browser
br=webdriver.Firefox() #opens Firefox browser 

# Choose a country, or add to the list
year="Mexico"
br.get('https://www.allrecipes.com/recipes/728/world-cuisine/latin-american/mexican')
probe_world_cuisine(year,br)
#year="Africa"
#br.get('https://www.allrecipes.com/recipes/226/world-cuisine/african')
#probe_world_cuisine(year,br)
#year="England"
#br.get('https://www.allrecipes.com/recipes/705/world-cuisine/european/uk-and-ireland/english')
#probe_world_cuisine(year,br)
#year="China"
#br.get('https://www.allrecipes.com/recipes/695/world-cuisine/asian/chinese')
#probe_world_cuisine(year,br)
#year="Philippines"
#br.get('https://www.allrecipes.com/recipes/696/world-cuisine/asian/filipino')
#probe_world_cuisine(year,br)
#year="France"
#br.get('https://www.allrecipes.com/recipes/721/world-cuisine/european/french')
#probe_world_cuisine(year,br)
#year="Germany"
#br.get('https://www.allrecipes.com/recipes/722/world-cuisine/european/german')
#probe_world_cuisine(year,br)
#year="India"
#br.get('https://www.allrecipes.com/recipes/233/world-cuisine/asian/indian')
#probe_world_cuisine(year,br)
#year="Italy"
#br.get('https://www.allrecipes.com/recipes/723/world-cuisine/european/italian')
#probe_world_cuisine(year,br)
#year="Japan"
#br.get('https://www.allrecipes.com/recipes/699/world-cuisine/asian/japanese/')
#probe_world_cuisine(year,br)
#year="Korea"
#br.get('https://www.allrecipes.com/recipes/700/world-cuisine/asian/korean')
#probe_world_cuisine(year,br)
#year="Pakistani"
#br.get('https://www.allrecipes.com/recipes/15974/world-cuisine/asian/pakistani')
#probe_world_cuisine(year,br)
#year="Russia"
#br.get('https://www.allrecipes.com/recipes/716/world-cuisine/european/eastern-european/russian')
#probe_world_cuisine(year,br)
