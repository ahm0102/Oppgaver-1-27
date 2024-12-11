PIN_BUZZER 15
PIN_BUTTON 16

void setup() {
    pinMode(PIN_BUZZER, OUTPUT);
    pinMode(PIN_BUTTON, INPUT);
    digitalWrite(PIN_BUZZER, LOW);
}

void loop() {
    if (digitalRead(PIN_BUTTON) == LOW) {
        digitalWrite(PIN_BUZZER, HIGH);
    } else {
        digitalWrite(PIN_BUZZER, LOW);
    }
}
