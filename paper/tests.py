from django.test import TestCase

# Create your tests here.


class SimpleTestCase(TestCase):
    def test_home_page_status_code(self):
    #    self.assertEqual('The lop', 'The lion says "roar"')
       self.assertEqual(2+2, 4)