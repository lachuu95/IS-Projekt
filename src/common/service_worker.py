from PyQt5.QtCore import QThread
from ladon.server.wsgi import LadonWSGIApplication
from os.path import normpath, abspath, dirname, join
import wsgiref.simple_server
from ladon.tools.log import (
    set_loglevel,
    set_logfile,
    set_log_backup_count,
    set_log_maxsize,
)
import os
from src.common.constants import file_path_log


class ServiceWorker(QThread):
    def __init__(self, parent=None):
        super().__init__(parent)

    def run(self):
        os.makedirs(dirname(file_path_log()), exist_ok=True)
        set_logfile(file_path_log())
        set_loglevel(4)  # debug
        set_log_backup_count(50)
        set_log_maxsize(50000)

        scriptdir = dirname(abspath(__file__))
        service_modules = ["select_from_db"]
        import sys

        sys.path.append(scriptdir)

        # Create the WSGI Application
        application = LadonWSGIApplication(
            service_modules,
            [join(scriptdir, "services"), join(scriptdir, "appearance")],
            catalog_name="Serwer SOAP integracja systemów",
            catalog_desc="Serwer udostępniający dane zawarte w katalogu.",
            logging=31,
        )
        port = 58585
        server = wsgiref.simple_server.make_server("", port, application)
        server.serve_forever()
