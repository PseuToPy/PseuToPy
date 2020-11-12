# %%
from src.pseutopy.pseutopy import PseuToPy
import astor
import textx

p = PseuToPy()
tree = p.convert_from_string("""
a+=1
a-=1
a*=1
a@=1
a/=1
a%=1
a&=1
a|=1
a^=1
a<<=1
a>>=1
a**=1
a//=1

display a""")
print(astor.to_source(tree))

# %%

# %%
