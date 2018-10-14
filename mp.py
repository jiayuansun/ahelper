import pandas as pd

def just_foo_cols(self):
    """get a list of colum names containing the string 'foo'
    """
    return [x for x in self.columns if 'foo' in x]

pd.DataFrame.just_foo_cols=just_foo_cols
df=pd.DataFrame([list(range(4))],columns=["A","foo","foozball","bar"])
df.just_foo_cols()
pass

del pd.DataFrame.just_foo_cols