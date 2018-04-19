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
        #f.write('website\t'+url+'\t'+year+'\n') # MZ: Avoid writing to file for easier processing; JC: agree
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
    
    ingred = br.find_elements_by_class_name("checkList__item")
    ingredients = []
    for x in np.arange(len(ingred)-1):
        #if (str(ingred[x].text) == '')
        ingredients.append(str(ingred[x].text.encode('ascii', 'ignore')).replace("b'","").replace("'",""))
    
    for ingr in ingredients:
        print('ingred\t'+rtitle+'\t'+idnumber+'\t'+ingr+'\t'+year)
        f.write('ingred\t'+rtitle+'\t'+idnumber+'\t'+ingr+'\t'+year+'\n')
    
# ============================= Main
# Open browser
br=webdriver.Firefox() #opens Firefox browser 

# Choose country (or countries) by uncommenting their line (or lines)
year=[]
year.append(['Mexico','https://www.allrecipes.com/recipes/728/world-cuisine/latin-american/mexican'])
year.append(['Africa','https://www.allrecipes.com/recipes/226/world-cuisine/african'])
#year.append(['England','https://www.allrecipes.com/recipes/705/world-cuisine/european/uk-and-ireland/english'])
#year.append(['China"','https://www.allrecipes.com/recipes/695/world-cuisine/asian/chinese'])
#year.append(['Philippines','https://www.allrecipes.com/recipes/696/world-cuisine/asian/filipino'])
#year.append(['France','https://www.allrecipes.com/recipes/721/world-cuisine/european/french'])
#year.append(['Germany','https://www.allrecipes.com/recipes/722/world-cuisine/european/german'])
#year.append(['India','https://www.allrecipes.com/recipes/233/world-cuisine/asian/indian'])
#year.append(['Italy','https://www.allrecipes.com/recipes/723/world-cuisine/european/italian'])
#year.append(['Japan','https://www.allrecipes.com/recipes/699/world-cuisine/asian/japanese/'])
#year.append(['Korea','https://www.allrecipes.com/recipes/700/world-cuisine/asian/korean'])
#year.append(['Pakistani','https://www.allrecipes.com/recipes/15974/world-cuisine/asian/pakistani'])
#year.append(['Russia','https://www.allrecipes.com/recipes/716/world-cuisine/european/eastern-european/russian'])

# Fetch recipes
for country in year:
    print('==== Fetching recipes from ',country[0])
    br.get(country[1])
    probe_world_cuisine(country[0],br)
