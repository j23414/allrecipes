# allrecipes

Pull recipe ingredients by country. Python code modified from [here](https://nycdatascience.com/blog/student-works/recipes-scraping-top-20-recipes-allrecipes/). I've removed the MongoDB dependency and substationally refactored the code for my purposes.

## let's get scraping
Choose the country of interest by uncommenting their corresponding two lines in **scrap.py**. I've chosen Mexico from the list below:

```
...
# Choose a country, or add to the list
year="Mexico"
br.get('https://www.allrecipes.com/recipes/728/world-cuisine/latin-american/mexican')
#year="Africa"
#br.get('https://www.allrecipes.com/recipes/226/world-cuisine/african')
#year="England"
#br.get('https://www.allrecipes.com/recipes/705/world-cuisine/european/uk-and-ireland/english')
#year="China"
#br.get('https://www.allrecipes.com/recipes/695/world-cuisine/asian/chinese')
#year="Philippines"
#br.get('https://www.allrecipes.com/recipes/696/world-cuisine/asian/filipino')
...
```

Then run **scrap.py** to fetch recipes from the AllRecipes country's page and get their list of ingredients. Two Mexican recipes shown below.

```
$ ./scrap.py
website	https://allrecipes.com/recipe/14231	Mexico
recipe	14231	Guacamole	Mexico
ingred	14231	b'3 avocados - peeled, pitted, and mashed'	Mexico
ingred	14231	b'1 lime, juiced'	Mexico
ingred	14231	b'1 teaspoon salt'	Mexico
ingred	14231	b'1/2 cup diced onion'	Mexico
ingred	14231	b'3 tablespoons chopped fresh cilantro'	Mexico
ingred	14231	b'2 roma (plum) tomatoes, diced'	Mexico
ingred	14231	b'1 teaspoon minced garlic'	Mexico
ingred	14231	b'1 pinch ground cayenne pepper (optional)'	Mexico
website	https://allrecipes.com/recipe/16700	Mexico
recipe	16700	Salsa Chicken	Mexico
ingred	16700	b'4 skinless, boneless chicken breast halves'	Mexico
ingred	16700	b'4 teaspoons taco seasoning mix'	Mexico
ingred	16700	b'1 cup salsa'	Mexico
ingred	16700	b'1 cup shredded Cheddar cheese'	Mexico
ingred	16700	b'2 tablespoons sour cream (optional)'	Mexico
...
```

The website, recipe, and ingredients list will be saved to a textfile (e.g. Mexico.txt). 

```
$ head Mexico.txt
website	https://allrecipes.com/recipe/13954	Mexico
recipe	13954	Addictive Sweet Potato Burritos	Mexico
ingred	13954	b'1 tablespoon vegetable oil'	Mexico
ingred	13954	b'1 onion, chopped'	Mexico
ingred	13954	b'4 cloves garlic, minced'	Mexico
ingred	13954	b'6 cups canned kidney beans, drained'	Mexico
ingred	13954	b'2 cups water'	Mexico
ingred	13954	b'3 tablespoons chili powder'	Mexico
ingred	13954	b'4 teaspoons prepared mustard'	Mexico
ingred	13954	b'2 teaspoons ground cumin'	Mexico
```

### split into ingredients and recipe list

For legacy users...

```
$ grep "ingred" Mexico.txt | awk -F'\t' 'OFS="\t" {print $2,$3,$4} > ingredientsMX.txt
$ grep "recipe" Mexico.txt | awk -F'\t' 'OFS="\t" {print $2,$3,$4} > recipesMX.txt

```

## room for improvement

* Loopify to fetch multiple countries
* Track down why `b'` is added to the ingredient descriptions and remove
