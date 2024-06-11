import pytest


# This class is used as a base for all test classes to inherit common fixtures or setup methods
@pytest.mark.usefixtures('setUp')
class BaseTest:

    pass
