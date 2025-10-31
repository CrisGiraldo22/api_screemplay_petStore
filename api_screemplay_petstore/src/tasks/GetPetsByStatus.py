from src.abilities.CallApi import CallApi

class GetPetsByStatus:
    def __init__(self,status):
        self.status = status
        self.reponse = None


    def perform_as(self, actor):
        api = actor.ability_to(CallApi)
        endpoint = f"/pet/findByStatus"    
        params = {"status": self.status}
        self.reponse = api.get(endpoint, params=params)
        actor.last_response = self.reponse

        print(f"Actor {actor.name} obtuvo código {self.response.status_code}")