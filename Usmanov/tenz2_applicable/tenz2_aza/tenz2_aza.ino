#include <stdio.h> 
#include <stdlib.h> 

#define _LCD_TYPE 1
#include <LCD_1602_RUS_ALL.h>
//#include <LCD_I2C.h>

#include <DHT20.h>
#include <BMP180I2C.h>
#include "HX711.h"
#include "GyverEncoder.h"
#include <GyverStepper2.h>
#define GS_NO_ACCEL 
//СВЯЗЬ
#include <MemoryFree.h>
#include <EEPROM.h>


//ЭКРАН
LCD_1602_RUS lcd(0x27, 16, 2, 2); // Default address of most PCF8574 modules, change according
uint8_t dot[8] = {
    B00000,
    B00100,
    B01110,
    B11111,
    B11111,
    B01110,
    B00100,
    B00000,
};

//ДАТЧИК1
DHT20 DHT;
uint8_t count = 0;

//ДАТЧИК2
#define I2C_ADDRESS 0x77
//create an BMP180 object using the I2C interface
BMP180I2C bmp180(I2C_ADDRESS);

//ТЕНЗОДАТЧИК
HX711 scale;
uint8_t dataPin = 6;
uint8_t clockPin = 7;

//ЭНКОДЕР
#define S1 46
#define S2 48
#define KEY 44
Encoder enc1(S1, S2, KEY);

//ДВИГАТЕЛЬ
const int stepPin = 50;
const int dirPin = 52;
GStepper2<STEPPER2WIRE> stepper(6400, stepPin, dirPin);

int speed = 0, rate = 500, drvstatus = 0; //спид скорость, статус статус двигателя
int glob = 0, loc = 0, iter = 1, raz = 2, ret = 0; //глоб следит за навигацией между меню, лок внутри меню, раз нужен, чтобы экран менялся один раз а не гориллион 
//(0 значит, что можно моргнуть экраном при повороте энкодера, 2 значит, что при нажатии), рет значит брейк и возврат в 0
int autom = 0, manual = 0, sled = 0; //основной и ручной режим соответственно, след чтобы эта мразь не лупилась сука
    int i = 0, stage = 0, start = 0, dir = -1, rufkinsrs=0, t0 = 1, t = 0; //это всё для авторежима
double sgm = 0, countt = 0, P = 0, T = 0, wc = 0;
char sgchar="";
String sgstr0 = "", sgstr = "", sgread = "";
double sgfloat, sgmin=0, sgmax=0, sgsum = 0;
//int sg=0;

void setup()
{
  //СВЯЗЬ
  // Инициализация портов и выходов
  Serial.begin(115200);
  Serial3.begin(115200);

  //ЭКРАН
  lcd.init();
  //lcd.clear();
  lcd.backlight();
  lcd.createChar(6, dot);
  lcd.setCursor(12, 1);

  //DHT
  Wire.begin();
  DHT.begin();

  //BMP
  bmp180.begin();
  //reset sensor to default parameters.
	bmp180.resetToDefaults();
	//enable ultra high resolution mode for pressure measurements
	bmp180.setSamplingMode(BMP180MI::MODE_UHR);

  //ЭНКОДЕР
  enc1.setType(TYPE2);
  //Двигатель
  //stepper.setAcceleration(0); 
  stepper.setSpeedDeg(speed);        // в градусах/сек
  delay(1000);
  //ЧИТАЕМ ОДИН РАЗ
  DHT.read(); //bmp180.readPressure(); bmp180.readTemperature();
  wc = DHT.getHumidity();
  T = bmp180.readTemperature();
  P = bmp180.readPressure()/100000;
  // Serial.print(sgm); Serial.print("\t"); Serial.print(wc); Serial.print("\t"); 
  // Serial.print(T); Serial.print("\t"); Serial.println(P,5);

}

