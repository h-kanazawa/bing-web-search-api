Bing Web Search API
==========================
| Python Client for Bing API v5, Web Search

|travis| |coverage|

| See API Reference:
| https://msdn.microsoft.com/en-us/library/dn760794.aspx


Install
----------------

.. code-block:: console

    $ pip install bing-web-search-api


How to use
----------------

.. code-block:: python

    from bing_web_search_api import Client

    apikey = 'Your Ocp-Apim-Subscription-Key'
    client = Client(apikey=apikey)
    response, content = client.search(q='...')


License
----------------
See `LICENSE` _ for more information.

.. _LICENSE: https://github.com/h-kanazawa/bing-web-search-api/blob/master/LICENSE

.. |travis| image:: https://img.shields.io/travis/h-kanazawa/bing-web-search-api.svg?branch=master&style=flat
  :target: https://travis-ci.org/h-kanazawa/bing-web-search-api
.. |coverage| image:: https://coveralls.io/repos/github/h-kanazawa/bing-web-search-api/badge.svg?branch=master&style=flat
  :target: https://coveralls.io/github/h-kanazawa/bing-web-search-api?branch=master
