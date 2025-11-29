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
        self.__usuario = self.cargarUsuarios()

    