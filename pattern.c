#include <stdio.h>
/*Program to print pattern*/

int main() 
{

    int n, i;
    scanf("%d", &n);
    int lnum= 2*n-1;
    //middle row is n itself
    i = 1;
    while ((i<=lnum)){
        int val = n;
        int val2;
        int i1;
        if (i<= n){i1 =i;}
        else{ i1 = lnum-i+1;}
            
            for (int x=1; x<=lnum;x++){
                if (x <=n){
                    printf("%d ", val);
                    if (x<i1){val -= 1;}
                    val2 = val;
                }
                else{
                    int x1=lnum-x+1;
                    if (x1<i1){val2 += 1;}
                    printf("%d ", val2);
                    
                }
                
            }
            
        
        
        printf("\n");
        i+=1;
    }
     
  	// Complete the code to print the pattern.
    return 0;
}
