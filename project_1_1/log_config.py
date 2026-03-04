import logging.config
import tomllib


def setup_logging(config_path='logging_config.toml'):
    try:
        with open(config_path,'rb') as f:
            config = tomllib.load(f)
        logging.config.dictConfig(config)
        print(f"Logging configured from {config_path}")
    except FileNotFoundError:
        print(f"Error: Configuration file'{config_path}' not found.")
    except Exception as e:
        print(f"Error loading configuration: {e}")

logger = logging.getLogger(__name__)