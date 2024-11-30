from io import BytesIO

from PIL import Image
from django.core.files.uploadedfile import SimpleUploadedFile
from django.test import TestCase
from django.urls import reverse

from catalog.models import Building
from catalog.tests.factories import BuildingFactory, TypeOfBuildingFactory
from user.tests.factories import UserFactory


class BuildingListView(TestCase):

    def setUp(self):
        BuildingFactory.create_batch(10)

    def test_building_list_status_code(self):
        response = self.client.get(reverse('index'))
        self.assertEqual(response.status_code, 200)

    def test_pagination_building_list(self):
        response = self.client.get(reverse('index'))
        self.assertIn('page_obj', response.context)
        self.assertEqual(len(response.context['page_obj']), 4)
        self.assertEqual(Building.objects.count(), 10)


class BuildingDetail(TestCase):

    def setUp(self):
        self.building =BuildingFactory.create()
        self.user_owner = UserFactory.create(role='owner')
        self.user_buyer = UserFactory.create(role='buyer')
        self.client.force_login(self.user_owner)
        self.type_of_building = TypeOfBuildingFactory.create(type_of_building='apartment')

    def test_detail_status_code(self):
        response = self.client.get(reverse('building', args=[self.building.id]))
        self.assertEqual(response.status_code, 200)

    def test_only_owner_can_add_building(self):
        image = SimpleUploadedFile("test_image.jpg", b"file_content", content_type="image/jpeg")
        form_data = {
            'title': 'Test Building',
            'type_of_building': self.type_of_building.id,
            'price': 500000.0,
            'year_of_construction': 2000,
            'square': 100,
            'description': 'A nice building',
            'image_path': image
        }
        response = self.client.post(reverse('creation'), data=form_data)
        self.assertEqual(response.status_code, 200)

    def test_not_owner_cant_add_building(self):
        self.client.logout()
        self.client.force_login(self.user_buyer)
        image = SimpleUploadedFile(
            "test_image.jpg",
            b"file_content",
            content_type="image/jpeg"
        )
        form_data = {
            'title': 'Test Building',
            'type_of_building': self.type_of_building.id,
            'price': 500000.0,
            'year_of_construction': 2000,
            'square': 100,
            'description': 'A nice building',
            'image_path': image
        }
        response = self.client.post(reverse('creation'), data=form_data)
        self.assertEqual(response.status_code, 403)

    def test_success_redirect_to_url(self):
        img = Image.new('RGB', (100, 100), color=(255, 255, 255))
        img_bytes = BytesIO()
        img.save(img_bytes, format='JPEG')
        img_bytes.seek(0)
        image = SimpleUploadedFile(
            "test_image.jpg",
            img_bytes.read(),
            content_type="image/jpeg")
        form_data = {
            'title': 'Test Building',
            'type_of_building': self.type_of_building.id,
            'price': 500000.0,
            'year_of_construction': 2000,
            'square': 100,
            'description': 'A nice building',
            'image_path': image
        }
        response = self.client.post(reverse('creation'), data=form_data)
        new_building = Building.objects.last()
        self.assertRedirects(response, reverse('building', kwargs={'pk':new_building.pk}))

    def test_form_missing_field(self):
        image = SimpleUploadedFile(
            "test_image.jpg",
            b"file_content",
            content_type="image/jpeg")
        form_data = {
            'type_of_building': self.type_of_building.id,
            'price': 500000.0,
            'year_of_construction': 2000,
            'square': 100,
            'description': 'A nice building',
            'image_path': image
        }
        response = self.client.post(reverse('creation'), data=form_data)
        form = response.context.get('form')
        self.assertTrue(form.errors)
        self.assertIn('title', form.errors)
        self.assertEqual(form.errors['title'], ['This field is required.'])


class ListOfMyBuilding(TestCase):

    def setUp(self):
        self.user_owner = UserFactory.create(role='owner')
        self.user_other_owner = UserFactory.create(role='owner')
        self.user_buyer = UserFactory.create(role='buyer')

    def test_only_owner_can_view_his_list(self):
        self.client.force_login(self.user_owner)
        response = self.client.get(reverse('my_catalog', args=[self.user_owner.pk]))
        self.assertEqual(response.status_code, 200)

    def test_buyer_cant_view_his_catalog(self):
        self.client.force_login(self.user_buyer)
        response = self.client.get(reverse('my_catalog', args=[self.user_buyer.pk]))
        self.assertEqual(response.status_code, 403)

    def test_owner_list_has_only_his_buildings(self):
        self.client.force_login(self.user_owner)
        self.building_of_owner = BuildingFactory.create(user_id=self.user_owner)
        self.building_of_other_owner = BuildingFactory.create(user_id=self.user_other_owner)
        response = self.client.get(reverse('my_catalog', args=[self.user_owner.pk]))
        user_buildings = response.context['user_buildings']
        for field in user_buildings:
            self.assertEqual(field.user_id, self.user_owner)

    def test_right_pagination(self):
        self.client.force_login(self.user_owner)
        BuildingFactory.create_batch(20, user_id=self.user_owner)
        response = self.client.get(reverse('my_catalog', args=[self.user_owner.id]))
        self.assertEqual(len(response.context['user_buildings']), 2)

    def test_right_template(self):
        self.client.force_login(self.user_owner)
        response = self.client.get(reverse('my_catalog', args=[self.user_owner.pk]))
        self.assertTemplateUsed(response, 'my_catalog.html')

    def test_empty_list_of_building(self):
        self.client.force_login(self.user_owner)
        response = self.client.get(reverse('my_catalog', args=[self.user_owner.pk]))
        self.assertContains(response, 'У вас пока нет своих объектов')


