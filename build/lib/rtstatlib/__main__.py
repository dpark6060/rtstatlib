# __main__.py
import logging
from .rtstat import sync_log

logging.basicConfig()
log = logging.getLogger('rtstat')

def main():

    sync_log()

if __name__ == "__main__":
    main()