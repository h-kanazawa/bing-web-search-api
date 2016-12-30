Bing Web Search API
==========================
| Python Client for Bing API v5, Web Search


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
