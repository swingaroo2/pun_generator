'''
 templates.py: Riddle surface form templates

 Author: Zach Lockett-Streiff, inspired by Kim Binstead, whose paper can
         be found here:

         http://citeseerx.ist.psu.edu/viewdoc/summary?doi=10.1.1.56.6823
'''
'''
A template looks like this in the paper:
  {Relations:
    describes(NPStr, {cross_between(_,X,Y)},
   SF: (presumably means "surface form")
    cross(X,Y,NPStr)}
'''
# JAPE templates: link uninstantiated SAD (USAD) with surface form
'''
Commented out until I get describes(...) working - do I make separate
templates for each representation in the JAPE paper, or do I make just
a few generalizable templates.

class Template:

  def __init__()

'''


# Helper functions for printing surface forms.
def cereal_killer(l1,l2,ans):
  print "\nWhat do you call a {0} with {1}? A {2}".format(l1,l2,ans)

def cross(l1,l2,ans):
  print "\nWhat do you get when you cross {0} and {1}? {2}".format(l1,l2,ans)

def spec_class(l1,l2,ans):
  print "\nWhat do you call {0} {1}? {2}".format(ll,l2,ans)

def class_has(cl,has,ans):
  print "\nWhat kind of {0} has {1}? {2}".format(cl,has,ans)

def act_verb(l1,l2,ans):
  print "\nWhat kind of {0} can {1}? {2}".format(l1,l2,ans)

def inact_verb(l1,l2,ans):
  print "\nWhat kind of {0} can you {1}? {2}".format(l1,l2,ans)

def vncompare(npa,npb,np1,verb1,np2,verb2):
  print "\nWhat is the difference between {0} and {1}?".format(npa,npb)
  print "You {0} {1} but you cannot {2} {3}.".format(verb1,np1,verb2,np2)

def vvcompare(np1,np2,verb11,verb12,verb21,verb22):
  print "\nWhat is the difference between {0} and {1}?".format(np1,np2)
  print "One {0} and {1}, the other {2} and {3}.".format(verb11,verb12,verb21,verb22)

def poscompare(np1,np2,npStr):
  print "\nHow is {0} like {1}? They are both {2}.".format(np1,np2,npStr)

def negcompare(np1,np2,npStr1,npStr2):
  print "\nWhat is the difference between {0} and {1}?".format(np1,np2)
  print "One is {0} and the other is {1}.".format(npStr1,npStr2)

def main():
  #print negcompare('1','2','3','4')
  pass

if __name__ == "__main__":
  main()
