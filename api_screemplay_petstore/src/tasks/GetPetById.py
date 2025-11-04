from src.abilities.CallApi import CallApi

class GetPetById:
    def __init__(self, pet_id):
        self.pet_id = pet_id
        self.response = None

    def perform_as(self, actor):
        api = actor.ability_to(CallApi)
        endpoint = f"/pet/{self.pet_id}"
        self.response = api.get(endpoint)
        actor.last_response = self.response
        print(f"Consulto la mascota con id {self.pet_id} -> {self.response.status_code}")    