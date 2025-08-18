import nltk

from gensim.models import Word2Vec
from nltk.corpus import stopwords

import re

X_men = '''They called them mutants long before anyone agreed on a name. Magneto, Erik Lehnsherr, once said we are not the problem, we are the solution. But even he couldn't predict the 1973 incident at Lab-9, when a field surge flipped three labs and a meeting room into static soup. The staff logged it as 1973-11-06, 03:14 UTC. Victims four, two recovered. Sample IDs X-002, X23-A.

Jean Grey woke up with the taste of ozone and a headache that felt like someone had rearranged her skull. Not again, she whispered to herself. Telepathy, telekinesis, and the occasional reality hiccup were bad enough, but with sleep-deprived mood swings the odds of catastrophe rose sharply. Project Phoenix was mentioned in the files, always followed by emergency protocols in red ink.

Historical records show three power states: latent powers stayed hidden until some unknown trigger forced them out, active powers worked predictably like clockwork, and volatile powers refused any pattern at all, requiring strict containment. Lead-lined chambers, industrial foam, and total silence were common safety measures. The worst mistake was introducing water near an electrical mutant, and that rule was broken too many times.

Reed once claimed that the lattice could hold at negative one hundred twenty degrees Celsius if the feedline remained untouched. Hank never believed him, saying any sentence that started with if and ended with should was an invitation for disaster. In practice, they both knew the truth — nothing ever held for long.

There were always hyphenated words scribbled in the margins of reports, mother-in-law jokes that made no sense, X-men written in block capitals, numbers like 3.14 and 1e6 hidden in the data, random email addresses like professor.x@academy.org, and links to half-broken archives. Ellipses marked sudden stops, parentheses spiraled into nested loops, and no one could tell where one thought ended and the next began.

The last surviving entry from the Mutant Archive ended with a warning. Stay alive. Stay hidden. Or stay together. The rest of the world will not care which choice you make.

In 1986, the island of Genosha claimed it had no mutants. Satellite scans proved otherwise. Thermal anomalies marked twenty-three underground chambers, each averaging four meters below surface. Reports found on an encrypted drive spoke of collars tagged MK-IV, restricting cortical spikes to under 0.7 millivolts. The logs never named the captives, only numbers: 402, 718, 719B.

Storm hated confined air. The metal corridors of the submersible pressed on her senses like a steel coffin. Pressure readings rose with each dive, and her weather instincts fought the silence. The Atlantic above was calm, yet her bones ached as if a storm loomed just out of sight. Scott told her it was in her head. She didn’t believe him.

In training simulations, probability curves rarely matched reality. A model might predict an 85% chance of target neutralization, yet a coin dropped in the wrong moment could throw the result to zero. Logan treated probabilities as polite lies — useful only until the fight started. His claws made better arguments than any statistical forecast.

They never figured out why the Westchester alarm tripped at exactly 02:13 every third Thursday. Maintenance replaced wiring, swapped the backup generator, even gutted the entire subpanel. The alarm kept ringing, always the same timestamp, always cutting off after 41 seconds. Xavier wrote in his log that some things are not for fixing.

Cerebro’s records showed language anomalies among young mutants. One could speak twelve dialects after two hours of exposure, another could only communicate in palindromes. Written reports contained oddities like “madam I’m adam” repeated fifty-three times in a row, with no apparent meaning. Linguists left confused, telepaths left silent.

In 1999, a blackout across Eastern Europe lasted seventeen minutes. Satellite logs noted no solar flare, no geomagnetic spike, no explainable cause. Files later surfaced referencing “Subject Theta-7,” a mutant able to bend electromagnetic fields with nothing more than concentration. Witness accounts conflicted — some claimed to see a boy in the rubble, others swore no one was there at all. Energy signatures burned into the data like scars, still unexplained two decades later.

Jubilee once described mutant life as “walking into every room carrying fireworks no one asked for.” Her files included timestamps, discharge levels, and even stress ratings before each flare. Yet the most important detail was never technical — it was that her sparks made children laugh in shelters where hope was short supply. Analysts flagged the entry as “non-essential,” but it stayed in the record anyway.

Warpath wrote long, unfiltered reports filled with metaphors instead of measurements. He compared training halls to “caves echoing with steel,” and tactical drills to “storms waiting for permission to break.” His language baffled technicians but resonated with other mutants, who said they understood him more than any dry percentage or curve. Sometimes, his words revealed more truth than a hundred charts.

By 2005, geneticists tracked more than three hundred known mutations worldwide. They mapped alleles, cross-referenced genomes, and still ended with a margin of error wider than comfort allowed. A note buried in the data read: Evolution is not an equation, it’s a tide. You can measure waves but never predict when the ocean will rise.

Magneto’s prison cell was technically a floating room, suspended by non-ferrous cables over a saltwater pit. Every bolt and weld was ceramic. Guards rotated every ninety minutes to avoid familiarity, each carrying no metal larger than a paperclip. The design was flawless until someone smuggled in a simple belt buckle.

Some powers aged with their hosts. Pyro’s flames lost brightness after age fifty, while Colossus’s steel skin took longer to manifest each morning. Beast kept records of these declines, noting cellular efficiency drops in percentage points: 0.9, 1.3, 1.8. He called it entropy in slow motion.

Not all mutants fought. Some built. Forge once designed a drone the size of a fingernail that could map a city block in thirty seconds. It flew once, mapped perfectly, then exploded in midair. The debris weighed less than a feather. No one could replicate it.

Records of mutant births show spikes after high-energy events: solar flares, nuclear tests, and the unexplained blackout of ’94. Analysts plotted them on a timeline and found fractal-like patterns, repeating across decades. The same gap lengths, the same sudden rises. A cycle hiding in plain sight.

The last known sighting of Mystique was not on any battlefield but at a small train station in rural France. CCTV caught her walking past the ticket booth, face unshifted, carrying a book with no title on the cover. She boarded the train, sat by the window, and vanished when it emerged from the next tunnel.

Mutants aren’t just powerful — they’re proof that humanity can grow beyond its limits. They don’t rely on gadgets or alien bloodlines. Their abilities are part of who they are, stitched into their DNA, and that makes their heroism feel more personal. When a mutant saves a city, it’s not a mask or a machine doing the work. It’s them, body and soul.

People admire mutants because they were born carrying a weight most couldn’t handle. There’s no “before” for them — no moment where they were ordinary. They grew up different, learned to control dangerous gifts, and still chose to help a world that didn’t always help them. That resilience earns respect.

Everyday citizens can see themselves in mutants more easily than in other heroes. You can’t train to be from another planet or buy your way into super strength, but the idea that evolution could give anyone the potential to do great things is inspiring. Mutants make people believe that heroism is not just an accident — it can be destiny.

When a mutant steps in to stop a disaster, the crowd knows it’s more than just power on display. It’s living proof that humanity’s future might not be something to fear. It might be something to look forward to.

Mutants are born different. They don’t choose their powers, and they don’t wait for an accident or a cosmic event to awaken them. Their abilities manifest naturally, often in childhood, and that alone terrifies people. A hero in armor is a man in a machine. A mutant is something else entirely — living proof that nature can rewrite the rules at will.

For most citizens, it’s easier to trust heroes whose powers have an explanation. A soldier in a suit, a scientist bitten by something strange, an alien from another planet — those stories have beginnings and boundaries. Mutants have neither. Their origins are tangled in biology, genetics, and whispers of evolution, which means anyone, anywhere, could be one without knowing it yet. That uncertainty breeds fear.

Fear turns into prejudice fast. Newspapers talk about mutants as a “problem,” not as individuals. Politicians campaign on the promise of registration. Neighbors glance too long at a kid who runs faster than he should. When a mutant saves a city, the headlines still focus on the destruction caused during the rescue. If a non-mutant does the same, they get parades.

Superheroes are celebrated because they are seen as exceptional individuals — rare, special, chosen. Mutants are hated because they represent a future people can’t control. It’s not that the world doesn’t need them. It’s that the world fears it might become them.

Mutants sit in a strange place in the public mind. To some, they’re heroes — proof that evolution can push humanity forward. To others, they’re walking reminders that the world is changing in ways no one can control. Every time a mutant saves lives, the headlines split: one side celebrates, the other asks if their powers make them too dangerous to be trusted.

The admiration is easy to understand. Many mutants spend their entire lives training to keep their abilities in check, choosing to risk themselves to protect strangers. They face the same threats as any other superhero, but often without the public’s full support. That persistence is hard not to respect.

The fear comes from the unknown. A masked vigilante can hang up the suit. An alien can fly home. But mutants can’t stop being what they are, and no one can predict what abilities the next generation will have. For some, that’s exciting — a glimpse into the future of humankind. For others, it’s terrifying — a sign that humanity might become something unrecognizable.

And so, mutants live in this constant push and pull between acceptance and suspicion. Loved in some cities, feared in others, and always aware that a single bad moment could tip the balance.

Mutants didn’t ask to be born different. But the world treats them like it’s a choice. A hero in a cape gets a parade. A mutant in the same fight gets a police escort… to a containment cell.

It’s not about what they’ve done. It’s about what they could do. People fear that power they can’t switch off, can’t hand over, can’t control. Every mutant is a walking question mark, and humans hate unanswered questions.

The irony? Most mutants want the same thing as everyone else — a life. Friends. Peace. Safety. But the second their genes reveal something extraordinary, that dream burns up in suspicion.

For every cheer, there’s a jeer. For every handshake, there’s a locked door. Mutants fight for the people, but the people can’t decide if they’re saviors or the first wave of something worse.'''


