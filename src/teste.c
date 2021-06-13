#include<stdio.h>
int main(){
    int a;
    a = 2147483647;
    printf("%ld\n",sizeof(int));
    printf("%d\n",a);
    a++;
    printf("%d\n",a);
    return 0;
}