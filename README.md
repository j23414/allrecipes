# allrecipes

Pull recipe ingredients by country. Python code modified from [here](https://nycdatascience.com/blog/student-works/recipes-scraping-top-20-recipes-allrecipes/). I've removed the MongoDB dependency and substantially refactored the code for my purposes.

**dependencies**

* python3
* python3 modules: selenium, numpy
* [Firefox](https://www.mozilla.org/en-US/firefox/new/)
* [geckodriver](https://github.com/mozilla/geckodriver/releases) - place executable in path 

See [wiki](https://github.com/j23414/allrecipes/wiki/Installation) for more detailed install instructions.

## let's get scraping
Choose the country of interest by uncommenting their corresponding two lines in **scrap.py**. I've chosen Mexico from the list below:

```
...
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
...
```

Then run **scrap.py** to fetch recipes from the AllRecipes country's page and get their list of ingredients. Two Mexican recipes shown below.

```
$ ./scrap.py
website	https://allrecipes.com/recipe/14231	Mexico
recipe	14231	Guacamole	Mexico
ingred	Guacamole	14231	b'3 avocados - peeled, pitted, and mashed'	Mexico
ingred	Guacamole	14231	b'1 lime, juiced'	Mexico
ingred	Guacamole	14231	b'1 teaspoon salt'	Mexico
ingred	Guacamole	14231	b'1/2 cup diced onion'	Mexico
ingred	Guacamole	14231	b'3 tablespoons chopped fresh cilantro'	Mexico
ingred	Guacamole	14231	b'2 roma (plum) tomatoes, diced'	Mexico
ingred	Guacamole	14231	b'1 teaspoon minced garlic'	Mexico
ingred	Guacamole	14231	b'1 pinch ground cayenne pepper (optional)'	Mexico
website	https://allrecipes.com/recipe/16700	Mexico
recipe	16700	Salsa Chicken	Mexico
ingred	Salsa Chicken	16700	b'4 skinless, boneless chicken breast halves'	Mexico
ingred	Salsa Chicken	16700	b'4 teaspoons taco seasoning mix'	Mexico
ingred	Salsa Chicken	16700	b'1 cup salsa'	Mexico
ingred	Salsa Chicken	16700	b'1 cup shredded Cheddar cheese'	Mexico
ingred	Salsa Chicken	16700	b'2 tablespoons sour cream (optional)'	Mexico
website	https://allrecipes.com/recipe/16881	Mexico
...
==== Saved to Mexico.txt
```

The ingredients list will be saved to a textfile (e.g. Mexico.txt). 

```
$ head Mexico.txt
ingred	Addictive Sweet Potato Burritos	13954	b'1 tablespoon vegetable oil'	Mexico
ingred	Addictive Sweet Potato Burritos	13954	b'1 onion, chopped'	Mexico
ingred	Addictive Sweet Potato Burritos	13954	b'4 cloves garlic, minced'	Mexico
ingred	Addictive Sweet Potato Burritos	13954	b'6 cups canned kidney beans, drained'	Mexico
ingred	Addictive Sweet Potato Burritos	13954	b'2 cups water'	Mexico
ingred	Addictive Sweet Potato Burritos	13954	b'3 tablespoons chili powder'	Mexico
ingred	Addictive Sweet Potato Burritos	13954	b'4 teaspoons prepared mustard'	Mexico
ingred	Addictive Sweet Potato Burritos	13954	b'2 teaspoons ground cumin'	Mexico
ingred	Addictive Sweet Potato Burritos	13954	b'1 pinch cayenne pepper, or to taste'	Mexico
ingred	Addictive Sweet Potato Burritos	13954	b'3 tablespoons soy sauce'	Mexico
```

### Remove the `b'` and `'` surrounding ingredient names

```
$ cat Mexico.txt | sed "s/b'//g" | sed "s/'//g" > temp.txt
$ mv temp.txt Mexico.txt
```

## room for improvement

* Loopify to fetch multiple countries
* Track down why `b'` is added to the ingredient names and remove
* Autoclose the AllRecipes "do you want to provide feedback" popup window. Right now the user can close it manually. If the popup is not closed, then ingredients for the current recipe is not scrapped and result in empty strings.