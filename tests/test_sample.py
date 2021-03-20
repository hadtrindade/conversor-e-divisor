import pytest
from conversor_divisor.app import MainWindow
from conversor_divisor import __version__


@pytest.fixture(scope="module")
def app():
    widget = MainWindow()
    return widget


def test_version(app, qtbot):
    assert app.label_version.text() == __version__
