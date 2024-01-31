import unittest
from tasktwo import get_buf_pad, submit, cbc_decrypt, hack

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
    
    def test_hack(self):
        assert(hack())

    def not_a_test(self):
        """This is only here to run the program with user input, don't run this test.
        Call this function if you want to see the your decrypted submit() message.
        """
        encrypted_message = submit()
        print(cbc_decrypt(encrypted_message))
        assert(True)

if __name__ == '__main__':
    unittest.main()