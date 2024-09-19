import time

from rich.progress import track

for i in track(range(100), description="Processing..."):
    time.sleep(0.5)