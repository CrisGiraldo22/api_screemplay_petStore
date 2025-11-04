from src.actors.Actor import Actor
from src.abilities.CallApi import CallApi
from src.models.Pet import Pet
from src.tasks.AddPet import AddPet
from src.tasks.GetPetById import GetPetById
from src.tasks.UpdatePet import UpdatePet
from src.tasks.DeletePet import DeletePet
from src.questions.ResponseStatus import ResponseStatus
import random, time

BASE_URL = "https://petstore.swagger.io/v2"

def test_crud_petstore():
    cristina = Actor("Cristina").can(CallApi(BASE_URL))

    # CREATE
    pet_id = random.randint(100000, 999999)
    new_pet = Pet(pet_id, "Akira", "available")
    cristina.attempts_to(AddPet(new_pet))
    print("🔍 Status POST:", ResponseStatus().answered_by(cristina))
    print("🔍 Respuesta POST:", cristina.last_response.text)
    assert ResponseStatus().answered_by(cristina) == 200

    # Esperar un poco antes del GET
    time.sleep(1)

    # READ
    cristina.attempts_to(GetPetById(new_pet.id))
    print("\n📖 READ:", cristina.last_response.status_code)
    print(cristina.last_response.text)

    # UPDATE
    new_pet.name = "Akira_Actualizada"
    cristina.attempts_to(UpdatePet(new_pet))
    print("\n✏️ UPDATE:", cristina.last_response.status_code)
    print(cristina.last_response.text)

    # DELETE
    cristina.attempts_to(DeletePet(new_pet.id))
    print("\n🗑️ DELETE:", cristina.last_response.status_code)
    print(cristina.last_response.text)

    # VALIDACIONES
    assert ResponseStatus().answered_by(cristina) in [200, 201, 204]