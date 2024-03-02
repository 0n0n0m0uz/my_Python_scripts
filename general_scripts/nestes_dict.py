def find(key, dictionary):
    for k, v in dictionary.items():
        if k == key:
            yield v
        elif isinstance(v, dict):
            for result in find(key, v):
                yield result
        elif isinstance(v, list):
            for d in v:
                for result in find(key, d):
                    yield result

example = {'app_url': '', 'models': [{'perms': {'add': True, 'change': True, 'delete': True}, 'add_url': '/admin/cms/news/add/', 'admin_url': '/admin/cms/news/', 'name': ''}], 'has_module_perms': True, 'name': u'CMS'}

list(find('admin_url', example))

# Find all occurences of a key in nested python dictionaries and lists - http://stackoverflow.com/questions/9807634/find-all-occurences-of-a-key-in-nested-python-dictionaries-and-lists
# This is helpful when importing deeply nested JSON file and need to access some of the inner nests

'''
def find4(keys, dictionary):
    ...:     for key in keys:
    ...:
    ...:         for k, v in dictionary.items():
    ...:             if k == key:
    ...:                 yield v
    ...:             elif isinstance(v, dict):
    ...:                 for result in find3(key, v):
    ...:                     yield result
    ...:             elif isinstance(v, list):
    ...:                 for d in v:
    ...:                     for result in find3(key, d):
    ...:                         yield result



list(find4(keys, d))

Programming routines
Python
import datetime
def date_from_webkit(webkit_timestamp):
    epoch_start = datetime.datetime(1601,1,1)
    delta = datetime.timedelta(microseconds=int(webkit_timestamp))
    print epoch_start + delta

inTime = int(raw_input('Enter a Webkit timestamp to convert:'))
date_from_webkit(inTime)


'''
