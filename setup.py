#!/usr/bin/python
#!/usr/bin/python3
#!/usr/bin/env python
#!/usr/bin/env python3
# -*- coding: utf8 -*-

import setuptools
 
with open('README.md', encoding='utf8', errors='ignore') as rd:
    long_description = rd.read()
 
setuptools.setup(
    name = 'englishtobengali',
    version = '0.0.2',
    author = 'Md Jabed Ali (Jabed)',
    author_email = 'Jabed.akcc@gmail.com',
    description = '+8801670105219',
    long_description = 'Python Web Based English To Bangla Translator.',
 
    #long_description_content_type=textmarkdown,
    url = 'https://github.com/jabedparadox',
    packages = setuptools.find_packages(),
      classifiers = [
        'Operating System :: OS Independent',
                'Programming Language :: Python :: 2.7',
		'Programming Language :: Python :: 3.3',
		'Programming Language :: Python :: 3.4',
		'Programming Language :: Python :: 3.5',
		'Programming Language :: Python :: 3.6',		
        'Intended Audience :: Developers',
		'License :: OSI Approved :: MIT License',
		'Development Status :: 5 - Production/Stable',
		'Topic :: Software Development :: Libraries :: Python Modules'
      ],
    license = 'MIT',
    setup_requires=['wheel'],
    keywords = 'python bangla english translator python english to bangla translator python bangla'
     
)
