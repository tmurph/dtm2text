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
def test_text_frame_from_bytes(binary_data, text_data):
    "Can we parse frame data to text?"
    text_frame = dtm2text.text_frame_from_bytes(binary_data)
    assert text_data == text_frame
