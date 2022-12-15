# Open file
import pytest


@pytest.mark.parametrize("message", ["test", "main"])
def test_main(message):
    main(message)
