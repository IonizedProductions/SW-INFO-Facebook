import os ## import curent os
import facebook ## imports the facebook sdk
import random
import swapi ## imports the star wars api
from PIL import Image, ImageDraw ## imports pillow

token = "your token here :p"

def pes():
	rs = random.randint(1,82)
	return rs
	## Ranomizer component to get random number between 1 and 82


SW_id = swapi.get_person(pes()) ## calls swapi to get person using randomizer above

SW_more = SW_id.get_homeworld() ## gets chosen persons homeworld

SW_data = SW_id.get_vehicles() ## gets number of chosen persons driven vehicles

SW_space = SW_id.get_starships() ## gets number of chosen persons flown spaceships

species = SW_id.get_species() ## gets chosen persons species


spe = species.items ## lists their species

SW_space2 = SW_space.items ## lists their flown starships

SW_vec = SW_data.items ## lists drivin vehicles

ld = str(SW_id) ## each item beloow this converts them into a string using str
ls = str(SW_more)
ls2 = str(spe)
ls3 = str(SW_vec)
ls4 = str(SW_space2)

## this function is the image generation, generates the image based on variables listed above
def imagegen():
	if(ls3 == "" or ls3 =="[]" and ls2 == "" or ls2 == "[]"): ## if there are no vehicles and no species listed do this
		print("ERROR 21: NO VEHICLE FOUND")
		print("ERROR 22: NO SPECIES")
		img = Image.new('RGB', (400, 400), color = (73, 109, 137))
		d = ImageDraw.Draw(img)
		d.text((10,10), ld, fill=(255,255,0))
		d.text((10,30), ls, fill=(255,255,0))
		d.text((10,60), "SPECIES NOT LISTED", fill=(255,255,0))
		d.text((10,90), "NO KNOWN VEHICLES", fill=(255,255,0))
		img.save('pil_text.png')
		print(SW_id)
		print(SW_more)
	elif(ls3 == "" or ls3 == "[]"): ## if no vehicles but there is species do this
		print("ERROR 21: NO VEHICLE FOUND")
		img = Image.new('RGB', (400, 400), color = (73, 109, 137))
		d = ImageDraw.Draw(img)
		d.text((10,10), ld, fill=(255,255,0))
		d.text((10,30), ls, fill=(255,255,0))
		d.text((10,60), ls2, fill=(255,255,0))
		d.text((10,90), "NO KNOWN VEHICLES", fill=(255,255,0))
		img.save('pil_text.png')


	else: ## if both do this
		img = Image.new('RGB', (400, 400), color = (73, 109, 137))
		d = ImageDraw.Draw(img)
		d.text((10,10), ld, fill=(255,255,0))
		d.text((10,30), ls, fill=(255,255,0))
		d.text((10,60), ls2, fill=(255,255,0))
		d.text((10,90), ls3, fill=(255,255,0))
		img.save('pil_text.png')

imagegen() ## make the image

def postToFacebook(token,message="standby"): ## posts to facebook
	graph = facebook.GraphAPI(token)

	post_id = graph.put_photo(image = open('pil_text.png', 'rb'), message = "Star Wars Person Of The Day: " )["post_id"]

postToFacebook(token,message="standby")
