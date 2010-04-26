from django.test import TestCase

from chronograph.models import parse_environment_vars

class ChronographModelEnvironmentParsing(TestCase):
    def test_parser(self):
        tests = [("K=v\nK2=v2K3\nv#=", {'K': 'v', 'K2': 'v2K3'}),]

        for text, expected in tests:
            items = parse_environment_vars(text)
            self.assertEquals(items, expected)
