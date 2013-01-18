'''
 relations.py: functions for evaluating relations between words from
               WordNet

 Author: Zach Lockett-Streiff, inspired by Kim Binstead, whose paper can
         be found here:

         http://citeseerx.ist.psu.edu/viewdoc/summary?doi=10.1.1.56.6823

 Notes to self:
    + class -> hyponym; has -> meronym;
    + from nltk.corpus import cmudict for phonetic pronounciations
 Should support the following semantic relations:
    + class: relates lexeme to supertype
    + specifier: relates lexeme to class-distinguishing feature
    + adjective: relates lexeme to adjective describing it
    + has: relates lexeme to part of itself
    + act_verb: relates lexeme to some action it performs
    + inact_verb: relates lexeme to action performed on it
      - (for above 2: verb synonyms?)

in lexical preconditions: Is written_form really necessary? Yes, for
                          certain circumstances (checking if homophone can
                          be found as a lexeme)
described_by: SAD generator
describes: Asserting relationships

'''

from nltk.corpus import wordnet as wn
from nltk.corpus import cmudict

def syn(x,y):
  # If strings x and y are members of a common synset
  return y in [l.name for s in wn.synsets(x) for l in s.lemmas]

def ant(x,y):
  # If strings x and y are opposites
  ants = set()
  for syn in wn.synsets(x):
    ants.update(a for m in syn.lemmas for a in m.antonyms())
  return y in list({x.name for x in ants})

def hypo(x,y):
  # If string x is a hyponym of string y
  hypos = set()
  for i in wn.synsets(y):
    hypos.update(i.hyponyms())
  if (hypos & set(wn.synsets(x))):
    return True
  return False
'''
# NOTE: Binstead does not use hypernyms. I'll keep this function
        around for good measure
def hyper(x,y):
  # If x is a hypernym of y
  hypers = set()
  for i in wn.synsets(x):
    hypers.update(i.hypernyms())
  if (hypers & set(wn.synsets(y))):
    return True
  return False
'''
def mero(x,y):
  # If string x is a meronym of ("part of") string y
  meros = set()
  for i in wn.synsets(y):
    meros.update(i.member_meronyms())
  if (meros & set(wn.synsets(x))):
    return True
  return False

''''''''''''''''''''''''
'''Phonetic relations'''
''''''''''''''''''''''''
def homonym(x,y):
  # If x and y are homonyms (two words, similar pronunciations)
  # Check if any pronunciations are present in both phoneme sets
  # I can get away with this because I threw away heteronyms
  d = cmudict.dict()
  if x not in d:
    print x + " not in CMU pronunciation dictionary."
  if y not in d:
    print y + " not in CMU pronunciation dictionary."
  if x not in d or y not in d:
    return False

  for phone in d[x]:
    if phone in d[y]: return True
  else: return False

def rhyme(x,y,xVer=0,yVer=0):
  # If x rhymes with y
  # Different initial consonant sounds
  # Identical remainders (codas)
  d = cmudict.dict()
  if x not in d:
    print x + " not in CMU pronunciation dictionary."
  if y not in d:
    print y + " not in CMU pronunciation dictionary."
  if x not in d or y not in d:
    return False

  phone1 = d[x][xVer]
  phone2 = d[y][yVer]

  if phone1[0] != phone2[0]:
    return phone1[-1] == phone2[-1]

  return False

def allit(x,y,xVer=0,yVer=0):
  # If x alliterates with y
  # Identical non-nil initial consonant sounds (non-nil?)
  # different remainders
  d = cmudict.dict()
  if x not in d:
    print x + " not in CMU pronunciation dictionary."
  if y not in d:
    print y + " not in CMU pronunciation dictionary."
  if x not in d or y not in d:
    return False

  phone1 = d[x][xVer]
  phone2 = d[y][yVer]

  if phone1[0] == phone2[0]:
    return phone1[-1] != phone2[-1]

  return False

def spoon(a,b,c,d,aVer=0,bVer=0,cVer=0,dVer=0): # Haha, bVer -> beaver
  '''
  Four words (a,b,c,d,) form 2 spoonerizing phrases if:
    A and C rhyme
    B and D rhyme
    A and D alliterate, and
    B and C alliterate
  '''
  return (rhyme(a,c,aVer,bVer) and rhyme(b,d,bVer,dVer) and
          allit(a,d,aVer,dVer) and allit(b,c,bVer,cVer))


def main():
  '''testing code goes here'''
  #print homonym('rouzt','route')
  #print homonym('plain','plane')
  #print spoon('cute','mitten','mute','kitten')
  #print spoon('cat','bake','bat','cake')
  #print allit('gate','gait')
  #print rhyme('bat','cat')
  #print syn('dog','frump')
  #print ant('black','white')
  #print hypo('dog','pooch')
  #print hyper('pooch','dog')
  #print mero('dog','pack')
  pass

if __name__ == '__main__':
  main()
