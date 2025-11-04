from src.actors.Actor import Actor
from src.abilities.CallApi import CallApi
from src.tasks.GetPetsByStatus import GetPetsByStatus
from src.questions.ResponseStatus import ResponseStatus

BASE_URL = "https://petstore.swagger.io/v2"
cristina = Actor("cristina").can(CallApi(BASE_URL))
cristina.attempts_to(GetPetsByStatus("available"))
status = ResponseStatus().answered_by(cristina)
print(f"Código de respuesta recibido: {status}")

assert status == 200

