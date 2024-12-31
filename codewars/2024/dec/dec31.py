cw = '''
Task
Your goal is to build a Berserk Rater function that takes an array/list of events of each episode (as strings) and calculate a rating based on that: you start with a score of 0 (hey, it's a work from Miura-sensei, I have great expectations to satisfy!) and you have to:

subtract 2 if "CG" is mentioned (case insensitive, once per string);
add 5 if "Clang" is mentioned (case insensitive, once per string);
if a sentence has both "Clang" and "CG", only "Clang" takes effect (just add 5, ignore "CG");
subtract 1 if neither is mentioned (I get bored easily, you know, particularly if you remove important parts and keep side character whining for half an episode).
You should then return a string, structured like this:

if the final score is less than 0: "worstest episode ever";
if the score is between 0 and 10: the score itself, as a string;
if the final score is more than 10: "bestest episode ever".
Examples
[ "is this the CG from a P2 game?",
  "Hell, no! Even the CG in the Dreamcast game was more fluid than this!",
  "Well, at least Gatsu does his clang even against a mere rabbit",
  "Hey, Cosette was not in this part of the story!", 
  "Ops, everybody dead again! Well, how boring..."
]
# Total score: (-2) + (-2) + 5 + (-1) + (-1) = -1
# Result: "worstest episode ever"

[ "missing the Count arc",
  "lame CG",
  "Gatsu doing its clang against a few henchmen", 
  "even more lame CG"
]
# Total score: (-1) + (-2) + 5 + (-2) = 0
# Result: "0"

[ "Farnese unable to shut the fuck up",
  "awful CG dogs assaulting everybody", 
  "Gatsu clanging the pig apostle!"
]
# Total score: (-1) + (-2) + 5 = 0
# Result: "2"

[ "spirits of the dead attacking Gatsu and getting clanged for good",
  "but the wheel spirits where really made with bad CG", 
  "Isidoro trying to steal the dragon Slayer and getting a sort of clang on his face",
  "Gatsu vs. the possessed horse: clang!", 
  "Farnese whining again...",
  "a shame the episode ends with that scrappy CG"
]
# Total score: 5 + (-2) + 5 + 5 + (-1) + (-2) = 10
# Result: "10"

[ "Holy chain knights being dicks",
  "Serpico almost getting clanged by Gatsu, but without losing his composure",
  "lame CG",
  "Luka getting kicked",
  "Gatsu going clang against the angels", 
  "Gatsu clanging vs Mozgus, big time!"
]
# Total score: (-1) + 5 + (-2) + (-1) + 5 + 5 = 11
# Result: "bestest episode ever"
Extra cookies if you manage to solve it all using a reduce/inject approach.

Oh, and in case you might want a taste of clang to fully understand it, click (one of the least gory samples I managed to find).
'''

def berserk_rater(synopsis):
    score = 0
    for line in synopsis:
        if 'clang' in line.lower():
            score += 5
        elif 'cg' in line.lower():
            score -= 2
        else:
            score -= 1
    return 'bestest episode ever' if score > 10 else 'worstest episode ever' if score < 0 else str(score)

print(berserk_rater([ "Holy chain knights being dicks",
  "Serpico almost getting clanged by Gatsu, but without losing his composure",
  "lame CG",
  "Luka getting kicked",
  "Gatsu going clang against the angels",
  "Gatsu clanging vs Mozgus, big time!"
]))