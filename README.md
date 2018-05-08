# Random vs SystemRandom


Python have 2 ways to generate randomness, first is using random module and the second is using secrets.SystemRandom module  
This repo only to show how the result using random or SystemRandom (which not affected by seed)  

Random without seed  
First try:  
1 :  93  
2 :  114  
3 :  95  
4 :  95  
5 :  100  
6 :  104  
7 :  94  
8 :  91  
9 :  104  
10 :  110  
Second try:  
1 :  89  
2 :  105  
3 :  95  
4 :  105  
5 :  122  
6 :  88  
7 :  106  
8 :  96  
9 :  90  
10 :  104  

Random with seed 1  
First try:  
1 :  98  
2 :  101  
3 :  93  
4 :  96  
5 :  112  
6 :  92  
7 :  102  
8 :  89  
9 :  119  
10 :  98  
Second try:  
1 :  98  
2 :  101  
3 :  93  
4 :  96  
5 :  112  
6 :  92  
7 :  102  
8 :  89  
9 :  119  
10 :  98  

System Random without seed  
First try:  
1 :  106  
2 :  92  
3 :  82  
4 :  96  
5 :  111  
6 :  105  
7 :  111  
8 :  94  
9 :  101  
10 :  102  
Second try:  
1 :  83  
2 :  110  
3 :  105  
4 :  106  
5 :  83  
6 :  100  
7 :  97  
8 :  123  
9 :  106  
10 :  87  

System Random with seed 1  
First try:  
1 :  113  
2 :  109  
3 :  100  
4 :  97  
5 :  102  
6 :  99  
7 :  102  
8 :  94  
9 :  102  
10 :  82  
Second try:  
1 :  98  
2 :  102  
3 :  103  
4 :  94  
5 :  97  
6 :  114  
7 :  96  
8 :  89  
9 :  103  
10 :  104  


If we see, the random from seed is always return the same result on the first or second try  
But the random seed from system random always return different result  

If we see the help in SystemRandom (by using `help(secrets.SystemRandom.seed)`) it shown:  
```
Help on function seed in module random:

seed(self, *args, **kwds)
    Stub method.  Not used for a system random number generator.
```

And also random seems faster than SystemRandom:  
random  
```
real	0m0.042s
user	0m0.034s
sys	0m0.008s
```
SystemRandom  
```
real	0m0.050s
user	0m0.030s
sys	0m0.019s
```

Rule of thumbs:  
Use SystemRandom when it related to security (eg: random password generate) and use random for the other else.  
