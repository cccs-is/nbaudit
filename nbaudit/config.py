from traitlets import Bool, Unicode, Dict, List, Union, default, validate
from traitlets.config import Configurable
import sys
import logging

class AuditLogger(Configurable):

  # This is just an example trait
  log_config = Dict(
        {},
        help="""
        """,
        config=True
    )

  disable_existing_loggers = Bool(default_value=False, allow_none=True, config=True, 
      help=""" ... """
  )
  log_format = Unicode(default_value='%(asctime)s AUDIT: %(message)s', allow_none=True, config=True,
      help=""" ... """
  )
  log_datefmt = Unicode(default_value='%b %d %H:%M:%S', allow_none=True, config=True)
  log_handler = Unicode(default_value=None, allow_none=True, config=True,
      help=""" ... """ 
  )
  log_handler_address =  Unicode(default_avlaue='/var/log', allow_none=True, config=True,
      help=""" ... """
  )
  log_handler_facility = Unicode(default_value=None, allow_none=True, config=True,
      help=""" ... """
  )
  log_level = Unicode(default_value='INFO', allow_none=True, config=True,
      help=""" ... """
  )

  def getHandler(self):
    if self.log_handler  == 'syslog':
      address = self.log_handler_address
      return logging.handlers.SysLogHandler(address= address,
                      facility= logging.handlers.SysLogHandler.LOG_LOCAL7) 
    else: # just return a standard console log
      return logging.StreamHandler(stream=sys.stdout)
