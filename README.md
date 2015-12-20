# Is your DNS round-robin setup really round?

![Almost ideal round robin](http://agafonov.pp.ru/blog/wp-content/uploads/2015/12/round-robin.png)

Just test! Take this simple script and test on your own, with python 2 or 3.

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
================ google.com ================ 20/20
  188.43.66.170 [               ||||| 25.0%] 5
  188.43.66.187 [               ||||| 25.0%] 5
  188.43.66.174 [          |||||||||| 50.0%] 10
```
