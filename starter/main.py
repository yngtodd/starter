import traceback
import logging
import argparse
import os

from starter.fancy_log.colorized_log import ColorizedLog
from starter.timing_tools.timeit import timeit
from starter.configuration.configuration import Configuration

logger = ColorizedLog(logging.getLogger('Main'), 'yellow')


def setup_log(log_path: str = '../logs/default.log', debug: bool = False) -> None:
    """Set the parameters of the logger

    Args:
        log_path (str): The path the log file is going to be saved
        debug (bool): Whether to print debug messages or not
    """
    log_path = log_path.split(os.sep)
    if len(log_path) > 1:

        try:
            os.makedirs((os.sep.join(log_path[:-1])))
        except FileExistsError:
            pass
    log_filename = os.sep.join(log_path)
    # noinspection PyArgumentList
    logging.basicConfig(level=logging.INFO if debug is not True else logging.DEBUG,
                        format='%(asctime)s %(name)-12s %(levelname)-8s %(message)s',
                        datefmt='%Y-%m-%d %H:%M:%S',
                        handlers=[
                            logging.FileHandler(log_filename),
                            # logging.handlers.TimedRotatingFileHandler(log_filename, when='midnight', interval=1),
                            logging.StreamHandler()
                        ]
                        )


@timeit()
def argparser() -> argparse.Namespace:
    """Setup the argument parser

    Returns:
        argparse.Namespace:
    """
    parser = argparse.ArgumentParser(
        description='A template for python projects.',
        add_help=False)
    # Required Args
    required_args = parser.add_argument_group('Required Arguments')
    config_file_params = {
        'type': argparse.FileType('r'),
        'required': True,
        'help': "The configuration yml file"
    }
    required_args.add_argument('-c', '--config-file', **config_file_params)
    # Optional args
    optional_args = parser.add_argument_group('Optional Arguments')
    optional_args.add_argument('-m', '--run-mode', choices=['run_mode_1', 'run_mode_2', 'run_mode_3'],
                               default='run_mode_1',
                               help='Description of the run modes')
    optional_args.add_argument('-l', '--log',
                               default='logs/default.log',
                               help="Name of the output log file")
    optional_args.add_argument('-d', '--debug', action='store_true',
                               help='Enables the debug log messages')
    optional_args.add_argument("-h", "--help", action="help", help="Show this help message and exit")

    return parser.parse_args()


@timeit(custom_print="{func_name} took {duration:2.5f} to run!")
def main():
    """This is the main function of starter.py

    Example: python starter/main.py -m run_mode_1

        -c confs/template_conf.yml -l logs/output.log
    """

    # Initializing
    args = argparser()
    setup_log(args.log, args.debug)
    # Load the configuration
    # configuration = Configuration(config_src=args.config_file,
    #                               config_schema_path='yml_schema_strict.json')
    configuration = Configuration(config_src=args.config_file)
    # Prints
    logger.info("Started with args: %s" % args)
    logger.info("Loaded Config file: %s", configuration.to_json())
    logger.info("Starting in run mode: {0}".format(args.run_mode))
    # Example timeit code block
    custom_print = "Iterating in a 10,000-number-range took {duration:2.5f} seconds."
    with timeit(custom_print=custom_print):
        for _ in range(10000):
            pass


if __name__ == '__main__':
    try:
        main()
    except Exception as e:
        logging.error(str(e) + '\n' + str(traceback.format_exc()))
        raise e
