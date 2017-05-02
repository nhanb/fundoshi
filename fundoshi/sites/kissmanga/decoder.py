import re
from Crypto.Hash import SHA256
from Crypto.Cipher import AES
from base64 import b64decode
import binascii

# Ported from unobfuscated wrapKA function:
# https://gist.github.com/nhanb/74542c36d3dcc5dde4e90b34437fb523

# AFAIK this is hardcoded in http://kissmanga.com/Scripts/lo.js and is never
# redefined elsewhere so it's ok to hardcode it here too.
_iv = binascii.a2b_hex('a5e8e2e9c2721be0a84ad660c472c1f3')


def _generate_sha(plaintext):
    sha = SHA256.new()
    sha.update(plaintext.encode('utf-8'))
    return sha.digest()


# This is also found in lo.js
_default_key = _generate_sha('mshsdf832nsdbash20asdm')


def decode_url(input, key):
    encoded = b64decode(input)
    dec = AES.new(key=key, mode=AES.MODE_CBC, IV=_iv)
    result = dec.decrypt(encoded)
    unpadded = result[:-result[-1]]
    return unpadded.decode()


def _crypto_tag(tag):
    return tag.name == 'script' and tag.text and 'chko' in tag.text


def get_key(soup):
    '''
    On each chapter page, a <script> tag is inserted that overrides the
    encryption key, so we'll need to find that. Only fall back to default key
    if such a tag is not found.
    '''

    crypto_tag = soup.find(_crypto_tag)
    if crypto_tag is None:
        return _default_key

    pat = re.compile('\["(.+)"\]')
    keys = pat.findall(crypto_tag.text)
    if len(keys) > 0:
        unhashed_key = keys[-1].encode().decode('unicode_escape')
        return _generate_sha(unhashed_key)
    else:
        return _default_key
