from notebook.services.kernels.handlers import ZMQChannelsHandler
import json
import logging
from .config import AuditLogger

class ZMQChannelAuditHandler(ZMQChannelsHandler):

    def initialize(self, audit_logger=None):
        super(ZMQChannelAuditHandler, self).initialize()
        self.audit_logger = audit_logger
        self.log.info("Loading AuditLogger logging extension.")

    def log_msg(self, msg):
        json_msg = json.loads(msg)
        json_msg['user'] = self.session.username
        self.audit_logger.info(json.dumps(json_msg))

    """
    Log a message sent from the Jupyter client. 
    This function, on_message, only triggers on one direction of communication (i.e. sending)
    """
    
    def on_message(self, msg):
       #print(">> Sending message: %s" % msg)
       # Call ZMQChannelAuditHandlercustom logging function.
       self.log_msg(msg)
       super(ZMQChannelAuditHandler, self).on_message(msg)


    def _handle_kernel_info_reply(self, msg):
      # self.log.info("AuditMsg2: {}".format(msg))
      super(ZMQChannelAuditHandler, self)._handle_kernel_info_reply(msg)

