c=10
print("celcius","Fahrenheit")
while c<=30:
    f = (9/5*c)+32
    print("{0:^7}\t{1:^10.0f}".format(c,f))
    c +=5
