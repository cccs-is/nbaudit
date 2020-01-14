from traitlets import Bool, Unicode, Dict, List, Union, default, validate
from traitlets.config import Configurable
import json
import sys
import logging

class AuditLogger(Configurable):

  def __init__(self):
    self.setupDone = False

  # This is just an example trait
  # log_config = Dict(
  #       {},
  #       help="""
  #       """,
  #       config=True
  #   )

  disable_existing_loggers = Bool(default_value=False, allow_none=True, config=True, 
      help=""" ... """
  )
  log_format = Unicode(default_value='[%(asctime)s,%(msecs).03d] [%(levelname)s] [%(name)s] %(message)s', allow_none=True, config=True,
      help=""" ... """
  )
  log_datefmt = Unicode(default_value='%b %d %H:%M:%S', allow_none=True, config=True)
  log_handler = Unicode(default_value=None, allow_none=True, config=True,
      help=""" ... """ 
  )
  log_handler_address =  Unicode(default_avlaue='localhost', allow_none=True, config=True,
      help=""" ... """
  )
  log_handler_facility = Unicode(default_value=None, allow_none=True, config=True,
      help=""" ... """
  )
  log_level = Unicode(default_value='INFO', allow_none=True, config=True,
      help=""" ... """
  )


  def setup(self):
    if not self.setupDone:
      # Create a logger for AuditLogger at INFO level.
      self.logger = logging.getLogger('AuditLogger')
      self.logger.propagate = False
      handler = self.getHandler()
      formatter = logging.Formatter(self.log_format)
      handler.setFormatter(formatter)
      self.logger.addHandler(handler)
      self.logger.setLevel(self.log_level)


  def getHandler(self):
    if self.log_handler  == 'syslog':
      address = (self.log_handler_address, logging.handlers.SYSLOG_UDP_PORT)
      return logging.handlers.SysLogHandler(address= address,
                      facility= logging.handlers.SysLogHandler.LOG_LOCAL7) 
    else: # just return a standard console log
      return logging.StreamHandler(stream=sys.stdout)

  @property
  def log(self):
    return self.logger


