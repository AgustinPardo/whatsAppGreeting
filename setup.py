 
from distutils.core import setup
setup(name='whatsAppGreeting',
		version='1.0',
		packages=['app'],
		#scripts=['main.py'],
		requires=['selenium', 'bs4']
		author='Pardo Agustin',
		license='MIT license',
		author_email='agustinmpardo@gmail.com',
		description='whatsApp send respond automatically',
		url='https://github.com/AgustinPardo/whatsAppGreeting',
		)