#include <stdio.h>

int main(void){
    int sum = 0;
    int n = 10;
    for(int sum=0,i=1;i<=n;++i){ //case 1
        printf("%d\n", sum); 
        sum += i;
    }
    for(int sum=0, i=1;i<=n;sum += i, ++i) //case 2
        printf("%d\n", sum);
   
    for(int sum=0, i=1;i<=n;++i, sum += i) //case 3
        printf("%d\n", sum);

    return 0; //case1 == case2 != case3
}