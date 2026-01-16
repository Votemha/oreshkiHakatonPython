from django.test import TestCase
from django.urls import reverse
from .models import User, Note

class UserModelTest(TestCase):
    '''Тесты пользователя'''

    def test_create_user(self):
        user = User.objects.create(
            name="Артём",
            email="art@gmail.com",
            password="12345"
        )

        self.assertEqual(user.name, "Артём")
        self.assertEqual(user.email, "art@gmail.com")
        self.assertEqual(User.objects.count(), 1)

class NoteModelTest(TestCase):
    '''Тест заметок'''

    def setUp(self):
        self.user = User.objects.create(
            name="Евгения",
            email="jeny@gmail.com",
            password="12345"
        )

    def test_create_note(self):
        note = Note.objects.create(
            user=self.user,
            title="Заголовок",
            text="Текст заметки",
            tags="test, 1"
        )

        self.assertEqual(note.user, self.user)
        self.assertEqual(note.title, "Заголовок")
        self.assertEqual(Note.objects.count(), 1)

class IndexViewTest(TestCase):
    '''Тест view'''

    def setUp(self):
        User.objects.create(
            name="Саша",
            email="sasha@gmail.com",
            password="123"
        )

    def test_index_page_contains_user(self):
        response = self.client.get('/')
        self.assertContains(response, "Саша")

class UserCreateViewTest(TestCase):
    '''Тест создание пользователя'''

    def test_create_user(self):
        response = self.client.post('/users/create/', {
            'name': 'Сергей',
            'email': 'sergey@test.com',
            'password': 'qwerty'
        })

        self.assertEqual(User.objects.count(), 1)
        self.assertRedirects(response, '/')

class NoteCreateViewTest(TestCase):
    '''Тест создание заметки'''

    def setUp(self):
        self.user = User.objects.create(
            name="Олег",
            email="oleg@test.com",
            password="pass"
        )

    def test_create_note(self):
        response = self.client.post(f'/notes/create/{self.user.id}/', {
            'title': 'Заголовок',
            'text': 'Текст',
            'tags': 'test'
        })

        self.assertEqual(Note.objects.count(), 1)
        self.assertRedirects(response, f'/notes/{self.user.id}/')

class NoteDeleteViewTest(TestCase):
    '''Тест удаление заметки'''

    def setUp(self):
        self.user = User.objects.create(
            name="Максим",
            email="max@test.com",
            password="123"
        )
        self.note = Note.objects.create(
            user=self.user,
            title="Удалить",
            text="Тест"
        )

    def test_delete_note(self):
        response = self.client.get(f'/notes/delete/{self.note.id}/')

        self.assertEqual(Note.objects.count(), 0)
        self.assertRedirects(response, f'/notes/{self.user.id}/')