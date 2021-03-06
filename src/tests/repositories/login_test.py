import unittest
from repositories.user_repository import user_repository
from entities.user import User

class TestUsers(unittest.TestCase):
    def setUp(self):
        user_repository.delete_all()
        self.user_test = User("TestUser", "TestPassword")
        self.user_tonttu = User("Tonttu", "TonttuPassword")
        self.user_kayttaja = User("Kayttaja", "KayttajaPassword")

    def test_username_and_password_is_set_correctly(self):
        user_repository.create(self.user_test)
        users = user_repository.find_all()
        self.assertEqual(len(users), 1)
        self.assertEqual(users[0].username, self.user_test.username)

    def test_username_and_password_works_if_correct(self):
        user_repository.create(self.user_test)
        user = user_repository.find_by_username(self.user_test.username)
        self.assertEqual(user.username, self.user_test.username)

    def test_find_all_when_multiple_users(self):
        user_repository.create(self.user_test)
        user_repository.create(self.user_tonttu)
        user_repository.create(self.user_kayttaja)
        users = user_repository.find_all()
        self.assertEqual(len(users), 3)
        self.assertEqual(users[0].username, self.user_test.username)
        self.assertEqual(users[1].username, self.user_tonttu.username)
        self.assertEqual(users[2].username, self.user_kayttaja.username)

