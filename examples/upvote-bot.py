from piston.steem import Steem
import os
import json
steem = Steem(wif=os.environ["WIF"])
authors = json.loads(os.environ["AUTHORS"])
for c in steem.stream_comments(mode="head"):
     if c["author"] in authors and c.identifier == c.openingPostIdentifier:
        try:
            print(c.upvote())
        except:
            print ("something went wrong, but your vote was casted and the bot its still running")
