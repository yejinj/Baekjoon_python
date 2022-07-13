#include <stdio.h>

int main()
{
	int n;
	scanf("%d", &n);
	
	int i, p1, p2;
	for (i = 1; i <= n; i++) {
		scanf("%d %d", &p1, &p2);
		printf("Case #%d: %d + %d = %d\n", i, p1, p2, p1 + p2);
	}
	
	return 0;
}