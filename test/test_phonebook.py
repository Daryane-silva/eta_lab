from src.phonebook import Phonebook

class TestPhonebook:

    def test_add_user_com_sucesso(self):
        # Setup
        name_1 = "Fabricio"
        numero_1 = "1"
        resultado_esperado = "Numero adicionado"
        service = Phonebook()

        # Chamada
        resultado = service.add(name=name_1, number=numero_1)

        # Avaliacao
        assert resultado_esperado == resultado

    def test_add_nome_invalido(self):
        # Setup
        name_1 = "@"
        numero_1 = "1"
        resultado_esperado = "Nome invalido"
        service = Phonebook()

        # Chamada
        resultado = service.add(name=name_1, number=numero_1)

        # Avaliacao
        assert resultado_esperado == resultado

    def test_add_numero_vazio(self):
        # Setup
        name_1 = "Fabricio"
        numero_1 = ""
        resultado_esperado = "Numero invalido"
        service = Phonebook()

        # Chamada
        resultado = service.add(name=name_1, number=numero_1)

        # Avaliacao
        assert resultado_esperado == resultado

    def test_lookup_sucesso(self):
        # Setup
        name_1 = "POLICIA"
        resultado_esperado = "190"
        service = Phonebook()

        # Chamada
        resultado = service.lookup(name=name_1)

        # Avaliacao
        assert resultado_esperado == resultado

    def test_lookup_falha(self):
        # Setup
        name_1 = "#"
        resultado_esperado = "Nome invalido"
        service = Phonebook()

        # Chamada
        resultado = service.lookup(name=name_1)

        # Avaliacao
        assert resultado_esperado == resultado

    def test_lookup_nao_existe(self):
        # Setup
        name_1 = "BOMBEIROS"
        resultado_esperado = "Nome não existe"
        service = Phonebook()

        # Chamada
        resultado = service.lookup(name=name_1)

        # Avaliacao
        assert resultado_esperado == resultado

    def test_get_names(self):
        # Setup
        name_1 = "Teste"
        numero_1 = "1"
        resultado_esperado = 2
        service = Phonebook()
        service.add(name_1, numero_1)

        # Chamada
        resultado = service.get_names()

        # Avaliacao
        assert resultado_esperado == len(resultado)

    def test_get_numbers(self):
        # Setup
        name_1 = "Teste"
        numero_1 = "1"
        resultado_esperado = 2
        service = Phonebook()
        service.add(name_1, numero_1)

        # Chamada
        resultado = service.get_names()

        # Avaliacao
        assert resultado_esperado == len(resultado)

    def test_clear_sucesso(self):
        # Setup
        resultado_esperado = "phonebook limpado"
        service = Phonebook()

        # Chamada
        resultado = service.clear()

        # Avaliacao
        assert resultado_esperado == resultado

    def test_clear_falha(self):
        # Setup
        resultado_esperado = "Lista vazia"
        service = Phonebook()
        service.delete('POLICIA')

        # Chamada
        resultado = service.clear()

        # Avaliacao
        assert resultado_esperado == resultado

    def test_search(self):
        # Setup
        name_1 = "POLICIA"
        resultado_esperado = 1
        service = Phonebook()

        # Chamada
        resultado = service.search(name_1)

        # Avaliacao
        assert resultado_esperado == len(resultado)

    def test_get_phonebook_sorted_sucesso(self):
        # Setup
        name_1 = 'BOMBEIROS'
        number_1 = "193"
        resultado_esperado = name_1
        service = Phonebook()
        service.add(name=name_1, number=number_1)

        # Chamada
        resultado = service.get_phonebook_sorted()[0]

        # Avaliacao
        assert resultado_esperado == resultado

    def test_get_phonebook_reverse_sucesso(self):
        # Setup
        name_1 = 'SAMU'
        number_1 = "193"
        resultado_esperado = name_1
        service = Phonebook()
        service.add(name=name_1, number=number_1)

        # Chamada
        resultado = service.get_phonebook_reverse()[0]

        # Avaliacao
        assert resultado_esperado == resultado

    def test_delete_sucesso(self):
        # Setup
        name_1 = 'POLICIA'
        service = Phonebook()
        resultado_esperado = 'Numero deletado'

        # Chamada
        resultado = service.delete(name_1)

        # Avaliacao
        assert resultado_esperado == resultado

    def test_delete_falha(self):
        # Setup
        name_1 = 'BOMBEIROS'
        service = Phonebook()
        resultado_esperado = 'Nome não existe'

        # Chamada
        resultado = service.delete(name_1)

        # Avaliacao
        assert resultado_esperado == resultado

    def test_delete_lista_vazia(self):
        # Setup
        resultado_esperado = "Lista vazia"
        service = Phonebook()
        service.delete('POLICIA')

        # Chamada
        resultado = service.delete('POLICIA')

        # Avaliacao
        assert resultado_esperado == resultado

    def test_change_number_sucesso(self):
        # Setup
        name_1 = "POLICIA"
        numero_1 = "234"
        resultado_esperado = "Numero alterado"
        service = Phonebook()

        # Chamada
        resultado = service.change_number(name_1, numero_1)

        # Avaliacao
        assert resultado_esperado == resultado

    def test_change_number_falha(self):
        # Setup
        name_1 = "BOMBEIROS"
        numero_1 = "234"
        resultado_esperado = "Nome não existe"
        service = Phonebook()

        # Chamada
        resultado = service.change_number(name_1, numero_1)

        # Avaliacao
        assert resultado_esperado == resultado

    def test_change_number_numero_invalido(self):
        # Setup
        name_1 = "POLICIA"
        numero_1 = ""
        resultado_esperado = "Numero invalido"
        service = Phonebook()

        # Chamada
        resultado = service.change_number(name_1, numero_1)

        # Avaliacao
        assert resultado_esperado == resultado

    def test_change_number_lista_vazia(self):
        # Setup
        name_1 = "POLICIA"
        numero_1 = "234"
        resultado_esperado = "Lista vazia"
        service = Phonebook()
        service.delete('POLICIA')

        # Chamada
        resultado = service.change_number(name_1, numero_1)

        # Avaliacao
        assert resultado_esperado == resultado

    def test_get_name_by_number_sucesso(self):
        # Setup
        numero_1 = "190"
        resultado_esperado = "POLICIA"
        service = Phonebook()

        # Chamada
        resultado = service.get_name_by_number(numero_1)

        # Avaliacao
        assert resultado_esperado == resultado

    def test_get_name_by_number_falha(self):
        # Setup
        numero_1 = "234"
        resultado_esperado = "Nome não existe"
        service = Phonebook()

        # Chamada
        resultado = service.get_name_by_number(numero_1)

        # Avaliacao
        assert resultado_esperado == resultado

    def test_get_name_by_number_lista_vazia(self):
        # Setup
        numero_1 = "190"
        resultado_esperado = "Lista vazia"
        service = Phonebook()
        service.delete('POLICIA')

        # Chamada
        resultado = service.get_name_by_number(numero_1)

        # Avaliacao
        assert resultado_esperado == resultado
