import time
from machine import Pin

# Definer relé og knapp
relay = Pin(14, Pin.OUT)
button = Pin(15, Pin.IN, Pin.PULL_UP)

# Funksjon for å endre reléets tilstand
def reverseRelay():
    if relay.value():
        relay.value(0)
    else:
        relay.value(1)

# Hovedløkke
while True:
    if not button.value():  # Sjekker om knappen trykkes
        time.sleep_ms(20)  # Debouncing
        if not button.value():  # Bekrefter at knappen fremdeles trykkes
            reverseRelay()  # Bytter reléets tilstand
            while not button.value():  # Venter til knappen slippes
                time.sleep_ms(20)
