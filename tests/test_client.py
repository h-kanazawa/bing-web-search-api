# -*- coding: utf-8 -*-

import unittest

from bing_web_search_api import client


class TestClient(unittest.TestCase):

    def test__build_api_url(self):
        expected = 'foo/bar/v1.2/baz?a=b&c=d'
        actual = client._build_api_url(api_url_template='{}/bar/v{}{}',
                                       api_base_url='foo',
                                       api_version='1.2',
                                       path='/baz',
                                       query_params='a=b&c=d')
        self.assertEqual(expected, actual)

    def test__build_query_params(self):
        expected = 'a=%E3%81%82%E3%81%84%E3%81%86&b=123&d=foo%3D'
        actual = client._build_query_params(param_list=[
            ('a', 'あいう'),
            ('b', 123),
            ('c', None),
            ('d', 'foo=')
        ])
        self.assertEqual(expected, actual)


def suite():
    suite = unittest.TestSuite()
    suite.addTests(unittest.makeSuite(TestClient))
    return suite
