from src.abilities.CallApi import CallApi

class DeletePet:
    def __init__(self, pet_id):
        self.pet_id = id
        self.response = None

    def perform_as(self, actor):
        api = actor.ability_to(CallApi)
        endpoint = f"/pet{self.pet_id}"
        self.response = api.session.delete(f"{api.base_url}{endpoint}")
        actor.last_response = self.response
        print(f"Eliminó la mascota con id {self.pet_id} -> código {self.response.status_code}")    