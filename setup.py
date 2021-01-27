 
from distutils.core import setup
setup(name='whatsAppGreeting',
		version='0.0.1',
		py_modules=['app.appCore', 'app.main'],
		scripts=['main.py'],
		install_requires=['selenium', 'bs4'],
		author='Pardo Agustin',
		license='MIT license',
		author_email='agustinmpardo@gmail.com',
		description='whatsApp send respond automatically',
		url='https://github.com/AgustinPardo/whatsAppGreeting',
		long_description='',
		)