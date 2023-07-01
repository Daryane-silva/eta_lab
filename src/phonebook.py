class Phonebook:

    def __init__(self):
        self.entries = {'POLICIA': '190'}

    def add(self, name, number):
        """

        :param name: name of person in string
        :param number: number of person in string
        :return: 'Nome invalido' or 'Numero invalido' or 'Numero adicionado'
        """
        if name is None:
            return 'Nome invalido'

        if type(name) != str:
            return 'Nome invalido'

        if name == '':
            return 'Nome invalido'

        if '#' in name:
            return 'Nome invalido'

        # O retorno deve ser "Nome invalido"
        if '@' in name:
            return 'Nome invalido'

        if '!' in name:
            return 'Nome invalido'

        # O retorno deve ser "Nome invalido"
        if '$' in name:
            return 'Nome invalido'

        if '%' in name:
            return 'Nome invalido'

        # O retorno deve ser "Numero invalido"
        if len(number) == 0:
            return 'Numero invalido'

        if name not in self.entries:
            self.entries[name] = number

        return 'Numero adicionado'

    #validar se é string e quando o nome é vazio


    def lookup(self, name):
        """
        :param name: name of person in string
        :return: return number of person with name
        """
        # O retorno deve ser "Nome invalido"
        if name is None:
            return 'Nome invalido'

        if type(name) != str:
            return 'Nome invalido'

        if name == '':
            return 'Nome invalido'

        if '#' in name:
            return 'Nome invalido'

        if '@' in name:
            return 'Nome invalido'

        # O retorno deve ser "Nome invalido"
        if '!' in name:
            return 'Nome invalido'

        if '$' in name:
            return 'Nome invalido'

        # O retorno deve ser "Nome invalido"
        if '%' in name:
            return 'Nome invalido'

        if self.entries.get(name) is None:
            return 'Nome não existe'

        return self.entries[name]
    #validar se o nome existe

    def get_names(self):
        """

        :return: return all names in phonebook
        """
        if len(self.entries) > 0:
            result = list()
            for name, number in self.entries.items():
                result.append({name})
            return result
        else:
            return None
    #exibir mensagem quando a lista estiver vazia

    def get_numbers(self):
        """

        :return: return all numbers in phonebook
        """
        if len(self.entries) > 0:
            result = list()
            for name, number in self.entries.items():
                result.append({number})
            return result
        else:
            return None
    #exibir mensagem quando a lista estiver vazia

    def clear(self):
        """
        Clear all phonebook
        :return: return 'phonebook limpado'
        """

        if len(self.entries) > 0:
            self.entries = {}
            return 'phonebook limpado'
        else:
            return 'Lista vazia'
    #exibir mensagem quando a lista estiver vazia

    def search(self, search_name):
        """
        Search all substring with search_name
        :param search_name: string with name for search
        :return: return list with results of search
        """
        if len(self.entries) > 0:
            result = list()
            for name, number in self.entries.items():
                if search_name in name:
                    result.append({name, number})
                return result
        else:
            return None

    # mostrar mensagem quando o nome não existe na lista
    # validar nome e número inválidos

    def get_phonebook_sorted(self):
        """

        :return: return phonebook in sorted order
        """
        # deve retornar ordenado
        if len(self.entries) > 0:
            result = list(self.entries)
            result.sort()
            return result
        else:
            return None
    # mostrar mensagem quando a lista estiver vazia
    # validar nome e número inválidos
    # avaliar se deveria retornar uma lista

    def get_phonebook_reverse(self):
        """

        :return: return phonebook in reverse sorted order
        """
        # deve retornar ordenado
        if len(self.entries) > 0:
            result = list(self.entries)
            result.reverse()
            return result
        else:
            return None

    # código não valida se existe o nome a ser deletado
    def delete(self, name):
        """
        Delete person with name
        :param name: String with name
        :return: return 'Numero deletado'
        """
        if len(self.entries) > 0:
            if self.entries.get(name) is not None:
                self.entries.pop(name)
                return 'Numero deletado'
            else:
                return 'Nome não existe'
        else:
            return 'Lista vazia'

    def change_number(self, name, number):
        if len(number) == 0:
            return 'Numero invalido'

        if len(self.entries) > 0:
            if self.entries.get(name) is not None:
                self.entries[name] = number
                return 'Numero alterado'
            else:
                return 'Nome não existe'
        else:
            return 'Lista vazia'

    def get_name_by_number(self, search_number):
        if len(self.entries) > 0:
            for name, number in self.entries.items():
                if search_number in number:
                    return name
            else:
                return 'Nome não existe'
        else:
            return 'Lista vazia'