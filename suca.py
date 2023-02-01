from pyfood.utils import Shelf
from datetime import datetime
import random

today = datetime.today()
month = today.month

#https://www.hsph.harvard.edu/nutritionsource/healthy-eating-plate/
#https://menu-vegetarien.com/comment-manger-vegetarien/

#Building a Healthy and Balanced Diet
#vegetables and fruits – ½ of your plate.
#whole grains – ¼ of your plate.
#Protein power – ¼ of your plate
#Healthy plant oils – in moderation.


shelf = Shelf(region='France', month_id=month-1)
fruits_in_season = shelf.get_seasonal_food(key='001')
#fruits_in_season = shelf.process_ingredients(fruits_in_season, lang_dest='EN')
#fruits_in_season = fruits_in_season['ingredients_by_taxon']
vegetables_in_season = shelf.get_seasonal_food(key='002')
whole_grains = ['Boulgour', 'Riz', 'Maïs', 'Avoine', 'Farro', 'Teff', 'Sorghum', 'Quinoa', 'Sarrasin', 'Millet', 'Kamut']
healthy_protein = ['Haricots', 'Noix', 'Fromage']

selected_fruit = random.choice(fruits_in_season)
selected_vegetable = random.choice(vegetables_in_season)
selected_wgrains = random.choice(whole_grains)
selected_hproteins =  random.choice(healthy_protein)

print('fruits : ' + selected_fruit + '\nlegumes : ' + selected_vegetable + '\ncéréales complètes : ' + selected_wgrains + '\nprotéines : ' + selected_hproteins)
