# Is your DNS round-robin setup really round?

![Almost ideal round robin](http://agafonov.pp.ru/blog/wp-content/uploads/2015/12/round-robin.png)

Just test! Take this simple script and test on your own.

Options:
```
usage: dns_round_robin_test.py [-h] [-c COUNT] [-d DELAY] name

positional arguments:
  name                  DNS name to test

optional arguments:
  -h, --help            show this help message and exit
  -c COUNT, --count COUNT
                        set total count of resolves
  -d DELAY, --delay DELAY
                        set delay between resolves in 1/100s of second
```

Sample run command:
```
$ ./dns_round_robin_test.py google.com -c 20
```

Sample output:
```
==== google.com ======== 20 of 20 ====
   188.43.66.154 [              |||||| 30.0%] 6
   188.43.66.177 [                |||| 20.0%] 4
   188.43.66.159 [          |||||||||| 50.0%] 10
```
