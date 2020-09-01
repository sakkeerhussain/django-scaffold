import os
from pathlib import Path

import dotenv

''' 
The environment of this project running for.
This should be configured in the OS environment with name 'env'
Possible values: local, prod, stg, uat.
Other config values mentioned in the config.yml should be 
   available in the env specific config file(.env.stg - for stg) 
   in the root folder or in the OS environment. The ideal 
   approach is to set all non secret items in an env specific 
   config file and secret configs such as passwords in the OS env.
'''
env = os.environ.get('env', 'local')

_base_path = Path(__file__).resolve().parent.parent.parent
_config_path = os.path.join(_base_path, f'.env.{env}')
dotenv.load_dotenv(dotenv_path=_config_path, verbose=True)

DEBUG = os.environ['DEBUG']
ALLOWED_HOSTS = os.environ['ALLOWED_HOSTS'].split(',')
