import json
from src.abilities.CallApi import CallApi

class AddPet:
    def __init__(self, pet):
        self.pet = pet
        self.response = None

    def perform_as(self, actor):
        api = actor.ability_to(CallApi) 
        endpoint = "/pet" 
        payload = json.dumps(self.pet.dictionary())  
        headers = {"Content-Type":"application/json"}

        self.response = api.session.post(
            f"{api.base_url}{endpoint}",
            json=self.pet.dictionary()
        )
        actor.last_response = self.response
        print(f"Se creo la mascota '{self.pet.name}' con código {self.response.status_code}")