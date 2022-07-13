#include <stdio.h>

int main()
{
	int n, st;
	scanf("%d %d", &n, &st);
	
	int i, tmp;
	for (i = 1; i <= n; i++) {
		scanf("%d", &tmp);
		if (tmp < st)
			printf("%d ", tmp);
	}
	
	return 0;
}