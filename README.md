# nbAudit

This project is a server extension for Jupyter Notebook that provides auditing of cell execution (code). This is done by replacing the ZMQChannelsHandler with a derived class which capture the messages that are sent and received during notebook interaction with the server. The code is inspired by the idea used [ganymede_nbextension](https://github.com/Lab41/ganymede_nbextension) but was written to support the latest notebook code base (notebook==6.0.0)
There is also a similar project [audited-notebook](https://github.com/gclen/audited-notebook) that modifies the logging of ZMQChannelsHandler on_message() and require compiling the notebook code.

_The goal is to accurately reconstruct a user's interactive session by logging the code executed by the user in a Jupyter notebook_

The generated logs are in JSON format. By default, they are logged to STDOUT, but can be configured to log to a Logstash server directly. 


## Install

### pip
    pip install git+https://github.com/cccs-is/nbaudit

### src
    pip install .

## To Verify the installation
    pip show nbaudit
    jupyter serverextension list

## To configure the logger
The logger can be configured by setting params in the jupyter_notebook_config.py
for example:

    c.AuditLogger.log_format = '[%(asctime)s,%(msecs).03d] [%(levelname)s] [%(name)s]: %(message)s'
    c.AduitLogger.log_datefmt =  '%b %d %H:%M:%S'
    c.AuditLogger.log_level = 'INFO'
    
To send output to a syslog server, you can add the following lines, otherwise stdout is used.

    c.AuditLogger.log_handler =  'syslog'
    c.AdutiLogger.log_handler_address =  '<SYSLOG_SERVER>'
