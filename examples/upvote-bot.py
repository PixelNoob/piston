import time
from piston.steem import Steem
import os
import json

steem = Steem(wif=os.environ["WIF"])
print ("login OK")
authors = json.loads(os.environ["AUTHORS"])
print ("checking authors OK")
for c in steem.stream_comments(mode="head"):
     if c["author"] in authors and c.identifier == c.openingPostIdentifier:
        try:
            time.sleep(1000)
            print(c.upvote())
        except:
            print ("something went wrong, your vote was NOT casted")

