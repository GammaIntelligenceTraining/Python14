import re

text_to_search = r'''
abcdefghijklmnopqurtuvwxyz
ABCDEFGHIJKLMNOPQRSTUVWXYZ
1234567890
Ha HaHa HaHaHa
MetaCharacters (Need to be escaped):
. ^ $ * + ? { } [ ] \ | ( )
example.com
example.commander
321-555-4321
123.555.1234
123*555*1234
800-555-1234
900-555-1234
Mr. Jones
Mr Smith
Ms Davis
Mrs. Robinson
Mr. T
Mr Weqw_131312
abc
123-123-123123123
привет
wall ball mall hall tall
1111111111
4444444444
aaaaa44444
a41a4141a1
'''

sentence = 'Start a sentence and then bring it to an end'

emails = '''
SampleMaiL@example.com
john.sample@my-work.net
jack-125-production@colledge.gov.edu
bob.Samples@example.co.uk
example@example.org
exaple@exaple.co.co.co.col.asdasd.casda
'''

urls = '''
https://www.google.com
http://www.wordpress.org
https://www.nasa.gov
https://example.net
www.example.net
example.net
'''


pattern = re.compile(r'\d\d\d# I AM A COMMENT', re.VERBOSE)

matches = pattern.finditer(text_to_search)

for line in matches:
    print(line)