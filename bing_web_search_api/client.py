# -*- coding: utf-8 -*-

from urllib.parse import quote_plus

import httplib2

API_BASE_URL = 'https://api.cognitive.microsoft.com/'
API_VERSION = '5.0'
API_URL_TEMPLATE = '{}/bing/v{}{}'
GET = 'GET'
MAX_URL_LENGTH = 2048


class Client(object):
    """Client for Bing Web Search API

    :type apikey: str
    :param apikey: Ocp-Apim-Subscription-Key
    """

    def __init__(self, apikey=None, api_version=None):
        self.apikey = apikey
        self.api_version = api_version or API_VERSION

    def search(self,
               q=None,
               count=None,
               offset=None,
               cc=None,
               freshness=None,
               mkt=None,
               responseFilter=None,
               safeSearch=None,
               setLang=None,
               textDecorations=None,
               textFormat=None):
        """
        :type q: str
        :param q: The user's search query string. (required)

        :return: (response, content)
        types are same with return of httplib2.request
        """
        SEARCH = '/search'
        if not q:
            return Exception('The argument "q" is required.')

        query_params = _build_query_params(param_list=[
            ('q', q),
            ('count', count),
            ('offset', offset),
            ('cc', cc),
            ('freshness', freshness),
            ('mkt', mkt),
            ('responseFilter', responseFilter),
            ('safeSearch', safeSearch),
            ('setLang', setLang),
            ('textDecorations', textDecorations),
            ('textFormat', textFormat)
        ])

        url = _build_api_url(
            api_url_template=API_URL_TEMPLATE,
            api_base_url=API_BASE_URL,
            api_version=self.api_version,
            path=SEARCH,
            query_params=query_params
        )

        if len(url) > MAX_URL_LENGTH:
            return Exception('The maximam URL length is 2048. '
                             'but actual is {}.'.format(len(url)))

        headers = {
            'Ocp-Apim-Subscription-Key': self.apikey,
        }

        http = httplib2.Http()
        return http.request(url, GET, headers=headers)


def _build_api_url(api_url_template=None,
                   api_base_url=None,
                   api_version=None,
                   path=None,
                   query_params=None):

    """construct api URL"""
    url = api_url_template.format(
        api_base_url,
        api_version,
        path
    )

    if query_params:
        url += '?' + query_params

    return url


def _build_query_params(param_list=[]):
    return '&'.join(
        [p[0] + '=' + quote_plus(str(p[1])) for p in param_list if p[1]]
    )
