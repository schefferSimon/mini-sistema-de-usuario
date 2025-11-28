class User:
    """
    Clase que representa un usuario.

    atributos:
    - userName: nombre del usuario
    - password_hash: contraseña hasheada

    """
    def __init__(self, userName, password_hash):
        self.userName = userName
        self.password_hash = password_hash

    
    def to_dict(self):
        """ Convierte el usuario a diccionario para guardarlo en JSON """
        
        return {
            "userName" : self.userName,
            "password_hash":self.password_hash
        }