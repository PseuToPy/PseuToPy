# %%
from src.pseutopy.pseutopy import PseuToPy
import astor
import textx


p = PseuToPy()
for i in """

    li += 1,2,3
    a+=*1,2,3
    a+=*[1,2,3]
    a+=*1
    """.split("\n"):
    try:
        tree = p.convert_from_string(i)
        print(astor.to_source(tree))
    except:
        print("ERROR converting :", i)
# %%

# %%
