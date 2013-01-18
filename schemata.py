'''
 schemata.py: Schemata based off Binstead's JAPE schemata

 Author: Zach Lockett-Streiff, inspired by Kim Binstead, whose paper can
         be found here: 
         
         http://citeseerx.ist.psu.edu/viewdoc/summary?doi=10.1.1.56.6823
'''
from nltk.corpus import cmudict
from nltk.corpus import wordnet as wn
import string
import templates as tmp
# Each schema searches internally for lexemes that satisfy preconditions
class Lotus():
  # What kind of murderer has fiber? A cereal killer.
  def __init__(self):
    self.nplist = self.nounPhrase()
    
    for npLex in self.nplist:
      # Lexical Preconditions
      self.homophone, npLex, self.np2 = self.lexical_preconds(npLex)
      if not self.homophone:
        continue
      # SAD description - generating the question
      self.qWords = self.sadGen(self.homophone, npLex)
      if not self.qWords[0] or not self.qWords[1]:
        continue
      # Relationships - generating the answer
      retval = self.relationships(self.qWords, self.np2)
      if not retval:
        continue
  
  def lexical_preconds(self, np):
    # Performs the Lexical Preconditions
    compLex = self.splitLexemes(np)
    homophone = self.getHomophone(compLex[0])
    if not homophone:
      return 0,0,0
    #print self.homophone[0]
    np2 = homophone + " " + compLex[1]
    #qWords = self.sadGen(homophone, np)
    return homophone, np, np2

  def relationships(self, qWords, np):
    # Passes the question keywords and the punny word into a template
    if not qWords or not np:
      #print 'qWords and/or np undefined'
      return 0
    tmp.cereal_killer(qWords[0],qWords[1],np)
    return 1
  
  def sadGen(self, homophone, np):
    # Get hypernym of np (murderer)
    # Get meronym of homophone (grains)
    # I now have my question keywords
    if not homophone or not np:
      #print 'homophone and/or np undefined'
      return [[],[]]
    hypernym = self.getHypernym(np)
    meronym = self.getMeronym(homophone)
    # Haven't tested this yet, but should eliminate
    # errant Synset notation in output
    if isInstance(meronym, list):
      meronym = meronym[0]
    if not hypernym or not meronym:
      #print 'Hypernym and/or meronym not found'
      return [[],[]]
    return [hypernym, meronym]

  def nounPhrase(self):
    # Finds a compound lexeme in WordNet, returns lemma/list of lemmas
    compNoms = []
    for synset in list(wn.all_synsets('n')):
      compNoms.extend([x.name for x in synset.lemmas if x.name.count('_')==1 and x.name != []])
    return compNoms

  def splitLexemes(self, nounPhrase):
    # Splits nounPhrase into component lexemes
    return nounPhrase.split('_')

  def getHomophone(self, wordA):
    # Finds a homophone of wordA
    phones = cmudict.dict()
    phone1 = []
    if wordA not in phones.keys():
      return 0
    phone1.extend(phones[wordA])
    phoneLst = []
    for i in phones.keys():
      if [a for a in phone1 if a in phones[i] and i != wordA]:
        phoneLst.append(i)
    if not phoneLst:
      #print 'No homophone found for ' + wordA
      return False
    return phoneLst[0]

  def getHypernym(self,np):
    # Gets most frequent hypernym of np
    # If this fails, exit the current call to getHypernym
    return wn.synsets(np)[0].hypernyms()[0].lemmas[0].name

  def getMeronym(self, homophone):
    # Gets meronym of homophone
    syn = wn.synsets(homophone)
    if not syn:
      #print 'No synset found for homophone'
      return False
    lst = [i.member_meronyms() for i in syn if i.member_meronyms()]
    if not lst:
      lst = [i.substance_meronyms() for i in syn if i.substance_meronyms()]
      if not lst:
        lst = [i.part_meronyms() for i in syn if i.substance_meronyms()]
        if not lst:
          #print 'Can\'t find any meronyms directly'
          # Can't find any meronyms of syn, invoke last-resort: find a synonym
          # that is not the string homophone
          lst = syn[0].definition.translate(string.maketrans('',''),
                string.punctuation).split(' ')
          if not lst:
            # No meronyms found
            return 0

          retLst = [i for i in lst if set(syn)&set(wn.synsets(i)) and (syn != wn.synsets(i))] 
          if not retLst:
            # retLst is empty
            return 0
          return retLst[0]
    return lst[0]

def main():
  lotus = Lotus()

if __name__ == '__main__':
  main()
