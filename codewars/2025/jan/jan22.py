cw = '''
Description:
Rotation ciphers are very vulnerable to brute force attacks. There are only 25 possible ways to decrypt the message.

Example Encoded Message:ymjxvznwwjqnxhzyj

Possible Decoded Messages:

znkywaoxxkroyiazk, aolzxbpyylspzjbal, bpmaycqzzmtqakcbm,
cqnbzdraanurbldcn, drocaesbbovscmedo, espdbftccpwtdnfep,
ftqecguddqxueogfq, gurfdhveeryvfphgr, hvsgeiwffszwgqihs,
iwthfjxggtaxhrjit, jxuigkyhhubyiskju, kyvjhlziivczjtlkv,
lzwkimajjwdakumlw, maxljnbkkxeblvnmx, nbymkocllyfcmwony,
ocznlpdmmzgdnxpoz, pdaomqennaheoyqpa, qebpnrfoobifpzrqb,
rfcqosgppcjgqasrc, sgdrpthqqdkhrbtsd, thesquirreliscute,
uiftrvjssfmjtdvuf, vjguswkttgnkuewvg, wkhvtxluuholvfxwh,
xliwuymvvipmwgyxi
If you scan through the list you will see only a few that contain an English word longer than two characters. thesquirreliscute is the only one that could be completely separated into english words to form the message "the squirrel is cute".

Your job for this kata is to make a function that will give all possible decoded messages given the encoded message and suspected contents.

The original unshifted alphabet should also be tested for, making it a total of 26 possible ways to decrypt the message. The order of the returned results does not matter. See last line below for an example:

Encoded message: "ymjxvznwwjqnxhzyj"
Suspected content: "squirrel"
returns ["thesquirreliscute"]

Encoded message: "lzwespnsdmwakafxafalq"
Suspected content: "max"
returns ["maxftqotenxblbgybgbmr", "themaxvalueisinfinity"]

Encoded message: "pumy"
Suspected content: "um"
returns ["pumy"]
'''


def decode(msg, contents):
    sentence_arr = []

    for offset in range(26):
        rotation = ''.join(chr((ord(char) - ord('a') + offset) % 26 + ord('a')) for char in msg)
        sentence_arr.append(rotation)

    return [sentence for sentence in sentence_arr if contents in sentence]


print(decode('ymjxvznwwjqnxhzyj', 'squirrel'))
