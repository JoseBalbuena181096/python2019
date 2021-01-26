#include <18f4550.h> 
#device ADC =10
#include <stdint.h>
#include <stdlib.h>
#fuses HSPLL, NOWDT, NOPROTECT, NOLVP, NODEBUG, PLL2, CPUDIV1, VREGEN, NOMCLR INTRC_IO, USBDIV   
#use delay (clock=48M,crystal=4000000)   
#include<MLCD.c>
#use rs232(uart1,baud=115200,parity=N)//Frecuencia del reloj del pic 
#define encender output_high //DEFIINIMOS LAS SALIDAS EN 1 COMO ENCENDE 
#define apagar output_low //DEFINIMOS LAS SALIDAS EN  0 CONO APAGAR 
#define led1 PIN_D7
#define led2 PIN_D6
#define led3 PIN_C0
#define led4 PIN_C1
#define led5 PIN_C2

int b1=0;
int b2=0;
int b3=0;
int b4=0;
int b5=0;

uint16_t AU[3]={0};
float AF[3]={0.0};
char buffer[30];
void readAnalogs();

char ch_recv;
char recv[10];
char lcd_buffer_f[16];
char lcd_buffer_s[16];
int i=0;
int j=0;
int first = 0;
int second = 0;
#int_RDA
void RDA_isr(){
  ch_recv=getc(); //Captura el dato recibido del PIC 1
  if(first==1){
     recv[i] = ch_recv;
     i++;
  }
  else if(second==1){
     if(j<16)
         lcd_buffer_f[j] = ch_recv;
     else
         lcd_buffer_s[j-16] = ch_recv;
     j++;
  }
  if(ch_recv=='\t'){
     i=0;
     first = 1;
     second = 0;
  }
  else if(ch_recv=='\n'){
     j=0;
     first = 0;
     second = 1;
  }
}


void main (){
setup_adc_ports(AN0_TO_AN2);
setup_adc(ADC_CLOCK_INTERNAL);
 //HAbilita interrupcion por puerto serial
   for(int l=0;l<10;l++)
        recv[l] = '0';
   for(int k=0;k<16;k++){
        lcd_buffer_f[k] = ' ';
        lcd_buffer_s[k] = ' ';
   }
   disable_interrupts(GLOBAL);
   enable_interrupts(INT_RDA);
   enable_interrupts(GLOBAL);
   lcd_init();                         //Se inicializa la LCD
while(true){
   b1=input(pin_b0);
   b2=input(pin_b1);
   b3=input(pin_b2);
   b4=input(pin_b3);
   b5=input(pin_b4);
   readAnalogs();
   sprintf(buffer "\t%d,%d,%d,%d,%d,%.2f,%.2f,%.2f\n",b1,b2,b3,b4,b5,AF[0],AF[1],AF[2]);
   printf(buffer); 
   if(recv[0]=='1'){
      if(recv[1]=='1')
         encender(led1);
      else
         apagar(led1); 
      if(recv[2]=='1')
         encender(led2);
      else
         apagar(led2);
      if(recv[3]=='1')
         encender(led3);
      else
         apagar(led3);
      if(recv[4]=='1')
         encender(led4);
      else
         apagar(led4);
      if(recv[5]=='1')
         encender(led5);
      else
         apagar(led5);  
   }
   else{
      b1=input(pin_b0);
      if(input(pin_b0)==1)
         encender(led1);
      else
         apagar(led1);
      b2=input(pin_b1);
      if(input(pin_b1)==1)
         encender(led2);
      else
         apagar(led2);
      b3=input(pin_b2);
      if(input(pin_b2)==1)
         encender(led3);
      else
         apagar(led3);
      b4=input(pin_b3);
      if(input(pin_b3)==1)
         encender(led4);
      else
         apagar(led4);
      b5=input(pin_b4);
      if(input(pin_b4)==1)
         encender(led5);
      else
         apagar(led5);
      }
      lcd_gotoxy(1,1);   
      printf(lcd_putc,lcd_buffer_f);
      lcd_gotoxy(1,2);
      printf(lcd_putc,lcd_buffer_s);
  }
}

void readAnalogs(){
   set_adc_channel(0);
   delay_us(20);
   AU[0] = read_adc();   
   AF[0] = (5.0*AU[0])/1024.0;
   set_adc_channel(1);
   delay_us(20);
   AU[1] = read_adc();   
   AF[1] = (5.0*AU[1])/1024.0;
   set_adc_channel(2);
   delay_us(20);
   AU[2] = read_adc();   
   AF[2] = (5.0*AU[2])/1024.0;
}
