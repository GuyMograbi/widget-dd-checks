import os
import json
import requests
import re
import unicodedata


from checks import AgentCheck

# http://code.activestate.com/recipes/577257-slugify-make-a-string-usable-in-a-url-or-filename/
_slugify_strip_re = re.compile(r'[^\w\s-]')
_slugify_hyphenate_re = re.compile(r'[-\s]+')
def _slugify(value):
    if not isinstance(value, unicode):
        value = unicode(value)
    value = unicodedata.normalize('NFKD', value).encode('ascii', 'ignore')
    value = unicode(_slugify_strip_re.sub('', value).strip().lower())
    return _slugify_hyphenate_re.sub('-', value)

# curl -H "AccountUuid: "
# url =

def get_pool_status( self, instance ):
    endpoint = instance['endpoint']
    headers = dict(
        AccountUuid=instance['account_uuid']
    )




    resp = requests.get(url= endpoint + 'admin/pools', headers=headers)
    pools = json.loads(resp.text)

    for pool in pools:
        slug_name = _slugify(pool['poolSettings']['name'])
        pool_id_str = str(pool['id'])
        # print pool_id_str + '::' + slug_name
        status = json.loads(requests.get(url= endpoint + 'admin/pools/' + pool_id_str + '/status', headers=headers).text)[pool_id_str]
        if status is not None:
            # print ( slug_name + '::' + json.dumps(status) )
            for stat in status['countPerNodeStatus']:
                value = status['countPerNodeStatus'][stat]
                # value_str = str(value)
                # print(slug_name + "__" + stat + '::' + value_str )
                self.gauge('pool_size_' + slug_name + '__' + stat, value)




class HelloCheck(AgentCheck):
    def check(self, instance):
        get_pool_status(self,instance)

# print(data)