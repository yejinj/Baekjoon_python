#include <stdio.h>
int main()
{
    int a, b;
    scanf("%d %d", &a, &b);
    
    if (b < 45) {
    	if (a == 0) {
    		a = 23;
    		b += 60;
		}
		else {
			a -= 1;
			b += 60;
		}
	}
	
	printf("%d %d", a, b - 45);
    
    return 0;
}