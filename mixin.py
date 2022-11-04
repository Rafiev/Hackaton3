import json


def validate_password(password):
    if len(password) < 8:
        raise Exception('Пароль слишком короткий')
    if password.isdigit() or password.isalpha():
        raise Exception('Пароль должен состоять из букв и цифр!')

class RegisterMixin:

    def register(self ,name, password):
        
        with open('user.json', 'r+') as file:
            data = json.load(file)
            __validate_name = [i for i in data if name == i['name']]
            if __validate_name:
                raise Exception('Такой user уже существует!')
            
            _new_id = self.__find_max_id(data)
            data.append({'id': _new_id,'name': name, 'password': password})
            __val_password = validate_password(password)
            with  open('user.json', 'w') as file:  
                json.dump(data, file, ensure_ascii=False, indent=4)
        
        return 'Регистрация прошла успешно !'

    def __find_max_id(self, data) -> int:
        if data:
            ids = [i['id'] for i in data]
            return max(ids) + 1
        else:
            return 0                
    

class LoginMixin:

    def login(self, name, password):
        with open('user.json', 'r') as file:
            data = json.load(file)
            __validate_name = [i for i in data if i['name'] == name]
            if __validate_name:
                if __validate_name[0]['password'] == password:
                    return 'Вы успешно залогинились !'
                else:
                    raise Exception('Неверный пароль!')
            else:
                raise Exception('Такой user не существует!')

                
class ChangePasswordMixin:
    
    def change_password(self, name, old_password, new_password):
        __validate_password = validate_password(new_password)
        with open('user.json') as file:
            data = json.load(file)
            __find_user = [i for i in data if i['name'] == name]
            if __find_user:
                if __find_user[0]['password'] == old_password:
                    __find_user[0]['password'] = new_password
                    with open('user.json', 'w') as file:
                        json.dump(data, file,ensure_ascii=False, indent=4)
                        return 'Пароль успешно изменен !'
                else:
                    raise Exception('Старый пароль указан не верно')
            else:
                raise Exception('User не найден !')


class ChangeUsernameMixin:
    
    def change_name(self, old_name, new_name):
        with open('user.json') as file:
            data = json.load(file)
            __find_user = [i for i in data if i['name'] == old_name]
            if __find_user:
                __validate_user = [i for i in data if i['name'] == new_name]
                if bool(__validate_user) == False:
                    __find_user[0]['name'] = new_name
                    with open('user.json', 'w') as file:
                        json.dump(data, file, ensure_ascii=False, indent=4)
                        return 'Имя usera успешно обновлено !'
                else:
                    print('User с таким именем уже есть !')
                    while True:
                        __data_name = [i['name'] for i in data]
                        new_name = input('Введите новое имя : ')
                        if __data_name.count(new_name) == 0:
                            __find_user[0]['name'] = new_name
                            with open('user.json', 'w') as file:
                                json.dump(data, file, ensure_ascii=False, indent=4)
                            return 'Имя usera успешно обновлено !'
                        else:
                            print('User с таким именем уже есть')
            else:
                raise Exception('User не найден !')


class CheckOwnerMixin:
    
    @staticmethod
    def check(owner:str):
        with open('user.json') as file:
            data = json.load(file)
            check_owner = [i for i in data if i['name'] == owner]
            if bool(check_owner) is False:
                raise Exception('Такого user нет в базе данных!') 
            else:
                return 'Пост создан успешно !'
