from datetime import datetime
import time

since_the_begining = time.time()
print(f"Seconds since January1, 1970: {since_the_begining:,.4f} or {since_the_begining:.2e} in scientific notations")

now = datetime.now()
print(now.strftime("%b %d %Y"))
