from setuptools import setup, find_packages


setup(name="aurproxy",
      version="20200222.0",
      packages=find_packages(),
      install_requires=[
          'azure==4.0.0', 
          'boto==2.34.0', 
          'boto3==1.9.188', 
          'commandr==1.3.2', 
          'Flask-RESTful==0.3.5',
          'gevent==1.0.2', 
          'Jinja2==2.10.1',
          'MarkupSafe>=0.23',
          'kazoo==2.0', 
          'librato-metrics==0.7.0', 
          'psutil==2.2.1', 
          'python-dateutil==2.4.2', 
          'raven==5.1.1', 
          'requests>=2.16', 
          'urllib3==1.23',
          # https://bitbucket.org/stoneleaf/enum34/issues/27/enum34-118-broken
          'enum34<1.1.8'
      ])
