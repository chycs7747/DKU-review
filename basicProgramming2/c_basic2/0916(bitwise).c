#include <stdio.h>

int main(void){
    char a = -2; // 0000 0010 -> 1111 1101 -> 1111 1110(2's complement)

    a = a>>1; // 1111 1110 -> 0111 1111 ..? , -2 * 1/2 = 127?

    printf("%d\n",a);
    return 0;
}