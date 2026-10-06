import io
import shutil
import tempfile
from PIL import Image
from django.contrib.auth.models import User
from django.core.files.uploadedfile import SimpleUploadedFile
from django.test import override_settings
from rest_framework.test import APITestCase
from .models import Notice

MEDIA_ROOT = tempfile.mkdtemp()

@override_settings(MEDIA_ROOT=MEDIA_ROOT)
class NoticeApiTests(APITestCase):
    url = '/middleware/api/notice/'

    @classmethod
    def tearDownClass(cls):
        super().tearDownClass()
        shutil.rmtree(MEDIA_ROOT, ignore_errors=True)

    def image(self):
        buf = io.BytesIO()
        Image.new('RGB', (10, 10)).save(buf, 'PNG')
        return SimpleUploadedFile('notice.png', buf.getvalue(), content_type='image/png')

    def test_anonymous_can_read_but_not_write(self):
        Notice.objects.create(title='Hello')
        self.assertEqual(self.client.get(self.url).status_code, 200)
        self.assertIn(self.client.post(self.url, {'title': 'x'}).status_code, (401, 403))

    def test_create_with_image_returns_absolute_url(self):
        self.client.force_authenticate(User.objects.create_user('u', password='p'))
        res = self.client.post(self.url, {
            'title': 'Maintenance',
            'description': 'Down on Friday',
            'url': 'https://www.spc.int',
            'url_enabled': False,
            'image': self.image(),
        }, format='multipart')
        self.assertEqual(res.status_code, 201, res.data)
        self.assertTrue(res.data['image'].startswith('http://testserver/middleware/media/notice/'))
        self.assertFalse(res.data['url_enabled'])
        self.assertTrue(res.data['image_enabled'])

    def test_filter_enabled(self):
        Notice.objects.create(title='On', is_notice_enabled=True)
        Notice.objects.create(title='Off', is_notice_enabled=False)
        res = self.client.get(self.url, {'is_notice_enabled': 'true'})
        self.assertEqual([n['title'] for n in res.data], ['On'])

    def test_enabled_endpoint(self):
        Notice.objects.create(title='On', is_notice_enabled=True)
        Notice.objects.create(title='Off', is_notice_enabled=False)
        Notice.objects.create(title='On too')
        res = self.client.get(self.url + 'enabled/')
        self.assertEqual(res.status_code, 200)
        self.assertEqual([n['title'] for n in res.data], ['On', 'On too'])
        self.assertIn(self.client.post(self.url + 'enabled/', {}).status_code, (401, 403, 405))
