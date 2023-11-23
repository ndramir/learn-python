from regex_main import *
import re


assert re.search(my_re, '255.0.190.35') == True
assert re.search(my_re, '122.35.48.1') == True
assert re.search(my_re, '256.4.4.4') == False
assert re.search(my_re, '.0.3.5.8') == False
assert re.search(my_re, '0.2.3.1.') == False
assert re.search(my_re, 'as1.2.3.4') == False
assert re.search(my_re, '26.123.45.69lk') == False
