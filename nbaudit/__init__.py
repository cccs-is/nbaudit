#from .nbaudit import load_jupyter_server_extension

def _jupyter_server_extension_paths():
    return [{
        "module": "nbaudit"
    }]

def load_jupyter_server_extension(nb_server_app):

    nb_server_app.log.info("nbaudit enabled!")


