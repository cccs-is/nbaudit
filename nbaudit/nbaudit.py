from notebook.services.kernels.handlers import ZMQChannelsHandler
import json
import logging
import sys
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


def load_jupyter_server_extension__(nb_server_app):

    nb_server_app.log.info("nbaudit enabled!")

    web_app = nb_server_app.web_app
    base_url = web_app.settings['base_url']
    audit_logger = AuditLogger(parent=nb_server_app)

#    print('FROM AUDIT_LOGGER:', audit_logger.log_format)

    rules = web_app.default_router.rules
#    print('rules len:', len(rules))
    index1 = -1
    index2 = -1
    # locate the ZMQChannelsHandler
    for i, rule in enumerate(rules):
        for j, r in enumerate(rule.target.rules):
            if r.target.__name__  == 'ZMQChannelsHandler':
               index1 = i
               index2 = j
               break


    i = index1
    j = index2
#    print('index:', i, j)
#    print('>', rules[i].target.rules[j])
#    print('>>', rules[i].target.rules[j].target.__name__)
    if i >=0 and j>-0:
        # Create a logger for AuditLogger at INFO level.
        alogger = logging.getLogger('nbaudit-logger')
    
        handler = audit_logger.getHandler()
        formatter = logging.Formatter(audit_logger.log_format)
        handler.setFormatter(formatter)
        alogger.addHandler(handler)
        alogger.setLevel(audit_logger.log_level)
        rules[i].target.rules[j].target = ZMQChannelAuditHandler
#        print('>>>', rules[i].target.rules[j].target_kwargs)
        rules[i].target.rules[j].target_kwargs = {'audit_logger': alogger,}
     

    
