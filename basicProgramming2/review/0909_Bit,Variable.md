#Bit & Byte
>Human’s number expression

<pre>decimal system
0 1 2 3 4 5 6 7 8 9
57 = (5*10^1)+7
</pre>

> Computer’s number expression

<pre>
'bi'nary digi't' = bit
  		   0 1
 [2 bits]
 00 01 10 11
 0  1  2  3
 [8 bits]
 0000 0000 => 1byte => C stores/retrieves variable in unit
</pre>

> Numeric system : How to use negative number in computer (2's complement)

<pre>
0000 0110 = 6
1111 1001 => 1's complement
1111 1010 => +1 => 2's complement => -6
0000 0110 + 1111 1010 = 1 0000 0000 => delete 9Bits (1) = > 0000 0000 => 0
</pre>
---
```c
#include <stdio.h>

int main(void){
  char a = -5; //signed char a
  unsigned char b;
  
  b = a;
  
  printf("%d, %u\n", a, b);
  return 0;
}
```

> Output

<pre>
  char => 1byte => 1bit
  0000 0101 = 5
  1111 1010 => 1's complement
  1111 1011 => 2's complement => -5 (signed : negative) => 251 (unsigned : postive)
</pre>

#Variables
> Variables

<pre>
  - It is a name given to a storage area that our programs can manipulate.
  - A placeholder for a value.
</pre>

> Declare Variables

```c
int some_number // 'int' is data type, 'some_number' is name of variable
```

<pre>
- Declaring some space for a variable called some_number, which will be used to store integer data.
</pre>

> Initialize variable

```c
int some_number = 3;
```

<pre>
- Declare variable some_number and assign 3 to it.
- “=” is assignment expression.
- If variable is not initialized, the variable contains garbage value. 
</pre>

>Rule for constructing variable name

<pre>
- Characters allowed : 
  - Underscore(_)
  - Capital/Small letters (A-Z, a-z)
  - Digits (0-9)
- Blanks & commas are not allowed.
- No special symbols other than underscore(_) are allowed.
- First character should be alphabet or underscore.
- Variable name should not be reserved word.
</pre>
