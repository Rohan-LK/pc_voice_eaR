from distutils.core import setup
setup(
  name = 'pc_voice_eaR',
  packages = ['pc_voice_eaR'],
  version = '0.1',      # Start with a small number and increase it with every change you make
  license='Mozilla Public License 2.0',
  description = 'Speak and print text; listen to user; take command',
  author = 'ROHAN LAL KSHETRY',
  author_email = 'rlkshetry95@gmail.com',
  url = 'https://github.com/Rohan-LK/py_module',
  download_url = 'https://github.com/Rohan-LK/py_module/archive/v_01.tar.gz',
  keywords = ['VOICE', 'LISTEN', 'VOICE INPUT'],
  install_requires=[            # I get to this in a second
          'validators',
          'beautifulsoup4',
      ],
  classifiers=[
    'Development Status :: 3 - Alpha',      # Chose either "3 - Alpha", "4 - Beta" or "5 - Production/Stable" as the current state of your package
    'Intended Audience :: Developers',
    'Topic :: Software Development :: Build Tools',
    'License :: OSI Approved :: Mozilla Public License 2.0',
    'Programming Language :: Python :: 3',
    'Programming Language :: Python :: 3.4',
    'Programming Language :: Python :: 3.5',
    'Programming Language :: Python :: 3.6',
  ],
)
