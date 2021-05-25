from django.test import TestCase
from django.contrib.auth import get_user_model
# Create your tests here.

User = get_user_model()

class RegisrationTest(TestCase):
    def setUp(self):
        user_pw = "somerandompassword"
        user = User.objects.create(email="hello@non-valig.com",password=user_pw)
        self.user_pw = user_pw
        user.iS_staff = True
        user.is_superuser = True
        user.save()
        user.set_password(user_pw)

    def test_User_Exists(self):
        user_count = User.objects.all().count()
        self.assertEqual(user_count, 1)
        self.assertNotEqual(user_count, 0)

    def test_userpassword(self):
        user = User.objects.get(email__iexact = "hello@non-valig.com")
        self.assertTrue(user.check_password(self.user_pw))