#an example of the xunit-style setup in pytest, as well as test fixtures

import pytest

class TestClass:

    @classmethod
    def setup_class(cls):
        print("setup class")

    @classmethod
    def teardown_class(cls):
        print("teardown class")

    def setup_method(self, method):
        print("setup function")

    def teardown_method(self, method):
        print("teardown function")

    @pytest.fixture()
    def setup(self):
        print("\nSetup")
        yield
        print("\nTeardown!")

    def test_1(self, setup):
        assert True

    @pytest.mark.usefixtures("setup")
    def test_2(self):
        assert True
