"""
    Python Real-World Projects
    Project Zero: A template for other projects
"""

import argparse
import sys
import logging

def setup_global_logging():
    logging.basicConfig(
        level=logging.DEBUG,
        format='%(asctime)s [%(levelname)s] %(name)s: %(message)s',
        handlers=[
            logging.StreamHandler(), 
            logging.FileHandler("app.log", mode='a') 
        ]
    )


def get_options(argv: list[str]) -> argparse.Namespace:
    """Parse command-line"""
    parser = argparse.ArgumentParser()
    parser.add_argument("--who", "-w", type=str, default="World",
        help='who = name provided in the cli')
    return parser.parse_args(argv)

def greeting(who: str = "World") -> None:
    """Write greeting."""
    if who == '':
        print(f"Is necessary to provide a value for {who}!")
    else:
        print(f"Hello, {who}!")
    

def main(argv: list[str] = sys.argv[1:]) -> None:
    """Get options and write greeting."""
    options = get_options(argv)
    greeting(options.who)

if __name__ == "__main__":
    setup_global_logging()
    logger = logging.getLogger(__name__)
    logger.info('Application started')
    main()
    logger.info('Apllication finished')
