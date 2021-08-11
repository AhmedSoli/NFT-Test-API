# main.py
from fastapi import FastAPI
app = FastAPI()

metadata = {
	1: {
		"attributes": [
			{
			  "trait_type": "Base", 
			  "value": "narwhal"
			}, 
			{
			  "trait_type": "Eyes", 
			  "value": "sleepy"
			}, 
			{
			  "trait_type": "Mouth", 
			  "value": "cute"
			}, 
			{
			  "trait_type": "Level", 
			  "value": 4
			}, 
			{
			  "trait_type": "Stamina", 
			  "value": 90.2
			}, 
			{
			  "trait_type": "Personality", 
			  "value": "Boring"
			}, 
			{
			  "display_type": "boost_number", 
			  "trait_type": "Aqua Power", 
			  "value": 10
			}, 
			{
			  "display_type": "boost_percentage", 
			  "trait_type": "Stamina Increase", 
			  "value": 5
			}, 
			{
			  "display_type": "number", 
			  "trait_type": "Generation", 
			  "value": 1
			}
	  ], 
	  "description": "Friendly OpenSea Creature that enjoys long swims in the ocean.", 
	  "external_url": "https://openseacreatures.io/3", 
	  "image": "https://storage.googleapis.com/opensea-prod.appspot.com/creature/3.png", 
	  "name": "Dave Starbelly"
	},
	2: {
		"attributes": [
			{
			  "trait_type": "Base", 
			  "value": "narwhal"
			}, 
			{
			  "trait_type": "Eyes", 
			  "value": "sleepy"
			}, 
			{
			  "trait_type": "Mouth", 
			  "value": "cute"
			}, 
			{
			  "trait_type": "Level", 
			  "value": 4
			}, 
			{
			  "trait_type": "Stamina", 
			  "value": 90.2
			}, 
			{
			  "trait_type": "Personality", 
			  "value": "Boring"
			}, 
			{
			  "display_type": "boost_number", 
			  "trait_type": "Aqua Power", 
			  "value": 10
			}, 
			{
			  "display_type": "boost_percentage", 
			  "trait_type": "Stamina Increase", 
			  "value": 5
			}, 
			{
			  "display_type": "number", 
			  "trait_type": "Generation", 
			  "value": 1
			}
	  ], 
	  "description": "Friendly OpenSea Creature that enjoys long swims in the ocean.", 
	  "external_url": "https://openseacreatures.io/3", 
	  "image": "https://storage.googleapis.com/opensea-prod.appspot.com/creature/3.png", 
	  "name": "Dave Starbelly"
	},
	3: {
		"attributes": [
			{
			  "trait_type": "Base", 
			  "value": "narwhal"
			}, 
			{
			  "trait_type": "Eyes", 
			  "value": "sleepy"
			}, 
			{
			  "trait_type": "Mouth", 
			  "value": "cute"
			}, 
			{
			  "trait_type": "Level", 
			  "value": 4
			}, 
			{
			  "trait_type": "Stamina", 
			  "value": 90.2
			}, 
			{
			  "trait_type": "Personality", 
			  "value": "Boring"
			}, 
			{
			  "display_type": "boost_number", 
			  "trait_type": "Aqua Power", 
			  "value": 10
			}, 
			{
			  "display_type": "boost_percentage", 
			  "trait_type": "Stamina Increase", 
			  "value": 5
			}, 
			{
			  "display_type": "number", 
			  "trait_type": "Generation", 
			  "value": 1
			}
	  ], 
	  "description": "Friendly OpenSea Creature that enjoys long swims in the ocean.", 
	  "external_url": "https://openseacreatures.io/3", 
	  "image": "https://storage.googleapis.com/opensea-prod.appspot.com/creature/3.png", 
	  "name": "Dave Starbelly"
	}	
}

@app.get("/tokens/{tokenId}")
def hello(tokenId : int):
	if tokenId in metadata:
		return metadata[tokenId]
	else:
		return metadata[1]