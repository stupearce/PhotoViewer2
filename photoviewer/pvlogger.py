import logging
import sys

def logInit():
    # Get rid of any loggers set up by other modules
    rootLogger = logging.getLogger()
    for handler in rootLogger.handlers:
        rootLogger.removeHandler(handler)

    handler = logging.FileHandler("app.log")
    handler.setFormatter(logging.Formatter("%(asctime)s %(levelname)s: %(name)s: %(message)s"))
    handler.setLevel(logging.DEBUG)
    rootLogger.addHandler(handler)

    handler = logging.StreamHandler(sys.stdout)
    handler.setFormatter(logging.Formatter("%(asctime)s %(levelname)s: %(name)s: %(message)s"))
    handler.setLevel(logging.DEBUG)
    rootLogger.addHandler(handler)

    rootLogger.setLevel(logging.DEBUG)
    
    log = logging.getLogger(__name__)
    log.setLevel(logging.DEBUG)

    log.info("PV logging Initialised")
    return log

