from .config import AuditLogger
from .auditHandler import ZMQChannelAuditHandler
import logging

def _jupyter_server_extension_paths():
    return [{
        "module": "nbaudit"
    }]


def load_jupyter_server_extension(nb_server_app):

    nb_server_app.log.info("nbaudit loaded!")

    web_app = nb_server_app.web_app
    base_url = web_app.settings['base_url']
    audit_logger = AuditLogger(parent=nb_server_app)

    rules = web_app.default_router.rules
    index1 = -1
    index2 = -1
    # locate the ZMQChannelsHandler
    for i, rule in enumerate(rules):
        for j, r in enumerate(rule.target.rules):
            if r.target.__name__  == 'ZMQChannelsHandler':
               index1 = i
               index2 = j
               break

    if index1 >=0 and index2>=0:
        # Create a logger for AuditLogger at INFO level.
        alogger = logging.getLogger('nbaudit-logger')
    
        handler = audit_logger.getHandler()
        formatter = logging.Formatter(audit_logger.log_format)
        handler.setFormatter(formatter)
        alogger.addHandler(handler)
        alogger.setLevel(audit_logger.log_level)

        rules[index1].target.rules[index2].target = ZMQChannelAuditHandler
        rules[index1].target.rules[index2].target_kwargs = {'audit_logger': alogger,}
        nb_server_app.log.info("nbaudit enabled!")
    else:
        nb_server_app.log.info("Failed to activate nbaudit server extension")
     