void loop()
{
  // enc1.tick(); //lcd.createChar(0, dot);
  // if (enc1.isHolded()){
  //     glob = 0; loc = 0; manual = 0; autom = 0; speed = 0; raz = 2;
  //     stepper.setSpeedDeg(0);
  // }
  
  // if (millis()/1000 - t>=t0){
  //   Serial.print(glob); Serial.print(";\t"); Serial.print(loc); Serial.print(";\t"); 
  //   Serial.print(raz); Serial.print(";\t"); Serial.print(autom); Serial.print(";\t"); Serial.println(iter);
  //   t = millis()/1000;
  // }
  //__________________________________________________________________________________________________________________
  
  //ЭНКОИНТЕРФЕЙС
  //СТАРТОВОЕ МЕНЮ______________________________
  if (glob==0){
    //ЭКРАН
    if (raz == 2 ){
      lcd.clear();
      lcd.setCursor(0, 0);
      lcd.print("Осн режим");
      lcd.setCursor(15, 0);
      lcd.write(6);

      lcd.setCursor(0, 1);
      lcd.print("Руч режим");

      raz = 3;
    }

    //ЭКРАН ИЗМЕНЕНИЯ
    if ((loc==0) && (raz==0)){
      lcd.setCursor(15, 1); lcd.print(" "); 
      lcd.setCursor(15, 0); lcd.write(6);
      raz = 1;
    }
    if ((loc==1) && (raz==0)){
      lcd.setCursor(15, 0); lcd.print(" "); 
      lcd.setCursor(15, 1); lcd.write(6);
      raz = 1;
    }
    //ЭНКОДЕР
    // if (enc1.isRight() && (loc!=1)){
    //   loc++; raz = 0;
    // }
    // if (enc1.isLeft() && (loc!=0)){
    //   loc--; raz = 0;
    // }
    
    Serial.print("Ввести loc (loc == 0 -> основной (авто) режим; loc == 1 -> ручной режим):" + "\n" + "loc = ")
    while (Serial.available()){
        loc_char = Serial.read();
        if (loc_char != '\n')
        {
          loc_str += loc_char;
        }
        if ((loc_char == '\n'))
        {
          loc = loc_str.toInt();
        }
      }

    // if (enc1.isPress()) {
    //   if (loc==0) glob = 1; //меню основного режима
    //   if (loc==1) glob = 2; //меню ручного режима
    //   raz = 2; loc = 0;
    // }

    if (loc==0) glob = 1; //меню основного режима
    if (loc==1) glob = 2; //меню ручного режима
    raz = 2; loc = 0;
  }
  //МЕНЮ ОСНОВНОГО РЕЖИМА______________________________
  if (glob == 1){
    //ЭКРАН
    if (raz == 2 ){
      lcd.clear();
      lcd.setCursor(1, 0);
      lcd.print("Число");
      lcd.setCursor(7, 0);
      lcd.write(6);

      lcd.setCursor(9, 0);
      lcd.print("Назад");
      lcd.setCursor(6, 1);           
      lcd.print("Нач");

      raz = 3;
    }

    //ЭКРАН ИЗМЕНЕНИЯ
    if ((loc==0) && (raz==0)){
      lcd.setCursor(7, 0); lcd.print(" "); 
      lcd.setCursor(15, 0); lcd.print(" "); 
      lcd.setCursor(11, 1); lcd.print(" "); 

      lcd.setCursor(7, 0); lcd.write(6);
      raz = 1;
    }
    if ((loc==1) && (raz==0)){
      lcd.setCursor(7, 0); lcd.print(" "); 
      lcd.setCursor(15, 0); lcd.print(" "); 
      lcd.setCursor(10, 1); lcd.print(" "); 

      lcd.setCursor(15, 0); lcd.write(6);
      raz = 1;
    }
    if ((loc==2) && (raz==0)){
      lcd.setCursor(7, 0); lcd.print(" "); 
      lcd.setCursor(15, 0); lcd.print(" "); 
      lcd.setCursor(10, 1); lcd.print(" "); 

      lcd.setCursor(10, 1); lcd.write(6);
      raz = 1;
    }
    //ЭНКОДЕР
    // if (enc1.isRight() && (loc!=2)){
    //   loc++; raz = 0;
    // }
    // if (enc1.isLeft() && (loc!=0)){
    //   loc--; raz = 0;
    }

    Serial.print("Ввести loc (loc == 0 -> выбор кол-ва погружений; loc == 1 -> возврат на стартовое меню; loc == 2 -> заспук эксперимента):" + "\n" + "loc = ")
    while (Serial.available()){
        loc_char = Serial.read();
        if (loc_char != '\n')
        {
          loc_str += loc_char;
        }
        if ((loc_char == '\n'))
        {
          loc = loc_str.toInt();
        }
      }

    // if (enc1.isPress()) {
    //   if (loc==0) glob = 3; //выбор количества погружений
    //   if (loc==1) glob = 0; //стартовое меню
    //   if (loc==2) {autom = 1; glob = -1; sled = 0;}//запуск эксперимента
    //   raz = 2; loc = 0;
      
    // }

    if (loc==0) glob = 3; //выбор количества погружений
    if (loc==1) glob = 0; //стартовое меню
    if (loc==2) {autom = 1; glob = -1; sled = 0;}//запуск эксперимента
    raz = 2; loc = 0;
      

  }
  //МЕНЮ РУЧНОГО РЕЖИМА______________________________
  if (glob == 2){
    //ЭКРАН
    if (raz == 2 ){
      lcd.clear();
      lcd.setCursor(0, 0);
      lcd.print("Начать");
      lcd.setCursor(7, 0);
      lcd.write(6);

      lcd.setCursor(9, 0);
      lcd.print("Назад");

      lcd.setCursor(3, 1);
      lcd.print("Гр/с :");
      lcd.setCursor(10, 1);
      lcd.print(String(speed));

      raz = 3;
    }

    //ЭКРАН ИЗМЕНЕНИЯ
    if ((loc==0) && (raz==0)){
      lcd.setCursor(7, 0); lcd.print(" "); 
      lcd.setCursor(15, 0); lcd.print(" "); 

      lcd.setCursor(7, 0); lcd.write(6);
      raz = 1;
    }
    if ((loc==1) && (raz==0)){
      lcd.setCursor(7, 0); lcd.print(" "); 
      lcd.setCursor(15, 0); lcd.print(" "); 

      lcd.setCursor(15, 0); lcd.write(6);
      raz = 1;
    }
    //ЭНКОДЕР
    // if (enc1.isRight() && (loc!=1)){
    //   loc++; raz = 0;
    // }
    // if (enc1.isLeft() && (loc!=0)){
    //   loc--; raz = 0;
    // }
    
    Serial.print("Ввести loc (loc == 0 -> перейти к ручному вводу скорости двигателя; loc == 1 -> возврат на стартовое меню):" + "\n" + "loc = ")
    while (Serial.available()){
        loc_char = Serial.read();
        if (loc_char != '\n')
        {
          loc_str += loc_char;
        }
        if ((loc_char == '\n'))
        {
          loc = loc_str.toInt();
        }
      }
    // if (enc1.isPress()) {
    //   if (loc==0) {manual = 1; glob = -1;} //ручной режим, -1 чтобы глоб временно ни на что не влиял
    //   if (loc==1) glob = 0; //стартовое меню
    //   raz = 2; loc = 0;
    // }
    if (loc==0) {manual = 1; glob = -1;} //ручной режим, -1 чтобы глоб временно ни на что не влиял
    if (loc==1) glob = 0; //стартовое меню
    raz = 2; loc = 0;
  }
  //РУЧНОЙ РЕЖИМ
  if (manual==1){
    //ЭКРАН
    if (raz == 2 ){
      lcd.clear();
      lcd.setCursor(3, 1);
      lcd.print("Гр/с : ");
      lcd.setCursor(10, 1);
      lcd.print(String(speed));

      raz = 3;
    }
    if (raz==0){
      lcd.setCursor(10, 1); lcd.print("        "); 
      lcd.setCursor(10, 1); lcd.print(String(speed)); 

      raz = 1;
    }
    //МОТОР И ЭНКОДЕР
    stepper.tick(); //enc1.tick();
    Serial.print("Ввести значение скорости:" + "\n" + "speed_value = ")
    while (Serial.available()){
        speed_value_char = Serial.read();
        if (speed_value_char != '\n')
        {
          speed_value_str += speed_value_char;
        }
        if ((speed_value_char == '\n'))
        {
          speed_value = speed_value_str.toInt();
          stepper.setSpeedDeg(speed);
        }
        if ((speed_value == -1))
        {
          raz = 0;
          manual = 0; glob = 2; raz = 2
        }

      }

      // stepper.setSpeedDeg(speed);
      // raz = 0;
      // manual = 0; glob = 2; raz = 2

  //   if (enc1.isRight()) {
  //     speed += 100;
  //     stepper.setSpeedDeg(speed);
  //     raz = 0;
  //     //Serial.println(speed);
  //   }
  //   if (enc1.isLeft()) {
  //     speed -= 100;
  //     stepper.setSpeedDeg(speed);
  //     raz = 0;
  //     //Serial.println(speed);
  //   }
  //   if (enc1.isPress()) {manual = 0; glob = 2; raz = 2;}
  // }
  //ВВОД КОЛИЧЕСТВА ПОГРУЖЕНИЙ______________________________
  if (glob == 3){
    //ЭКРАН
    if (raz == 2 ){
      lcd.clear();
      lcd.setCursor(0, 0);
      lcd.print("Число итераций:"); 
      lcd.setCursor(7, 1);
      lcd.print(String(iter));

      raz = 3;
    }

    //ЭКРАН ИЗМЕНЕНИЯ
    if (raz==0){
      lcd.setCursor(7, 1); lcd.print("  "); 
      lcd.setCursor(7, 1); lcd.print(String(iter)); 

      raz = 1;
    }
    //ЭНКОДЕР
    // if (enc1.isRight() && (iter!=99)){
    //   iter++; raz = 0;
    // }
    // if (enc1.isLeft() && (iter!=1)){
    //   iter--; raz = 0;
    // }
    Serial.print("Ввести количество итераций:" + "\n" + "iter = ")
    while (Serial.available()){
        iter_char = Serial.read();
        if (iter_char != '\n')
        {
          iter_str += iter_char;
        }
        if ((iter_char == '\n'))
        {
          iter = iter_str.toInt();
        }
      }
    // if (enc1.isPress()) {
    //   glob = 1;
    //   raz = 2; loc = 0;
    // }
    glob = 1;
    raz = 2; loc = 0;
  }

  //ОСНОВНОЙ РЕЖИМ
  if (autom==1){
    if (sled==0) {i = 0, stage = 0, start = 0, dir = -1, rufkinsrs=0, t0 = 1, t = 0; sgmax = 0; sgmin = 0; sgsum = 0;}
    if ((raz == 2) && (i!=iter)){
      lcd.clear();
      lcd.setCursor(5, 0);
      lcd.print("i = "); 
      lcd.setCursor(9, 0);
      lcd.print(String(i));
      raz = 3;
    }
    while ((i<iter)&&(autom==1)){
      stepper.tick(); 
      // enc1.tick();
      // if (enc1.isHolded()){
      //   glob = 0; loc = 0; manual = 0; autom = 0; speed = 0; raz = 2;
      //   stepper.setSpeedDeg(0);
      // }
      Serial.print("Для экстренной остановки и возврата на 0 нажать на 0")
      while (Serial.available()){
        stop_char = Serial.read();
        if (stop_char != '\n')
        {
          stop_str += stop_char;
        }
        if ((stop_char == '\n'))
        {
          stop = stop_str.toInt();
        }
      }

      if (stop == 0){
        glob = 0; loc = 0; manual = 0; autom = 0; speed = 0; raz = 2;
        stepper.setSpeedDeg(0);
      }

      //СВЯЗЬ
      while (Serial3.available())
      {
        sgchar = Serial3.read();
        if (sgchar != '\n')
        {
          sgstr += sgchar;
        }
        if ((sgchar == '\n'))// && (sgstr!=sgstr0))
        {
          sgfloat = sgstr.toDouble();
          sgread = sgstr;
          sgstr0 = sgstr;
          sgstr = "";
          // Serial.print(sgfloat); Serial.print(";\t"); Serial.print(sgmax); Serial.print(";\t"); Serial.println(sgmin);
        }
        if (sgfloat>sgmax) sgmax = sgfloat;
        if (sgfloat<sgmin) sgmin = sgfloat;
      }
      //ДЕБАГГИНГ
      if (millis()/1000 - t>=t0){
        Serial.print("t = "); Serial.print(t); Serial.print(";\t"); 
        Serial.print("i = "); Serial.print(i); Serial.print(";\t"); 
        Serial.print("stage = "); Serial.print(stage); Serial.print(";\t");
        Serial.print("start = "); Serial.print(start); Serial.print(";\t");
        Serial.print("dir = "); Serial.print(dir); Serial.print(";\t");
        Serial.print("sgfloat = "); Serial.print(sgfloat); Serial.print(";\t");
        Serial.print("sgmax = "); Serial.print(sgmax); Serial.print(";\t");
        Serial.print("sgmin = "); Serial.print(sgmin); Serial.print(";\t");
        Serial.print("sgsum = "); Serial.print(sgsum); Serial.println(";\t");
        t = millis()/1000;
      }
      //КОНТРОЛЬ МОТОРА
      if (stage==0){
        if (start==0) {stepper.setSpeedDeg(2*rate); start++;}
        if (sgmax/abs(sgmin)>=10) stage = 1;
      }
      if (stage==1){
        if (start==0) {stepper.setSpeedDeg(2*rate); start++;}
        if ( (sgfloat/sgmin<=0.6) && (abs(sgmin)>=abs(0.1*sgmax)) ) {stage = 2; start = 0; delay(5000);}
      }
      if (stage==2){
        if (start==0) {stepper.setSpeedDeg(-rate); start++;}
        if (sgfloat>=0.99*sgmax) {stage = 3; start = 0;}
      }
      if (stage==3){
        if (dir==-1){
          if (start==0) {stepper.setSpeedDeg(-rate); start++;}
          if (sgfloat<=0.95*sgmax){
            dir = 1; start = 0; i++;
            lcd.setCursor(9, 0); lcd.print(String(i));
            sgsum += sgmax;
          }
        }
        if ((dir==1) && (i<iter)){
          if (start==0) {stepper.setSpeedDeg(rate); start++;}
          if (sgfloat<=0.9*sgmax){
            dir = -1; start = 0; sgmax = 0; 
          }
        }
      }
    }
    if (i==iter){
      sled = 1;
      if (rufkinsrs==0) {rufkinsrs = 1; sgsum = sgsum/iter;}
      if (start==0) {stepper.setSpeedDeg(-2*rate); start = 1;}
      stepper.tick();
      //СВЯЗЬ
      if ((autom==1)&&(glob!=4))
      {
        sgchar = Serial3.read();
        if (sgchar != '\n')
        {
          sgstr += sgchar;
        }
        if ((sgchar == '\n'))// && (sgstr!=sgstr0))
        {
          sgfloat = sgstr.toDouble();
          // Serial.print("glob = "); Serial.print(glob); Serial.println(";\t");
          // Serial.print("autom = "); Serial.print(autom); Serial.println(";\t");
        }
      }
      if (abs(sgfloat)<=0.01*sgmax){
        stepper.setSpeedDeg(-1000);
        glob = 4; raz = 2; autom = 0;// i = 0;
      }
      //ДЕБАГГИНГ
      if (millis()/1000 - t>=t0){
        Serial.print("t = "); Serial.print(t); Serial.print(";\t"); 
        Serial.print("i = "); Serial.print(i); Serial.print(";\t"); 
        Serial.print("stage = "); Serial.print(stage); Serial.print(";\t");
        Serial.print("start = "); Serial.print(start); Serial.print(";\t");
        Serial.print("dir = "); Serial.print(dir); Serial.print(";\t");
        Serial.print("sgfloat = "); Serial.print(sgfloat); Serial.print(";\t");
        Serial.print("sgmax = "); Serial.print(sgmax); Serial.print(";\t");
        Serial.print("sgmin = "); Serial.print(sgmin); Serial.print(";\t");
        Serial.print("sgsum = "); Serial.print(sgsum); Serial.println(";\t");
        t = millis()/1000;
      }
    }
  }
  //МЕНЮ ВЫВОДА
  if (glob == 4){
    //Serial.println("TOOOTA");
    //ЭКРАН
    //ЧИТАЕМ
    DHT.read(); //bmp180.readPressure(); bmp180.readTemperature();
    //T = DHT.getTemperature();
    wc = DHT.getHumidity();
    T = bmp180.readTemperature();
    P = bmp180.readPressure()/100000;
    //ВЫВОДИМ
    if (raz == 2 ){
      lcd.clear();
      lcd.backlight();
      lcd.print("S=");
      lcd.setCursor(2, 0);
      lcd.print(String(sgsum));

      lcd.setCursor(8, 0);
      lcd.print("W=");
      lcd.setCursor(10, 0);
      lcd.print(String(wc));

      lcd.setCursor(0, 1);
      lcd.print("T=");
      lcd.setCursor(2, 1);
      lcd.print(String(T));

      lcd.setCursor(8, 1);
      lcd.print("P=");
      lcd.setCursor(10, 1);
      lcd.print(String(P));

      raz = 3;
    }
    // if (enc1.isPress()) {
    //   glob = 0;
    //   raz = 2; loc = 0;
    // }
    Serial.print("Эксперимент окончен. Для начала нового эксперимента нажать на 0 ")
    while (Serial.available()){
      restart_char = Serial.read();
      if (restart_char != '\n')
      {
        restart_str += restart_char;
      }
      if ((restart_char == '\n'))
      {
        restart = restart_str.toInt();
      }
    }
    if (restart == 0) {
      glob = 0;
      raz = 2; loc = 0;
    }
  }
  
  //СВЯЗЬ
  // while (Serial3.available())
  // {
  //   sgchar = Serial3.read();
  //   if (sgchar != '\n')
  //   {
  //     sgstr += sgchar;
  //   }
  //   if ((sgchar == '\n'))// && (sgstr!=sgstr0))
  //   {
  //     sgfloat = sgstr.toDouble();
  //     sgread = sgstr;
  //     sgstr0 = sgstr;
  //     sgstr = "";
  //     Serial.print(sgfloat); Serial.print(";\t"); Serial.print(sgmax); Serial.print(";\t"); Serial.println(sgmin);
  //   }
  //   if (sgfloat>sgmax) sgmax = sgfloat;
  //   if (sgfloat<sgmin) sgmin = sgfloat;
  // }
  //КОНЕЦ ВОТ ЗДЕСЬ
}

