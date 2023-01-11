/*
โปรแกรมนี้จะคำนวณว่า จากรายได้ต่อปีของบุคคลนั้น จะต้องจ่ายภาษีเป็นจำนวนเท่าใด (ให้แสดงเป็นทศนิยม 2 ตำแหน่ง)
โดยการเก็บภาษีจะเป็นแบบขั้นบันได กล่าวคือ 300,000 บาทแรกจะต้องจ่าย 5% และ 300,000.01 บาทขึ้นไปจะจ่าย 10%

เช่น ถ้ารายได้ต่อปีเป็น 100,000 บาท จะจ่ายภาษี 5% เท่ากับ 5,000 บาท

แต่ถ้ารายได้ต่อปีเป็น 500,000 บาทแล้ว การจ่ายภาษีจะคำนวณดังนี้
300,000 บาทแรกจะจ่าย 5% เท่ากับ 15,000 บาท และที่เหลือ 200,000 บาทจะจ่าย 10% 
เท่ากับ 20,000 บาท ดังนั้น เสียภาษีรวมเป็นเงิน (15,000+20,000=35,000 บาท)

นอกจากนั้น ถ้ารายได้เป็นค่าลบ 
ให้แสดงข้อความเตือน Error: Salary must be greater or equal to 0
*/
#include <stdio.h>
#include <stdlib.h>
int main (){
    // input
    char number[100];
    fgets(number, 100 ,stdin);
    float tax,inumber = atof(number);
    //process
    if (inumber >= 0){
        if (inumber > 300000.0){
            tax = ((inumber-300000.0)*0.1) + (300000.0*0.05);
            printf("%.2f",tax);
        }else{
            tax = inumber*0.05;
            printf("%.2f",tax);
        }
    }else{
        printf("Error: Salary must be greater or equal to 0");
    }
}