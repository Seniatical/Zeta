from setuptools import setup, find_packages

classifiers = [
  'Development Status :: 5 - Production/Stable',
  'Intended Audience :: Developers',
  'Operating System :: OS Independent',
  'License :: OSI Approved :: Apache License',
  'Programming Language :: Python :: 3'
]

setup(
  name='Zeta',
  version='0.0.1',
  description='A module which allows you to create or use various ciphers with minimal effort',
  long_description=open('README.md').read(),
  long_description_content_type = "text/markdown",
  url = "https://github.com/Seniatical/Zeta/", 
  project_urls={
   "Documentation": "https://github.com/Seniatical/Zeta/",
   "Issue tracker": "https://github.com/Seniatical/Zeta/issues",
   },
  author='Seniatical',
  author_email='smelted02@gmail.com',
  license='Apache', 
  classifiers=classifiers,
  keywords='decoder,encoder,ciphers,hashmap', 
  packages=find_packages(),
  install_requires=[''] 
)
