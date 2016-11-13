  //lcd.print("C D E F G A B C");
 // lcd.setCursor(0, 1);

#define C4 0x30
#define Cs4 0x31
#define D4 0x32
#define E4 0x34
#define F4 0x35
#define G4 0x37
#define A4a 0x39
#define B4 0x3B



#define C5 0x3C
#define D5 0x3E
#define E5 0x40
#define F5 0x41
#define G5 0x43
#define A5a 0x45
#define As5 0x46
#define B5 0x47
#define C6 0x48
#define Cs6 0x49

//#define pin1 3
#define pin2 4
#define pin3 5
#define pin4 6
#define pin5 7
#define pin6 8
#define pin7 9
#define pin8 10

//#define mode 11

#define bg_delay 0
#define sm_delay 0
/*
#define RS A1
#define EN A0
#define LD4 A2
#define LD5 A3
#define LD6 A4
#define LD7 A5
*/

const int size_of_i = 6;
int i=0;
int note[size_of_i][8]= { {C5,D5,E5,F5,G5,A5a,B5,C6} , {C5,C5,G5,G5,A5a,A5a,G5,G5} , {F5,F5,E5,E5,D5,D5,C5,C5} , {C5,G5,C6,C5,As5,A5a,A5a,A5a} , {C5,G5,C6,C5,As5,A5a,G5,F5} , {C4,Cs4,D4,E4,C6,Cs6,C5,B5} }    ;
int status[8]={0,0,0,0,0,0,0,0};

#include <LiquidCrystal.h>

LiquidCrystal lcd(A1, A0, A2, A3, A4, A5);

void setup()
{
  //pinMode(pin1, INPUT_PULLUP);
  pinMode(pin2, INPUT_PULLUP);
  pinMode(pin3, INPUT_PULLUP);
  pinMode(pin4, INPUT_PULLUP);
  pinMode(pin5, INPUT_PULLUP);
  pinMode(pin6, INPUT_PULLUP);
  pinMode(pin7, INPUT_PULLUP);
  pinMode(pin8, INPUT_PULLUP);
 
 pinMode(11, INPUT_PULLUP);

  Serial.begin(9600);
  lcd.begin(16, 2);
}
//=====================================================================
void loop() 
{
  if (digitalRead(11) == LOW)                      //Interface LCD here!!
  {
    while(digitalRead(11) == LOW);
    
    lcd.print(i);
    ++i;
    if (i>=size_of_i) i=0;
    lcd.setCursor(0, 0);
   if (i==0) 
     {lcd.clear();
      lcd.print("C D E F G A B C");
     } 
   else if (i==1)
   { lcd.clear();
     lcd.print("TWINKLE 1");
   }
   else if (i==2)
   { lcd.clear();
     lcd.print("TWINKLE 2");
   }
   else if (i==3)
   { lcd.clear();
     lcd.print("Vodafone 1");
   }
   else if (i==4)
   { lcd.clear();
     lcd.print("Vodafone 2");
   }
   else if (i==5)
   { lcd.clear();
     lcd.print("Drum loop1");
   }
   
   
    
    }
/*/====================================================================
  if (digitalRead(pin1) == LOW) 
  {
    if (status[0]!=1)
      noteOn(0x90,note[i][0],0x55);
      status[0]=1;
      delay(bg_delay);
  }
  if (digitalRead(pin1)==HIGH && status[0]==1 )
  {  
      noteOn(0x80,note[i][0],0x00);
      delay(sm_delay);
      status[0]=0;
   }
*/
//---------------------------------------------------------------------   
  if (digitalRead(pin2) == LOW) 
  {
    if (status[1]!=1)
      noteOn(0x90,note[i][1],0x55);
      status[1]=1;
      delay(bg_delay);
  }
  if (digitalRead(pin2)==HIGH && status[1]==1 )
  {  
      noteOn(0x80,note[i][1],0x00);
      delay(sm_delay);
      status[1]=0;
   }
//---------------------------------------------------------------------    
  if (digitalRead(pin3) == LOW) 
  {
    if (status[2]!=1)
      noteOn(0x90,note[i][2],0x55);
      status[2]=1;
      delay(bg_delay);
  }
  if (digitalRead(pin3)==HIGH && status[2]==1 )
  {  
      noteOn(0x80,note[i][2],0x00);
      delay(sm_delay);
      status[2]=0;
   }

//---------------------------------------------------------------------    
  if (digitalRead(pin4) == LOW) 
  {
    if (status[3]!=1)
      noteOn(0x90,note[i][3],0x55);
      status[3]=1;
      delay(bg_delay);
  }
  if (digitalRead(pin4)==HIGH && status[3]==1 )
  {  
      noteOn(0x80,note[i][3],0x00);
      delay(sm_delay);
      status[3]=0;
   }
//---------------------------------------------------------------------  
  if (digitalRead(pin5) == LOW) 
  {
    if (status[4]!=1)
      noteOn(0x90,note[i][4],0x55);
      status[4]=1;
      delay(bg_delay);
  }
  if (digitalRead(pin5)==HIGH && status[4]==1 )
  {  
      noteOn(0x80,note[i][4],0x00);
      delay(sm_delay);
      status[4]=0;
   }
//---------------------------------------------------------------------  
  if (digitalRead(pin6) == LOW) 
  {
    if (status[5]!=1)
      noteOn(0x90,note[i][5],0x55);
      status[5]=1;
      delay(bg_delay);
  }
  if (digitalRead(pin6)==HIGH && status[5]==1 )
  {  
      noteOn(0x80,note[i][5],0x00);
      delay(sm_delay);
      status[5]=0;
   }
//---------------------------------------------------------------------  
  if (digitalRead(pin7) == LOW) 
  {
    if (status[6]!=1)
      noteOn(0x90,note[i][6],0x55);
      status[6]=1;
      delay(bg_delay);
  }
  if (digitalRead(pin7)==HIGH && status[6]==1 )
  {  
      noteOn(0x80,note[i][6],0x00);
      delay(sm_delay);
      status[6]=0;
   }
//---------------------------------------------------------------------  
  if (digitalRead(pin8) == LOW) 
  {
    if (status[7]!=1)
      noteOn(0x90,note[i][7],0x55);
      status[7]=1;
      delay(bg_delay);
  }
  if (digitalRead(pin8)==HIGH && status[7]==1 )
  {  
      noteOn(0x80,note[i][7],0x00);
      delay(sm_delay);
      status[7]=0;
   }
//=====================================================================  
     
}

void noteOn(int cmd, int pitch, int velocity) {
  Serial.write(cmd);
  Serial.write(pitch);
  Serial.write(0x55);
}
//_______________________________________________________________________

