### --------------------------------------------------------------------
### mydc.s
###
### Desk Calculator (dc)
### --------------------------------------------------------------------

	.equ   ARRAYSIZE, 20
	.equ   EOF, -1
	
.section ".rodata"

scanfFormat:
	.asciz "%s"
### --------------------------------------------------------------------

        .section ".data"

### --------------------------------------------------------------------

        .section ".bss"
buffer:
        .skip  ARRAYSIZE

### --------------------------------------------------------------------

	.section ".text"

	## -------------------------------------------------------------
	## int main(void)
	## Runs desk calculator program.  Returns 0.
	## -------------------------------------------------------------

	.globl  main
	.type   main,@function

main:

	pushl   %ebp
	movl    %esp, %ebp

input:

	## dc number stack initialized. %esp = %ebp
	
	## scanf("%s", buffer)
	pushl	$buffer
	pushl	$scanfFormat
	call    scanf
	addl    $8, %esp

	## check if user input EOF
	cmpl	$EOF, %eax
	je	quit
	
	## PSEUDO-CODE
	## /*
	##  * In this pseudo-code we assume that you do not use no local variables
	##  * in the _main_ process stack. In case you want to allocate space for local
	##  * variables, please remember to update logic for 'empty dc stack' condition
	##  * (stack.peek() == NULL). 
	##  */
	##
        ##  while (1) {
        ##     /* read the current line into buffer */
        ##     if (scanf("%s", buffer) == EOF)
        ##         return 0;
        ## 
        ##     /* is this line a number? */
        ##     if (isdigit(buffer[0]) || buffer[0] == '_') {
        ##        int num;
        ##        if (buffer[0] == '_') buffer[0] = '-';
        ##        num = atoi(buffer);
        ##        stack.push(num);	/* pushl num */
        ##        continue;
        ##     }
        ## 
        ##     /* p command */
        ##     if (buffer[0] == 'p') {
        ##        if (stack.peek() == NULL) { /* is %esp == %ebp? */
        ##           printf("dc: stack empty\n");
        ##        } else {
        ##           /* value is already pushed in the stack */
        ##           printf("%d\n", (int)stack.top()); 
        ##        }
        ##        continue;
        ##     }
        ## 
        ##     /* q command */
        ##     if (buffer[0] == 'q') {
        ##        goto quit;
        ##     }
        ##  
        ##     /* + operation */
        ##     if (buffer[0] == '+') {
        ##        int a, b;
        ##        if (stack.peek() == NULL) {
        ##           printf("dc: stack empty\n");
        ##           continue;
        ##         }
        ##         a = (int)stack.pop();
        ##         if (stack.peek() == NULL) {
        ##            printf("dc: stack empty\n");
        ##            stack.push(a); /* pushl some register value */
        ##            continue;
        ##         }
        ##         b = (int)stack.pop(); /* popl to some register */
        ##         res = a + b;
        ##         stack.push(res);
        ##         continue;
        ##     }
        ## 
        ##     /* - operation */
        ##     if (buffer[0] == '-') {
        ##        /* ... */
        ##     }
        ## 
        ##     /* | operation */
        ##     if (buffer[0] == '|') {
        ##        /* pop two values & call abssum() */
        ##     }
        ## 
        ##     /* other operations and commands */
        ##     if (/* others */) {
        ##        /* ... and so on ... */
        ##     }
        ##  
        ##   } /* end of while */
        ## 

quit:	
	## return 0
	movl    $0, %eax
	movl    %ebp, %esp
	popl    %ebp
	ret
