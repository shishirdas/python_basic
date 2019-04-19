

import os
if os.path.exists("shishir.txt"):
  os.remove("shishir.txt")
else:
  print("The file does not exist")