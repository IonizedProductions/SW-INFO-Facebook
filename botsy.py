import os
import facebook
import random
import swapi
from PIL import Image, ImageDraw

token = "your token here :P"

def pes():
	rs = random.randint(1,82)
	return rs


SW_id = swapi.get_person(pes())

SW_more = SW_id.get_homeworld()

SW_data = SW_id.get_vehicles()

SW_vec = SW_data.items

species = SW_id.get_species()
spe = species.items

ld = str(SW_id)
ls = str(SW_more)
ls2 = str(spe)
ls3 = str(SW_vec)
def imagegen():
	if(ls3 == "" or ls3 =="[]" and ls2 == "" or ls2 == "[]"):
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
	elif(ls3 == "" or ls3 == "[]"):
		print("ERROR 21: NO VEHICLE FOUND")
		img = Image.new('RGB', (400, 400), color = (73, 109, 137))
		d = ImageDraw.Draw(img)
		d.text((10,10), ld, fill=(255,255,0))
		d.text((10,30), ls, fill=(255,255,0))
		d.text((10,60), ls2, fill=(255,255,0))
		d.text((10,90), "NO KNOWN VEHICLES", fill=(255,255,0))
		img.save('pil_text.png')


	else:
		img = Image.new('RGB', (400, 400), color = (73, 109, 137))
		d = ImageDraw.Draw(img)
		d.text((10,10), ld, fill=(255,255,0))
		d.text((10,30), ls, fill=(255,255,0))
		d.text((10,60), ls2, fill=(255,255,0))
		d.text((10,90), ls3, fill=(255,255,0))
		img.save('pil_text.png')

imagegen()

def postToFacebook(token,message="standby"):
	graph = facebook.GraphAPI(token)

	post_id = graph.put_photo(image = open('pil_text.png', 'rb'), message = SW_id )["post_id"]

postToFacebook(token,message="standby")
