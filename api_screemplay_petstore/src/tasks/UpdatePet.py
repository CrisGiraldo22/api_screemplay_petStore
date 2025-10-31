import json
from src.abilities.CallApi import CallApi

class UpdatePet:
    def __init__(self,pet):
        self.pet = pet
        self.response= None

def perform_as(self, actor):
    api = actor.ability_to(CallApi)
    endpoint ="/pet"
    payload = json.dumps(self.pet.dictionary())
    headers = {"Content-Type":"aplication/json"}

    self.response = api.session.put(f"{api.base_url}{endpoint}", data=payload, headers=headers)
    actor.last_response = self.response  
    print(f"Actualizó la mascota '{self.pet.name}' ->código {self.response.status_code}")    