import contextlib
import io
import unittest

from learning_python.__main__ import main


class MainTests(unittest.TestCase):
    def test_main_prints_welcome_message(self) -> None:
        output = io.StringIO()
        with contextlib.redirect_stdout(output):
            main()

        self.assertEqual(output.getvalue(), "Welcome to your Python learning project!\n")


if __name__ == "__main__":
    unittest.main()
