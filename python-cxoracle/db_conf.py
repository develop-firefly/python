# Import cx_Oracle package: This is Python API for Oracle DB connection and Transaction
import cx_Oracle

# Path to oracle client on local machine
ora_client_config = {'orcl_client_path': '/usr/lib/oracle/21/client64'}

# Hostname, Port and Service Name for the DB connection
db_config = {'host': '192.168.1.22',
             'port': 1521,
             'service_name': 'ORCLPDB'}

# User credentials for python_api user
python_api_user_config = {'user': 'python_api',
                          'password': 'password',
                          'dsn': db_config['host'] + ':' + str(db_config['port']) + '/' + db_config['service_name']}

# User credentials for soda user
soda_user_config = {'user': 'sodauser',
                    'password': 'password',
                    'dsn': db_config['host'] + ':' + str(db_config['port']) + '/' + db_config['service_name']}

# Comment Specific only for privileged connection
'''
Do not convert value of mode to a string as 'cx_Oracle.SYSDBA', since cx_Oracle.SYSDBA eventually
refers to mode = 2. if its converted to string you will continue to see
TypeError: an integer is required (got type str) while attempting to connect
'''
privileged_user = {'user': 'SYS',
                   'password': 'password',
                   'dsn': db_config['host'] + ':' + str(db_config['port']) + '/' + db_config['service_name'],
                   'mode': cx_Oracle.SYSDBA}

