from unittest import mock

import pytest

from main import log_info


class TestLogMessage:
    @pytest.mark.parametrize("message", ["info", "error"])
    @mock.patch("main.logger")
    def test_log_message(self, mock_logger, message):
        mock_logger.info.return_value = message

        assert log_info(message)
        assert mock_logger.info.called
