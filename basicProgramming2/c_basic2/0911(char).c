#include <stdio.h>

int main(void){
    char a = -5;
    unsigned char b = 251;
    a = a-5;
    b = b-5;
    printf("%x %x\n",a, b);
    //printf("%lu %lu\n",sizeof((unsigned char)a), sizeof(b));
    printf("%d %d\n",a, b);
    printf("%p %p\n",&a,&b);
    printf("%u %u\n",(unsigned char)a, b);
    printf("%d\n",sizeof('a'));
  
    return 0; 
}
