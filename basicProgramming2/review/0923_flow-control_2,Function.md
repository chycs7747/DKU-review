# For

```c
for(exp1;exp2;exp3)
  //statement
//next statement
```

> If **_exp2_** is missing. the rule is that the test is always true.

```c
int factorial = 1;
int i;
for(i=1;i<=n;i++)
  factorial *= i;
```

> Same as

```c
int factorial = 1;
int i=1;
while(i<=n){
  factorial *= i;
	i++;
}
```

# do-while

```c
do
  statement
while (exp);
//next statement
```

> A variant of the while statement. Instead of making its test at the top of the loop, it makes it at the bottom.

```c
int error;
do{
  printf("Input a positive integer: ");
  scanf(“%d”, &n);
  if(error = (n <= 0))
    printf("\nError: Negative...");
}
while(error);
```

# break

```c
while(1){
  scanf("%lf", &x);
  if(x<0.0) break; //if break, goto exc
  printf("%f\n",sqrt(x));
} //exc
```

> The break statement causes an exit from the innermost enclosing loop.

# continue

```c
int n;
for(n=1;n<=100;n++/*exc*/){
  if(n%3 != 0) continue; //if continue goto exc
  printf("4d\n",n);
}
```

> The continue statement causes the current iteration of a loop to stop and the next iteration to begin immediately.

# switch

```c
switch(exp){
  case exp1:
    //statement1
    break;
  case exp2:
    //statement2
    break;
  case exp3:
    //statement3
    break;
  case exp4:
    //statement4
    break;
  default:
    //statement default
    break;
}
```

> If **_exp_** is same expn(n is int), it will statementn.

```c
switch(val){
  case 1:
    ++a_cnt;
    break;
  case 2:
    ++b_cnt;
  case 3:
    ++c_cnt;
    break;
  default:
    break;
}
```

> If val == 2, '++b_cnt' and '++c_cnt'. Because case 2: don't write 'break'.

## conditional operator

```c
if(exp1) A = exp2;
else A = exp3;
```

> Same as

```c
A = exp1 ? exp2: exp3
```

```c
if(y<z) x = y;
else x = z;

//same as

x = (y<z) ? y : z
```

# Function

> Every C program has at least one function.

**main()**

> Structure of function.

```c
return_type function_name(parameter list){
  //body of the function
}
```

