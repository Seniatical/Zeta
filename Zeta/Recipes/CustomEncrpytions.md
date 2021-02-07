Here I will show you many ways of forming your custom cipher

**Loading From `.json` file:**
```py
import json
import Zeta

with open('.json', 'r') as myhashes:
	hashes =  json.load(myhashes)

MyHashmap = Zeta.Hashmap(complexity=5, hashes=**hashes, is_same=True)

del MyHashmap
```

**Saving your hashmaps:**
```py
import Zeta

MyHashmap = Zeta.Hashmap(complexity=5, hashes=**MyHashes, is_same=True)

MyHashmap.export('.json')
```

**Combining 2 hashmaps:**
```py
## Must require 2 hashmap objects
import Zeta

MyHashmap = Zeta.LoadHashFromFile('.json')
MyNewHashmap = Zeta.Hashmap(complexity=2, hashes=**MyHashes, is_same=True)

CombinedHashmap = MyHashmap + MyNewHashmap
```