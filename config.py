"""
config.py

author: erich@emfeld.com
========================

This file acts as the configuration holder for the environment.
If you want to define a global configuration please define it here.

Naming convention:
- Use all uppercase letters.
- If needed, use underscores ('_') as separators between words 
"""

import os
# These variables defines basic root and repo for database migrations.
BASE = os.path.abspath(os.path.dirname(__file__))
MIGRATIONS = os.path.join(BASE, 'migrations')

"""
This variable lists the additional package dependencies.
Add list of python libraries you wish to install on startup in this list.
Example:
DEPENDENCIES = ['flask-mail','nose']
"""
DEPENDENCIES = []

"""
This variable defines the database connection URI used by SQLAlchemy.
Select the database connectivity that you wish to use.
The current value defaults to sqlite.
If you use database other than sqlite, remember to add the driver package 
to the DEPENDENCIES list.

examples of other database engine configurations:
MySQL:
DATABASE_URI = 'mysql://root:password01@127.0.0.1/adam'
PostgreSQL:
DATABASE_URI = 'postgresql://scott:tiger@localhost/mydatabase'
Oracle:
DATABASE_URI = 'oracle://scott:tiger@127.0.0.1:1521/sidname'
"""
DATABASE_URI = 'sqlite:///' + os.path.join(BASE, 'db/app.db')


# This is the default server port settings that will be used by the system
SERVER_PORT = 5000

# This is to determine the white space used in generating the controllers.
WHITE_SPACE = "\t"

"""
This is the settings for raw assets directory that will be used to compile asset scripts. 
Change accordingly. Defaults to BASE/raw-assets.
"""
RAW_ASSETS = os.path.join(BASE, 'raw-assets')

"""
This variable will be used to check the valid data types enterred by the
user in generator command
"""
VALID_DATA_TYPES = [
    'boolean', 'date', 'time', 'datetime', 'enum', 'interval', 'pickletype', 'schematype',
    'numeric', 'float', 'biginteger', 'smallinteger', 'smallint', 'string', 'bigint', 'int', 'integer',
    'text', 'unicode', 'unicodetext', 'binary', 'largebinary', 'blob'
]


# end of file
