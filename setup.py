from setuptools import setup, find_packages
from glob import glob
import sys


data_files = [['lib', glob('lib/*')]]
if len(sys.argv) > 1 and (sys.argv[1] == 'bdist_wininst' or sys.argv[1] == 'bdist_msi'):
 for file in data_files:
  file[0] = '\\PURELIB\\accessible_output\\%s' % file[0]

setup(
 name = 'sound_lib',
 author = 'Christopher Toth',
 author_email = 'q@qwitter-client.net',
 version = '0.4.0',
 url = 'http://www.qwitter-client.net',
 description = 'Pythonic wrapper to the Bass sound library',
 #long_description = open('README.txt').read(),
 package_dir = {'sound_lib':'sound_lib'},
 packages = find_packages(),
 data_files = data_files,
 classifiers = [
  'Development Status :: 4 - Beta',
  'Intended Audience :: Developers',
  #'Operating System :: Microsoft :: Windows',
  'Programming Language :: Python',
  'License :: OSI Approved :: MIT License',
'Topic :: Software Development :: Libraries'
],
)
