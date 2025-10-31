class Actor:
    def __init__(self, name):
        self.name = name
        self.abilities = {}

    def can(self, ability):
        """Asigna una habilidad al actor."""
        self.abilities[type(ability)] = ability
        return self

    def ability_to(self, ability_type):
        """Obtiene una habilidad asignada.""" 
        return self.abilities.get(ability_type)

    def attempts_to(self, *tasks):
        """Ejecuta una o varias tareas."""
        for task in tasks:
            task.perform_as(self)  