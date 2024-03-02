import requests
import os
import hashlib
import io


def download(file, url_suffix=None, checksum=None):
    if url_suffix is None:
        url_suffix = file

    if not os.path.exists(file):
        if os.path.exists('.voc'):
            url = 'https://cse6040.gatech.edu/datasets/{}'.format(url_suffix)
        else:
            url = 'https://github.com/cse6040/labs-fa17/raw/master/datasets/{}'.format(
                url_suffix)
        print("Downloading: {} ...".format(url))
        r = requests.get(url)
        with open(file, 'w', encoding=r.encoding) as f:
            f.write(r.text)

    if checksum is not None:
        with io.open(file, 'r', encoding='utf-8', errors='replace') as f:
            body = f.read()
            body_checksum = hashlib.md5(body.encode('utf-8')).hexdigest()
            assert body_checksum == checksum, \
                "Downloaded file '{}' has incorrect checksum: '{}' instead of '{}'".format(
                    file, body_checksum, checksum)

    print("'{}' is ready!".format(file))


datasets = {'student-mat.csv': '83dc97a218a3055f51cfca1e76b29036',
            'student-por.csv': 'c5fe725d1436c73e5bc16fe8c2618bf9'}

for filename, checksum in datasets.items():
    download(filename, url_suffix='ksac/{}'.format(filename), checksum=checksum)

print("\n(All data appears to be ready.)")
