cw = '''
Description:
Write an algorithm that will identify valid IPv4 addresses in dot-decimal format. IPs should be considered valid if they consist of four octets, with values between 0 and 255, inclusive.

Valid inputs examples:
Examples of valid inputs:
1.2.3.4
123.45.67.89
Invalid input examples:
1.2.3
1.2.3.4.5
123.456.78.90
123.045.067.089
Notes:
Leading zeros (e.g. 01.02.03.04) are considered invalid
Inputs are guaranteed to be a single string
'''

def is_valid_IP(strng):
    ip_list = strng.split('.')
    if len(ip_list) != 4 or not all(octet.isdigit() for octet in ip_list):
        return False
    for octet in ip_list:
        if octet.startswith('0') and octet != '0':
            return False
        if not (0 <= int(octet) <= 255):
            return False
    return True


# print(is_valid_IP('1.2.3.4'))
# print(is_valid_IP('123.45.67.89'))
# print(is_valid_IP('123.456.78.90'))
# print(is_valid_IP('abc.def.gh.i'))
# print(is_valid_IP('1.2.3.4.5'))