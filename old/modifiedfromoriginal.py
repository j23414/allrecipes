#! /usr/bin/env python3
# Auth: 
# Date: 2018/04/05

from selenium import webdriver
#from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
#import scrapy
#from sys import argv
import time
#import csv
#import lxml.html
#import unicodedata
#import time
import numpy as np
import re
import pymongo

        
# Mexico
def allyears(br):
    browser.get('https://www.allrecipes.com/recipes/728/world-cuisine/latin-american/mexican')
    top20list(browser,"Mexican")

#http://selenium-python.readthedocs.io/locating-elements.html #function to retrieve viewingactivity list items
def top20list(br, year):
    urls = br.find_elements(By.CLASS_NAME, "favorite")   
    id = []
    for i, e in enumerate(urls):
        id.append(e.get_attribute('data-id'))    
        urls[i] = 'https://allrecipes.com/recipe/' + str(id[i])
        # counter +=
    urls = np.unique(urls)
    id = np.unique(id)

    for i, url in enumerate(urls):
        br.get(url)
        time.sleep(3)
        scrape_recipe(br, year, id[i])


def scrape_recipe(br, year, idnumber):
    # fill in code for recipe page
    try:
        rtitle = br.find_element_by_tag_name('h1').text
    except:
        rtitle = 'NA'

    print(idnumber)
    print(rtitle)
    
    try:
        br.find_element_by_xpath('//div[contains(@class,"ui-dialog") and @aria-describedby="dialogContent2"]//button[@title="Close"]').click()
    except:
        print('no popup')
    '''
    try:
        starrating = br.find_element_by_class_name('rating-stars').get_attribute('data-ratingstars')
        
    except:
        starrating = 'NA'
        

    try:
        madeitcount = br.find_element_by_class_name('made-it-count').text
        
    except:
        madeitcount = 'NA'

    try:
        reviewcount = br.find_element_by_class_name('review-count').text
        reviewcount = str(re.findall('(\w+) reviews', reviewcount)[0])
        
    except:
        reviewcount = 'NA'
        

    try:
        calcount = br.find_element_by_class_name('calorie-count').text
        calcount = str(re.findall('(\w+) cals', calcount)[0])
        
    except:
        calcount = 'NA'
        
    
    try:
        prepTime = br.find_element_by_xpath('//time[@itemprop = "prepTime"]').get_attribute('datetime')
        prepTime = str(re.findall('PT(\w+)', prepTime)[0])
        
    except: 
        prepTime = 'NA'
        


    try:
        cookTime = br.find_element_by_xpath('//time[@itemprop = "cookTime"]').get_attribute('datetime')
        cookTime = str(re.findall('PT(\w+)', cookTime)[0])
        
    except:
        cookTime = 'NA'
        


    try:
        totalTime = br.find_element_by_xpath('//time[@itemprop = "totalTime"]').get_attribute('datetime')
        totalTime = str(re.findall('PT(\w+)', totalTime)[0])
        
    except:
        totalTime = 'NA'
    '''
        
    # "prep time: " + 
    # print "cook time: " + br.find_elements_by_class_name("prepTime__item")[2].get_attribute('datetime')
    # print "total time: " + br.find_elements_by_class_name("prepTime__item")[3].get_attribute('datetime')


    ingred = br.find_elements_by_class_name("checkList__item")

    ingredients = []
    for x in np.arange(len(ingred)-1):
        #if (str(ingred[x].text) == '')

        ingredients.append(str(ingred[x].text.encode('ascii', 'ignore')))
    
    print('testoutput: ')
#    recoutput = '\t'+year+'\t'+idnumber+'\t'+rtitle+'\t'+starrating+'\t'+madeitcount+'\t'+reviewcount+'\t'+calcount+'\t'+prepTime+'\t'+\
#    cookTime+'\t'+totalTime
    recoutput = '\t'+year+'\t'+idnumber+'\t'+rtitle
    
    print(recoutput)

    temp = {'idnumber': idnumber, 'year': year, 'recipe_title': rtitle.encode('ascii', 'ignore')}
    print(temp)
    
    listingr = []
    for ingr in ingredients:
        temp = {'idnumber': idnumber, 'year': year, 'ingredient': ingr.encode('ascii', 'ignore')}
        #collection2.insert(temp)#listingr.append(year+'\t'+idnumber+'\t'+ingr)
        print(idnumber+'\t'+ingr+'\t'+year)
        

    ingroutput = '\t'.join(listingr)
    ingroutput = '\t'+ingroutput
    print(ingroutput)
    #cloeses automatically, append data to csv then open as panda data frame 
    '''
    temp = {'idnumber': idnumber, 'year': year, 'recipe_title': rtitle.encode('ascii', 'ignore'), 'star_rating': starrating, 'made_it_count': \
        madeitcount, 'review_count': reviewcount, 'cal_count': calcount, 'prep_time': prepTime, 'cook_time': cookTime, \
        'total_time': totalTime}
    '''

    #collection.insert(temp)

    

#opens browser and initalizes MongoDB
if __name__ == '__main__':
    '''
    try:
        conn=pymongo.MongoClient()
        print("Connected successfully!!!")
    except pymongo.errors.ConnectionFailure as e:
#    except pymongo.errors.ConnectionFailure, e:
        print("Could not connect to MongoDB: %s" % e )
    conn

    recipesdb = conn['allrecipesMX']
    collection = recipesdb['recipesMX']
    collection2 = recipesdb['ingredientsMX']
    '''
    browser = webdriver.Firefox() #opens Firefox browser 
    allyears(browser) 

    