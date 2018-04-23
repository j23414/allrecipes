[![Build Status](https://travis-ci.org/j23414/allrecipes.svg?branch=master)](https://travis-ci.org/j23414/allrecipes)

# allrecipes

Pull recipe ingredients by country. Python code modified from [here](https://nycdatascience.com/blog/student-works/recipes-scraping-top-20-recipes-allrecipes/). I've removed the MongoDB dependency and substantially refactored the code for my purposes. The recipe ingredients were used to create recipe-phylogenetic trees for a [EEOB 563 Molecular Phylogeny](https://isu-molphyl.github.io/EEOB563-Spring2018/) project. The project repo can be found at [https://github.com/mazeller/EEOB563-Final-Project](https://github.com/mazeller/EEOB563-Final-Project).

**dependencies**

* python3
* python3 modules: selenium, numpy
* [Firefox](https://www.mozilla.org/en-US/firefox/new/)
* [geckodriver](https://github.com/mozilla/geckodriver/releases) - place executable in path 

See [wiki](https://github.com/j23414/allrecipes/wiki/Installation) for more detailed install instructions.

## let's get scraping
Choose the country of interest by uncommenting their corresponding 3 lines in **scrape.py**. I've chosen Mexico and Africa from the list below:

```
...
# Choose country (or countries) by uncommenting their line (or lines)
year=[]
year.append(['Mexico','https://www.allrecipes.com/recipes/728/world-cuisine/latin-american/mexican'])
year.append(['Africa','https://www.allrecipes.com/recipes/226/world-cuisine/african'])
#year.append(['England','https://www.allrecipes.com/recipes/705/world-cuisine/european/uk-and-ireland/english'])
#year.append(['China"','https://www.allrecipes.com/recipes/695/world-cuisine/asian/chinese'])
#year.append(['Philippines','https://www.allrecipes.com/recipes/696/world-cuisine/asian/filipino'])
...
```

Then run **scrape.py** to fetch recipes from the AllRecipes country's page and get their list of ingredients. Two Mexican recipes shown below.

```
$ ./scrape.py
website	https://allrecipes.com/recipe/14231	Mexico
recipe	14231	Guacamole	Mexico
ingred	Guacamole	14231	3 avocados - peeled, pitted, and mashed	Mexico
ingred	Guacamole	14231	1 lime, juiced	Mexico
ingred	Guacamole	14231	1 teaspoon salt	Mexico
ingred	Guacamole	14231	1/2 cup diced onion	Mexico
ingred	Guacamole	14231	3 tablespoons chopped fresh cilantro	Mexico
ingred	Guacamole	14231	2 roma (plum) tomatoes, diced	Mexico
ingred	Guacamole	14231	1 teaspoon minced garlic	Mexico
ingred	Guacamole	14231	1 pinch ground cayenne pepper (optional)	Mexico
website	https://allrecipes.com/recipe/16700	Mexico
recipe	16700	Salsa Chicken	Mexico
ingred	Salsa Chicken	16700	4 skinless, boneless chicken breast halves	Mexico
ingred	Salsa Chicken	16700	4 teaspoons taco seasoning mix	Mexico
ingred	Salsa Chicken	16700	1 cup salsa	Mexico
ingred	Salsa Chicken	16700	1 cup shredded Cheddar cheese	Mexico
ingred	Salsa Chicken	16700	2 tablespoons sour cream (optional)	Mexico
website	https://allrecipes.com/recipe/16881	Mexico
...
==== Saved to Mexico.txt
...
```

The ingredients list will be saved to a textfile (e.g. Mexico.txt, Africa.txt). 

```
$ head Mexico.txt
ingred	Addictive Sweet Potato Burritos	13954	1 tablespoon vegetable oil	Mexico
ingred	Addictive Sweet Potato Burritos	13954	1 onion, chopped	Mexico
ingred	Addictive Sweet Potato Burritos	13954	4 cloves garlic, minced		Mexico
ingred	Addictive Sweet Potato Burritos	13954	6 cups canned kidney beans, drained	Mexico
ingred	Addictive Sweet Potato Burritos	13954	2 cups water	Mexico
ingred	Addictive Sweet Potato Burritos	13954	3 tablespoons chili powder	Mexico
ingred	Addictive Sweet Potato Burritos	13954	4 teaspoons prepared mustard	Mexico
ingred	Addictive Sweet Potato Burritos	13954	2 teaspoons ground cumin	Mexico
ingred	Addictive Sweet Potato Burritos	13954	1 pinch cayenne pepper, or to taste	Mexico
ingred	Addictive Sweet Potato Burritos	13954	3 tablespoons soy sauce	Mexico
```

## room for improvement

* Autoclose the AllRecipes "do you want to provide feedback" popup window. Right now the user can close it manually. If the popup is not closed, then ingredients for the current recipe is not scraped and result in empty strings. Does not affect later scraped recipes.
* May be able to remove the Firefox and geckodriver dependency. Would require text processing the html file (instead of popping a window)
