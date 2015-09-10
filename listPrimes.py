#!/usr/bin/env python

class mangeNombre:
  "Class comtaining prime and next prime"
  def __init__(self, c = 2, n = None):
    self.current = c;
    self.nextMangeNombre = n;
  def eat(self, arg):
    if arg%self.current != 0:
      # Tested number is not divideable by current mangeNombre
      if self.nextMangeNombre != None:
        # Tested number will be tested by next mangeNombre instance
        return (self.nextMangeNombre).eat(arg);
      else :
        # Tested Number is a prime Number
        print arg;
        return True;
    else :
      return False;

def listPrimes(N):
  """List primes ranging from 2 to N"""
  tab = [];
  tab.append(mangeNombre(2));
  for i in range (2,N):
    if tab[0].eat(i) == True:
      tab.append(mangeNombre(i));
      tab[len(tab)-2].nextMangeNombre = tab[len(tab)-1];
    else :
      i+=1;
      
#####

listPrimes(7906)
