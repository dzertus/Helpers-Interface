import requests

import requests
#url = "https://www.w3.org/WAI/ER/tests/xhtml/testfiles/resources/pdf/dummy.pdf"
r = requests.get(url)
with open("dummy.pdf", 'wb') as f:
    f.write(r.content)
