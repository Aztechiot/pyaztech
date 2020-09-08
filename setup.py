    from setuptools import setup

setup(name='pyaztech',
      version='0.3.5',
      description='Interface for Aztech',
      url='https://github.com/Aztechiot/pyaztech',
      author='Aztechiot',
      author_email='warren.lee@aztech.com',
      license='GPLv3',
      packages=['pyaztech'],
      install_requires=['click', 'deprecation'],
      python_requires='>=3.5',
      entry_points={
            'console_scripts': [
                  'pyaztech=pyaztech.cli:cli',
            ],
      },
      zip_safe=False)
