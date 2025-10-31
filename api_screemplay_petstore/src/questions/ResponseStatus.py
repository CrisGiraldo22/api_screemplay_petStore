class ReponseStatus:
    def answeres_by(self,actor):
        response = getattr(actor, "last_response",None)
        if response is None:
            raise ValueError("El actor no tiene una respuesta previa")
        return response.status_code 