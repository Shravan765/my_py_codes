#include <stdio.h>

/*
Write a program to find and print the largest prime palindrome (a number that is both a prime and a palindrome) within a given range. Your program should take two positive integer inputs, start and end from the user, representing the inclusive range within which to search for the prime palindrome.

THIS GIVES ALL PRIME PALINDROME AND TELLS THE LARGEST
*/

int pw(int b, int e){ //power function
	int val = 1;
	for (int i = 0; i < e; i++){
		val*= b;
	}
	return val;
} //closes

int checkprime(int n){ //function to check if the number is prime
	for( int i = 2; i < n ;i++)	{
		if (n % i ==0){
			return 0;
			break;
		}
	}
	return 1;
} //function closes


int main() //main function begins 
{
	int lp = 0; //will give at end largest palindrome
	//int val = pw(10, 4);
		//printf("%d",val);
	int numi, numf;
	int pnum;
	printf("Enter starting and ending number with space  : ");
	scanf("%d %d", &numi, &numf);
	int i = numi;
	while (i < numf) {
		int key;
		key = checkprime(i);
		if (key == 1){
		// if number is prime we will check its palimdrome
		//printf("\n%d . ", i);
		
		int p10 = 0;
		while (i%pw(10, p10 ) != i){
		
			p10+=  1;
		
		}
		//p10 gives number of digits  
		//printf("%d %d\n", i , p10);
		int x = 1;
		int sum = 0;
		int tno= 0;
		int temp;
		while (x<=p10){
			temp = i%pw(10,x);
			int tno = temp/pw(10,x-1); 
			//printf("\t%d\t", tno );
			sum += tno*pw(10, (p10-x));
			x+=1;
			
		}
		//printf("%d   ->  %d\n", i, sum);
		if (sum == i) {
		printf("%d\n", i);
		lp = i;
		}
		
		}
		i+=1;
	

}    
printf("\n\nGREATEST PRIME PALINDROME : %d\n\n", lp);
}//program ends
