from log_manager import setup_logging, LoggingConfig
import pytest
 
def test_setup_logging_creates_loggers(tmp_path):
    # Temporary log configuration
    config = LoggingConfig(
        log_paths={
            'developer': tmp_path / 'developer.log',
            'business': tmp_path / 'business.log',
        },
        log_levels={
            'developer': 'DEBUG',
            'business': 'INFO',
        },
        display_logs={
            'developer': True,
            'business': False,
        }
    )
     
    loggers = setup_logging(config)
     
    assert 'developer' in loggers
    assert 'business' in loggers
    assert loggers['developer'].level == 10  # DEBUG corresponds to level 10
    assert loggers['business'].level == 20