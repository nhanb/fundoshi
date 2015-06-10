import requests_cache
requests_cache.install_cache('test_cache', allowable_methods=('GET', 'POST'))

import nose
nose.main()
