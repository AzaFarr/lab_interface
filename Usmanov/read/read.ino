void setup() {

  Serial.begin(115200);
  while (!Serial) {
    ;
  }
  Serial.println("Arduino ready for communication AAAAAA");
}

void loop() {
  if (Serial.available() > 0) {
    char receivedData = Serial.read();//StringUntil('\n') + " - REC";
    // receivedData.trim();


    //if (receivedData.length() > 0) 
    {
      Serial.println("рпвьор");
    }
  }
}