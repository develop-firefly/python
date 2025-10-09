# Import cx_oracle package: This is Python API for Oracle DB connection and Transaction
import sys
import cx_oracle
from tabulate import tabulate
# Import the configuration file to read th attributes and values utilized in the class
import db_conf


# Class definitions should use CamelCase convention based on pep-8 guidelines
class CustomCxOracle:

    # Create an Error Code Map as Class Variable to be used in any of the custom methods
    _oracle_error_map = {955: 'Table Already Exists',
                         1109: 'Error: Database Is not Open',
                         12153: 'Error: Not currently connected to a remote host. Please check connection',
                         12154: 'Error: Could not resolve the connect identifier specified',
                         12236: 'Error: Protocol support not loaded',
                         12235: 'Error: Failure to redirect to destination. Please reach out to Network Administrator',
                         12233: 'Error: Failure to accept a connection. Please reach out to Network Administrator',
                         12231: 'Error: No connection possible to destination. Please reach out to Network Administrator',
                         12230: 'Error: Severe Network error occurred in making this connection. Please reach out to Network Administrator',
                         12225: 'Error: Destination host unreachable. Please check your Network Connection or Reach out to Network Administator',
                         12224: 'Error: No Listener. Please check if listener service is running and compare the TNSNAMES.ORA entry with the appropriate LISTENER.ORA file',
                         12223: 'Error: Too many TNS connections open simultaneously. Please close few connections and re-try',
                         12170: 'Error: Connection has timed out',
                         12168: 'Error: Unable to contact LDAP Directory Server',
                         12157: 'Error: Internal error during network communication.'}

    def __init__(self, **connection_params: dict):
        '''
        Initialize the class to load the oracle client
        Arguments to this method is - **kwargs
        **Key word argument (has three params, user, password and the dsn)
        '''

        # use the 'orcl_client_path' path from configuration file
        # since the 64bit client is kept in that location
        cx_oracle.init_oracle_client(lib_dir=db_conf.ora_client_config['orcl_client_path'])
        # get the client version and assign it to initialization attribute
        self.client_version = cx_oracle.clientversion()
        # assign the user provided db_user to initialization method, for reuse across all methods
        self.db_user = connection_params.get('user')
        # assign the user provided db_password to initialization method, for reuse across all methods
        self.db_password = connection_params.get('password')
        # assign the user provided connection_dsn to initialization method, for reuse across all methods
        self.connection_dsn = connection_params.get('dsn')
        '''
        By default, connection pools are ‘homogeneous’, meaning that all connections use the same database credentials. 
        However, if the pool option homogeneous is False at the time of pool creation, then a ‘heterogeneous’ pool will 
        be created. This allows different credentials to be used each time a connection is acquired from the pool with 
        acquire(). This approach makes the class more flexible to be used with different instantiated objects
        '''
        self.pool = cx_oracle.SessionPool(dsn=self.connection_dsn, homogeneous=False)
        try:
            '''
            When a heterogeneous pool is created by setting homogeneous to False and no credentials are supplied during pool
            creation, then a user name and password may be passed to acquire():
            '''
            self.db_auto_connect = self.pool.acquire(user=self.db_user, password=self.db_password)
        # In Case Database Error occurs
        except cx_oracle.DatabaseError as _errors:
            # Capture the errors in a variable
            _error, = _errors.args
            # The corresponding error code is loaded in to _error.code
            # Check if the encountered error is defined in the error map
            # If its defined, print the custom message based on the mapped key and value
            if _error.code in CustomCxOracle._oracle_error_map.keys():
                print(CustomCxOracle._oracle_error_map[_error.code])
                # In case the code enters the except block
                # user will be provided with error brief and code will exit without execute any more statements
                sys.exit()