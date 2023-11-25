from django.test import TestCase
from .models import Livro


class LivroModelTest(TestCase):

    def test_criacao_livro(self):
        livro = Livro.objects.create(titulo="Teste Livro", autor="Autor Teste", isbn="1234567890123")
        self.assertEqual(livro.titulo, "Teste Livro")
        self.assertEqual(livro.autor, "Autor Teste")
        self.assertEqual(livro.isbn, "1234567890123")