class DeleteBuilding(TestCase):

    def setUp(self):
        self.owner_one = UserFactory.create(role='owner')
        self.owner_two = UserFactory.create(role='owner')
        self.buyer = UserFactory.create(role='buyer')
        self.building = BuildingFactory.create(user_id=self.owner_one)

    def test_right_redirect(self):
        self.client.force_login(self.owner_one)
        response = self.client.post(reverse('delete', args=[self.building.id]))
        self.assertRedirects(response, reverse('my_catalog', args=[self.owner_one.id]))

    def test_only_owner_can_delete_his_building(self):
        self.client.force_login(self.owner_one)
        response = self.client.post(reverse('delete', args=[self.building.id]))
        self.assertEqual(response.status_code, 302)
        self.assertFalse(Building.objects.filter(id=self.building.id).exists())

    def test_other_owner_cant_delete(self):
        self.client.force_login(self.owner_two)
        response = self.client.post(reverse('delete', args=[self.building.id]))
        self.assertEqual(response.status_code, 403)

    def test_buyer_cant_delete(self):
        self.client.force_login(self.buyer)
        response = self.client.post(reverse('delete', args=[self.building.id]))
        self.assertEqual(response.status_code, 403)

    def test_unauthenticated_cant_delete_building(self):
        response = self.client.post(reverse('delete', args=[self.building.id]))
        self.assertEqual(response.status_code, 403)


class UpdateBuilding(TestCase):

    def setUp(self):
        self.user_owner = UserFactory.create(role='owner')
        self.user_other_owner = UserFactory.create(role='owner')
        self.user_buyer = UserFactory.create(role='buyer')
        self.type_of_building = TypeOfBuildingFactory.create()

    def test_success_update_building_by_owner(self):
        img = Image.new('RGB', (100, 100), color=(255, 255, 255))
        img_bytes = BytesIO()
        img.save(img_bytes, format='JPEG')
        img_bytes.seek(0)
        image = SimpleUploadedFile(
            "test_image.jpg",
            img_bytes.read(),
            content_type="image/jpeg"
        )
        form_data = {
            'title': 'Test Building',
            'type_of_building': self.type_of_building.id,
            'price': 500000.0,
            'year_of_construction': 2000,
            'square': 100,
            'description': 'A nice building',
            'image_path': image
        }
        self.client.force_login(self.user_owner)
        building = BuildingFactory.create(user_id=self.user_owner)
        response = self.client.post(reverse('change_data', args=[building.pk]), data=form_data)
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse('my_catalog', args=[self.user_owner.id]))

    def test_other_owner_cant_update_other_building(self):
        self.client.force_login(self.user_other_owner)
        img = Image.new('RGB', (100, 100), color=(255, 255, 255))
        img_bytes = BytesIO()
        img.save(img_bytes, format='JPEG')
        img_bytes.seek(0)
        image = SimpleUploadedFile(
            "test_image.jpg",
            img_bytes.read(),
            content_type="image/jpeg"
        )
        form_data = {
            'title': 'Test Building',
            'type_of_building': self.type_of_building.id,
            'price': 500000.0,
            'year_of_construction': 2000,
            'square': 100,
            'description': 'A nice building',
            'image_path': image
        }
        building = BuildingFactory.create(user_id=self.user_owner)
        response = self.client.post(reverse('change_data', args=[building.pk]), data=form_data)
        self.assertEqual(response.status_code, 403)

    def test_buyer_cant_update_building(self):
        self.client.force_login(self.user_buyer)
        img = Image.new('RGB', (100, 100), color=(255, 255, 255))
        img_bytes = BytesIO()
        img.save(img_bytes, format='JPEG')
        img_bytes.seek(0)
        image = SimpleUploadedFile("test_image.jpg", img_bytes.read(), content_type="image/jpeg")
        form_data = {
            'title': 'Test Building',
            'type_of_building': self.type_of_building.id,
            'price': 500000.0,
            'year_of_construction': 2000,
            'square': 100,
            'description': 'A nice building',
            'image_path': image
        }
        building = BuildingFactory.create(user_id=self.user_buyer)
        response = self.client.post(reverse('change_data', args=[building.id]), data=form_data)
        self.assertEqual(response.status_code, 403)

    def test_right_template(self):
        self.client.force_login(self.user_owner)
        building = BuildingFactory.create(user_id=self.user_owner)
        response = self.client.get(reverse('change_data', args=[building.id]))
        self.assertTemplateUsed(response, 'change_data.html')


class Sorting(TestCase):

    def setUp(self):
        self.house_type = TypeOfBuildingFactory.create(type_of_building='house', id=5)
        self.apartment_type = TypeOfBuildingFactory.create(type_of_building='apartment', id=6)
        self.building_one = BuildingFactory.create_batch(5, type_of_building=self.house_type)
        self.building_two = BuildingFactory.create_batch(5, type_of_building=self.apartment_type)

    def test_without_param(self):
        response = self.client.get(reverse('sorted_building'))
        self.assertRedirects(response, reverse('index'))

    def test_with_param_type_of_building(self):
        response = self.client.get(reverse('sorted_building') + f'?category={self.house_type.id}')
        building = response.context['page_obj']
        for item in building:
            self.assertEqual(item.type_of_building, self.house_type)

    def test_with_param_square(self):
        response = self.client.get(reverse('sorted_building') + '?square=10-50')
        building = response.context['page_obj']
        for item in building:
            self.assertTrue(9 < int(item.square) < 51)

    def test_with_param_year_of_construction(self):
        response = self.client.get(reverse('sorted_building') + '?year=1900-1930')
        building = response.context.get('page_obj', None)
        for item in building:
            self.assertTrue(1899 < int(item.year_of_construction) < 1931)