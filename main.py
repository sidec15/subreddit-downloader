__author__ = 'simone.decristofaro'

import getopt
import sys

# INIT LOG <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
import PARAMETER
import downloader
from logger_manager import *

PARAMETER_REDDIT_CLIENT_ID = "reddit_client_id"
PARAMETER_REDDIT_USERNAME = "reddit_username"
PARAMETER_REDDIT_SECRET = "reddit_secret"


def get_long_option(parameter_name):
    return '--{}'.format(parameter_name)


def get_option_declaration(parameter_name):
    return '{}='.format(parameter_name)


def check_existence_required_parameter(parameter_name, parameter_value):
    if parameter_value is None:
        print("No value specified for required parameter {}".format(parameter_name))
        print(__help())
        sys.exit(2)


def main(argv):
    parse_command_line(argv)
    downloader.download()



def parse_command_line(argv):
    # Parse command line parameters
    try:
        opts, args = getopt.getopt(argv, "ht:f:c:", [
            "help"
            , get_option_declaration(PARAMETER_REDDIT_USERNAME)
            , get_option_declaration(PARAMETER_REDDIT_CLIENT_ID)
            , get_option_declaration(PARAMETER_REDDIT_SECRET)
        ])
    except getopt.GetoptError:
        log.exception("ERROR parsing command line arguments")
        sys.exit(2)
    for opt, arg in opts:
        if opt in ("-h", "--help"):
            print(__help())
            sys.exit()
        elif opt == get_long_option(PARAMETER_REDDIT_USERNAME):
            PARAMETER.REDDIT_USERNAME = arg
        elif opt == get_long_option(PARAMETER_REDDIT_CLIENT_ID):
            PARAMETER.REDDIT_CLIENT_ID = arg
        elif opt == get_long_option(PARAMETER_REDDIT_SECRET):
            PARAMETER.REDDIT_SECRET = arg

    # check type value
    check_existence_required_parameter(PARAMETER_REDDIT_USERNAME, PARAMETER.REDDIT_USERNAME)
    check_existence_required_parameter(PARAMETER_REDDIT_CLIENT_ID, PARAMETER.REDDIT_CLIENT_ID)
    check_existence_required_parameter(PARAMETER_REDDIT_SECRET, PARAMETER.REDDIT_SECRET)

    # global appType
    # appType = OUTPUT.getOutPutTypeByName(PARAMETER.TYPE)


def __help():
    """
    :rtype: str
    """
    return os.linesep.join([
        os.linesep
        , "----------- configuration -----------: "
        , "-h, --help:               usage"
        , get_long_option(PARAMETER_REDDIT_USERNAME) + ":          [REQUIRED] reddit username."
        , get_long_option(PARAMETER_REDDIT_CLIENT_ID) + ":          [REQUIRED] reddit client id."
        , get_long_option(PARAMETER_REDDIT_SECRET) + ":          [REQUIRED] reddit secret."
        , os.linesep
    ])


if __name__ == '__main__':
    main(sys.argv[1:])
