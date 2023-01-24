from datetime import datetime



str = "16;04:40"

print(datetime.strptime(str, "%H:%M:%S"))
