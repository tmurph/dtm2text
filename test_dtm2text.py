import pytest

import dtm2text


@pytest.mark.parametrize("binary_data, text_data", [
    (b'\x00\x00\x00\x00\x80\x80\x80\x80',
     "0:0:0:0:0:0:0:0:0:0:0:0:0:0:128:128:128:128"),
    (b'\x01\x00\x00\x00\x80\x80\x80\x80',
     "1:0:0:0:0:0:0:0:0:0:0:0:0:0:128:128:128:128"),
    (b'\x02\x00\x00\x00\x80\x80\x80\x80',
     "0:1:0:0:0:0:0:0:0:0:0:0:0:0:128:128:128:128"),
    (b'\x00\x00\x00\x00\xff\x80\x80\x80',
     "0:0:0:0:0:0:0:0:0:0:0:0:0:0:255:128:128:128"),
    (b'\x02\x00\x00\x00\xff\x80\x80\x80',
     "0:1:0:0:0:0:0:0:0:0:0:0:0:0:255:128:128:128"),
])
def test_text_input_from_bytes(binary_data, text_data):
    "Can we parse input data to text?"
    text_input = dtm2text.text_input_from_bytes(binary_data)
    assert text_data == text_input


@pytest.mark.parametrize("text_data, binary_data", [
    ("0:0:0:0:0:0:0:0:0:0:0:0:0:0:128:128:128:128",
     b'\x00\x00\x00\x00\x80\x80\x80\x80'),
    ("1:0:0:0:0:0:0:0:0:0:0:0:0:0:128:128:128:128",
     b'\x01\x00\x00\x00\x80\x80\x80\x80'),
    ("0:1:0:0:0:0:0:0:0:0:0:0:0:0:128:128:128:128",
     b'\x02\x00\x00\x00\x80\x80\x80\x80'),
    ("0:0:0:0:0:0:0:0:0:0:0:0:0:0:255:128:128:128",
     b'\x00\x00\x00\x00\xff\x80\x80\x80'),
    ("0:1:0:0:0:0:0:0:0:0:0:0:0:0:255:128:128:128",
     b'\x02\x00\x00\x00\xff\x80\x80\x80'),
    ("\n", b''),
    ("# a comment", b''),
])
def test_byte_input_from_text(text_data, binary_data):
    "Can we parse input data to bytes?"
    byte_input = dtm2text.byte_input_from_text(text_data)
    assert binary_data == byte_input
