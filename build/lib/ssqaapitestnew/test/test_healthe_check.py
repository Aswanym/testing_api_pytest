import pytest
import logging as logger


@pytest.mark.checkid1
def test_health():
    logger.debug("test passed!!")
