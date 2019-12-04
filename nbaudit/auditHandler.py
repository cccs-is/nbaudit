from notebook.services.kernels.handlers import ZMQChannelsHandler
import socket
import getpass
import json
import logging
from .auditLogger import AuditLogger

class ZMQChannelAuditHandler(ZMQChannelsHandler):

    def initialize(self, audit_logger=None):
        super(ZMQChannelAuditHandler, self).initialize()

        self.audit_logger = audit_logger
        self.user = getpass.getuser()
        self.hostname = socket.getfqdn()

        self.log.info("Loading AuditLogger logging extension.")


    def log_msg(self, msg):
        json_msg = json.loads(msg)
        # on jupyterhub username is just "username", so we'll use the one from getpass
        # json_msg['user'] = self.session.username
        json_msg['user'] = self.user
        json_msg['hostname'] = self.hostname
        if self.audit_logger != None:
          self.audit_logger.log.info(json.dumps(json_msg))

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