# Text Preprocessing the data
text = re.sub(r'[[0-9]*]', ' ', X_men)       # remove numbers in brackets []
text = re.sub(r'\s+', ' ', text)             # remove extra whitespace
text = text.lower()                          # convert to lowercase
text = re.sub(r'\d', ' ', text)              # remove digits
text = re.sub(r'\s+', ' ', text)             # remove extra whitespace again

# Tokenizing Sentences
sentences = nltk.sent_tokenize(X_men)

# Preparing the dataset
sentences = [nltk.word_tokenize(sentence) for sentence in sentences]
for i in range(len(sentences)):
    sentences[i] = [word for word in sentences[i] if word not in stopwords.words('english')]
    
# Training the Word2Vec model
model = Word2Vec(sentences, vector_size=100, window=5, min_count=1, workers=4)
# word2vec is applied for huge amount of data

# Vocabulary
# in this paragraph if we want to find the vocalbulary & create a object called words
words = model.wv.key_to_index
print(words)

# Finding Word Vectors
vector = model.wv['mutant']
#if i want to find the vector of mutant word and if i want to find the relationship 

# Most similar words
similar = model.wv.most_similar('disaster')
#if i try to find most similar word related to the war 

similar1 = model.wv.most_similar('hate')

similar2 = model.wv.most_similar('mind')



#STILL MORE RESEARCH GOING ON REGARDS TO THE WORD2VEC











