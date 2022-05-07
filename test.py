import whatsoup
from datetime import datetime

tests = []
tests.append('2/15/2021 2:35')
tests.append('9/18/2019 16:11')

fmt = '%m/%d/%Y %H:%M'

for test in tests:
    print("test data: ", test, whatsoup.parse_datetime(test), datetime.strptime(test, fmt))
