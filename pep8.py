#CamelCase
class UserAdmin():


    # Identacion: 4 Espacion (no tabs)
    # Parametros separados por , 1 espacip


    def __init__(self, username, password = ''):
        self.username = username
        self.password = password


    def set_password(self):
        pass

#snake_case
cody_user = UserAdmin('cody')  