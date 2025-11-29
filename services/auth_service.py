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
        self.usuarios = self.cargarUsuarios()

    
    # CARGA Y GUARDADO

    def cargarUsuarios(self):

        """ Carga los usuarios desde el archivo JSON."""

        if not os.path.exists(self.DATA_PATH):
            return {}

        with open(self.DATA_PATH, "r") as f:
            return json.load(f)

    
    def guardarUsuarios(self):

        """ Guarda los usuarios en el archivo JSON."""

        with open(self.DATA_PATH, "w") as f:
            json.dump(self.usuarios, f, indent= 4)
            
    
    #HASH DE CONTRASEÑA

    def hashearPassword(self, password):

        """
        Convierte una contraseña de texto plano en un has seguro.
        """

        return hashlib.sha256(password.encode()).hexdigest()


    #REGISTRO

    def reguistrar(self,userName, password):
        """Registra un nuevo usuario si no existe"""
        
        if userName in self.usuarios:
            return False, "El usuario ya existe"
        
        passwordHash = self.hashearPassword(password)
        self.usuarios[userName] = passwordHash
        self.guardarUsuarios()

        return True, "Usuario registrado correctamente"


    #LOGIN

    def login(self, userName, password):
        """Verifica si un usuario puede iniciar sesion"""
        
        if userName not in self.usuarios:
            return False, "Usuario no registrado"

        passwordHash = self.hashearPassword(password)

        if self.usuarios[userName] == passwordHash:
            return True ,"Inicio de sesion exitosa"
        else:
            return False, "Contraseña incorrecta"
        
