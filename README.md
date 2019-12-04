# nbAudit

This project is server extension for Jupyter Notebook that provides auditing of cell execution (code). This is done by placing a hook onto the messages which are sent and received to the underlying Jupyter protocol.
The goal is to accurately reconstruct a user's interactive session by logging the inputs and outputs for each cell in a Jupyter notebook,

The generated logs are in JSON format. By default, they are logged to STDOUT, but can be configured to log to a file or to a Logstash server directly. 


## Install

### pip
    pip install git+https://github.com/cccs-is/nbaudit

### src
    pip install .

## To Verify the installation
    pip show nbaudit
    jupyter serverextension list

## To configure the logger
The logger can be configured by seeting params in the jupyter_notebook_config.py
for example:

    c.AuditLogger.log_format = '[%(asctime)s,%(msecs).03d] [%(levelname)s] [%(name)s]: %(message)s'
    c.AduitLogger.log_datefmt =  '%b %d %H:%M:%S'
    c.AuditLogger.log_level = 'INFO'
    
To send output to a syslog server, you can add the following lines, otherwise stdout is used.

    c.AuditLogger.log_handler =  'syslog'
    c.AdutiLogger.log_handler_address =  '<SYSLOG_SERVER>'
