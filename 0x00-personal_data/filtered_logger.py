"""
Function called filter_datum to return the log message
"""
#!/usr/bin/python3
import re


def filter_datum(fields, redaction, message, separator):
    """the actual function"""
    return re.sub(f'({"|".join(fields)})=[^{separator}]+',
            lambda m: f'{m.group().split("=")[0]}={redaction}', message)
