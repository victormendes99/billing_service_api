import logging


def setup_logging(logger_name: str = "logger") -> None:
    DEFAULT_FORMAT: str = (
        "[%(asctime)2s] %(levelname)-2s -  "
        + "%(message)s (%(filename)s: %(funcName)s)"
    )

    # Custom formatter
    class MyFormatter(logging.Formatter):

        err_fmt = DEFAULT_FORMAT
        dbg_fmt = DEFAULT_FORMAT
        info_fmt = DEFAULT_FORMAT

        def __init__(self):
            super().__init__(fmt=DEFAULT_FORMAT, datefmt=None, style="%")

        def format(self, record):

            # Save the original format configured by the user
            # when the logger formatter was instantiated
            format_orig = self._style._fmt

            # Replace the original format with one customized by logging level
            if record.levelno == logging.DEBUG:
                self._style._fmt = MyFormatter.dbg_fmt
                self._style._fmt = MyFormatter.dbg_fmt

            elif record.levelno == logging.INFO:
                self._style._fmt = MyFormatter.info_fmt

            elif record.levelno == logging.ERROR:
                self._style._fmt = MyFormatter.err_fmt

            # Call the original formatter class to do the grunt work
            result = logging.Formatter.format(self, record)

            # Restore the original format configured by the user
            self._style._fmt = format_orig

            return result

    log = logging.getLogger(logger_name)
    log.setLevel(logging.INFO)
    fmt = MyFormatter()
    hdlr = logging.StreamHandler()
    hdlr.setFormatter(fmt)
    log.addHandler(hdlr)

    return log
