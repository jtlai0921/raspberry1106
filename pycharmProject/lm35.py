from gpiozero import MCP3008
from time import sleep


while True:
    lm35 = MCP3008(channel=6)
    print(lm35.value)
    sleep(1)

