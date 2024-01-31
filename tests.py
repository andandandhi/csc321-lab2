import unittest
from tasktwo import get_buf_pad

class TestTaskTwo(unittest.TestCase):
    def test_16pad_submit(self):
        bytes_in = ("userid=456;userdata=" + \
                    "12345678901" + \
                    ";session-id=31337").encode('utf-8')
        expected = [bytes("userid=456;userd", 'utf-8'),
                    bytes("ata=12345678901;", 'utf-8'),
                    bytes("session-id=31337", 'utf-8'),
                    bytes([16] * 16)]
        result = list(get_buf_pad(bytes_in))
        assert(expected == result)
            
    def test_15pad_submit(self):
        bytes_in = ("userid=456;userdata=" + \
                    "123456789012" + \
                    ";session-id=31337").encode('utf-8')
        expected = [bytes("userid=456;userd", 'utf-8'),
                    bytes("ata=123456789012", 'utf-8'),
                    bytes(";session-id=3133", 'utf-8'),
                    bytes([ord('7')] + ([15] * 15))]
        result = list(get_buf_pad(bytes_in))
        assert(expected == result)
    
if __name__ == '__main__':
    unittest.main()