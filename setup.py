from setuptools import setup, find_packages


setup(name='mocafi-mobile-automation',
      version='1.0',
      description="Mocafi Mobile Automation testing",
      author='Manoj Sahu',
      author_email='manoj.sahu@moafi.com',
      url='https://development.mocafi.com',
      packages=find_packages(),
      install_requires=[
          "pytest==5.4.2",
          "pytest-html==2.1.1",
          "selenium==3.141.0",
          "Appium-Python-Client==1.2.0"
      ]
      )