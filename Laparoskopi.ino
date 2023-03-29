int SensorValue1, SensorValue2;

void setup() {
  // put your setup code here, to run once:

  Serial.begin(9600);

}

void loop() {
  // put your main code here, to run repeatedly:

  SensorValue1 = analogRead(0); // 0 or 5, 0 for sensor on the left.
  SensorValue2 = analogRead(1);
  Serial.print(SensorValue1);
  Serial.print(':');
  Serial.println(SensorValue2);
  delay(100);
}