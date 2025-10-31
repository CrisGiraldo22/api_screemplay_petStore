class pet:
    def __init__(self, pet_id, name, status):
        self.id = pet_id
        self.name = name
        self.status =status

    def dictionary(self):
        """Convierte el objeto en un diccionario listo para enviar en json"""  
        return {
            "id":self.id,
            "name":self.name,
            "status":self.status
        }  