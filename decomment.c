//20180714ÇÑÀç¹Î  Assignment1 decomment.c
#include <stdio.h>
#include <stdlib.h>

enum DFAState{A,B,C,D,E};
int num_rows_after_error=0;					//number of \n after error

void after_error(char c){
	//It's a function counting the number of lines after error.
	if (c=='\n'){
		num_rows_after_error+=1;
	}
}

int main(){
	/* By dividing into 5 states, we switch state for determined cases.
	When c==\n, putchar(\n) regardless of the state where it exists.
	It uses the global variable num_rows_after_error.
	*/
	enum DFAState state=A;
	int quote=0, c=0, num_rows=1; 
	/*	Single quote(=') : 1, Double quotes(=") : 2*/
	// the number of num row starts from 1 
	while((c=getchar())!=EOF){				
		switch (state) {	
			case A:
				if (c=='\"'){
					putchar(c);
					state=B, quote=2;
				}
				else if (c=='\''){
					putchar(c);
					state=B, quote=1;
				}
				else if (c=='/'){
					state=C;
				}
				else if (c=='\n'){
					putchar(c);
					num_rows+=1;
				}
				else putchar(c);
				break;
			case B:
				if ((c=='\"')&(quote==2)){
					putchar(c);
					state=A;	
				}
				else if ((c=='\'')&(quote==1)){
					putchar(c);
					state=A;
				}
				else if (c=='\n'){
					putchar(c);
					num_rows+=1;
				}
				else putchar(c);
				break;
			case C:
				if (c=='*'){
					putchar(' ');
					state=D;
				}
				else if (c=='\n'){
					putchar('/');
					putchar(c);
					num_rows+=1;
					state=A;
				}
				else if (c=='/'){
					putchar(c);
				}
				else{
					putchar('/');
					putchar(c);
					state=A;
				}
				break;
			case D:
				after_error(c);
				if (c=='\n'){
					putchar('\n');
					num_rows+=1;
				}
				else if (c=='*'){
					state=E;
				}
				else continue;
				break;
			case E:
				after_error(c);
				if (c=='/'){
					state=A;
					num_rows_after_error=0;
				}
				else if (c=='\n'){
					putchar('\n');
					num_rows+=1;
					state=D;
				}
				else if (c=='*'){
					state=E;
				}
				else{
					state=D;
				}
				break;
		}
	}
	if ((state==D) || (state==E)){
		int er=num_rows-num_rows_after_error;	//denoting error line
		fprintf(stderr, "Error: line %d: unterminated comment\n", er);
		return EXIT_FAILURE;
	}
	else{
		return EXIT_SUCCESS;
	}
}

