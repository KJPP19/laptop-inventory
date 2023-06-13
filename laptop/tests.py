from django.test import TestCase
from rest_framework.test import APITestCase
from rest_framework import status
from .models import UserInfo, Laptop
from account.models import CustomAccount
from django.urls import reverse


class UserInfoApiTest(APITestCase):
    def setUp(self):
        self.user_info_url = reverse('user-info-list')
        self.user_info_create_url = reverse('add-user-info')
        self.credentials = {
            "email": "testuser@sample.com",
            "name": "testuser",
            "password": "123456789"
        }
        self.user_info_data = {
            "name": "John",
            "email": "Johnd@sample.com",
            "contact_number": "09921248433"
        }
        self.account = CustomAccount.objects.create(**self.credentials)
        self.user_info = UserInfo.objects.create(**self.user_info_data)
        self.user_info_detail_url = reverse('user-info-detail', kwargs={'user_id': self.user_info.pk})

    def test_get_user_info_list(self):
        self.client.force_authenticate(user=self.account)
        response = self.client.get(self.user_info_url)
        # print(response.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['results'][0]['name'], 'John')
        self.assertEqual(response.data['results'][0]['email'], 'Johnd@sample.com')
        self.assertEqual(response.data['count'], 1)

    def test_create_new_user_info(self):
        self.client.force_authenticate(user=self.account)
        self.new_user_info_data = {
            "name": "doe",
            "email": "doe@sample.com",
            "contact_number": "09122228624"
        }
        response = self.client.post(self.user_info_create_url, data=self.new_user_info_data)
        # print(response.data, UserInfo.objects.all().count())
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(UserInfo.objects.all().count(), 2)

    def test_create_existing_user_info(self):
        self.client.force_authenticate(user=self.account)
        response = self.client.post(self.user_info_create_url, data=self.user_info_data)
        # print(response.data['error']['email'][0])
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(response.data['error']['email'][0], 'user info with this email already exists.')
        self.assertEqual(response.data['error']['contact_number'][0], 'user info with this contact number already exists.')
        
    def test_get_single_user_info(self):
        self.client.force_authenticate(user=self.account)
        response = self.client.get(self.user_info_detail_url)
        # print(response.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['email'], 'Johnd@sample.com')
        self.assertEqual(response.data['name'], 'John')
        self.assertEqual(response.data['contact_number'], '09921248433')

    def test_update_user_info(self):
        self.client.force_authenticate(user=self.account)
        self.update_user_info_data = {
            "name": "John",
            "email": "johnnydarwin@sample.com",
            "contact_number": "09921111444"
        }
        response = self.client.put(self.user_info_detail_url, data=self.update_user_info_data)
        # print(response.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['email'], 'johnnydarwin@sample.com')

    def test_delete_user_info(self):
        self.client.force_authenticate(user=self.account)
        response = self.client.delete(self.user_info_detail_url)
        self.assertFalse(UserInfo.objects.filter(pk=self.user_info.pk).exists())


class LaptopApiTest(APITestCase):
    def setUp(self):
        self.laptop_create_url =reverse('laptop-create')
        self.laptop_url = reverse('laptop-list')
        self.user_credentials = {
            "email": "testuser@sample.com",
            "name": "testuser",
            "password": "123456789"
        }
        self.laptop_data = {
            "brand": "Apple",
            "model": "macbook air",
            "serial_number": "XXXY67U",
            "PO_number": "133211",
            "status": "assigned"
        }
        self.user_info_data = {
            "name": "John",
            "email": "Johnd@sample.com",
            "contact_number": "09921248433"
        }
        self.account = CustomAccount.objects.create(**self.user_credentials)
        self.user_info = UserInfo.objects.create(**self.user_info_data)
        self.laptop = Laptop.objects.create(**self.laptop_data)
        self.laptop.current_user = self.user_info
        self.laptop.save()

    def test_get_laptop_list(self):
        self.client.force_authenticate(user=self.account)
        response = self.client.get(self.laptop_url)
        # print(response.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['results'][0]['brand'], 'Apple')
        self.assertEqual(response.data['results'][0]['model'], 'macbook air')
        self.assertEqual(response.data['results'][0]['serial_number'], 'XXXY67U')
        self.assertEqual(response.data['results'][0]['PO_number'], '133211')
        self.assertEqual(response.data['results'][0]['current_user'], 2)
        self.assertEqual(response.data['count'], 1)

    def test_create_new_laptop(self):
        self.client.force_authenticate(user=self.account)
        self.new_laptop_data = {
            "brand": "Dell",
            "model": "XPS",
            "serial_number": "XXXY633",
            "PO_number": "133333",
            "status": "assigned",
            "current_user": 1
        }
        response = self.client.post(self.laptop_create_url, data=self.new_laptop_data)
        # print(response.data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data['brand'], 'Dell')
        self.assertEqual(response.data['model'], 'XPS')
        self.assertEqual(response.data['serial_number'], 'XXXY633')
        self.assertEqual(response.data['PO_number'], '133333')
