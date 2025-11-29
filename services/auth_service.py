import json
import os
import hashlib
from models.user import User

class AuthService:
    """
    Servicio encargado de:
    - Reguistrar usuarios
    - Iniciar sesion
    - guardar y leer usuarios del archivo

    """

    DATA_PATH = "data/usuarios.json"

    def __init__(self):
        self.__usuarios = self.cargarUsuarios()

    
    # CARGA Y GUARDADO

    def cargarUsuarios(self):
        """ Carga los usuarios desde el archivo JSON."""
        if not os.path.exists(self.DATA_PATH):
            return {}

        with open(self.DATA_PATH, "r") as f:
            return json.load(f)

        