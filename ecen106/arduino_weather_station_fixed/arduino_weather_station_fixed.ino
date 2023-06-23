#include <SimpleDHT.h>
#include <LiquidCrystal_I2C.h>

LiquidCrystal_I2C lcd(0x27, 16, 2);

#define DHT11_PIN 3

SimpleDHT11 dht11(DHT11_PIN);

void setup(){
  lcd.init();
  lcd.backlight();
}

void loop(){
  byte temperature = 0;
  byte humidity = 0;
  int chk = dht11.read(&temperature, &humidity, NULL);
  lcd.setCursor(0,0); 
  lcd.print("Temp: ");
  lcd.print(temperature);
  lcd.print((char)223);
  lcd.print("C");
  lcd.setCursor(0,1);
  lcd.print("Humidity: ");
  lcd.print(humidity);
  lcd.print("%");
  delay(1000);
}