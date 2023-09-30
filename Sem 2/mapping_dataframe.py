import pandas as pd

frame = pd.DataFrame({'numbers': range(1,11), 'chars': ['a']*10})
mapping = {10: 'ten', 1: 'one', 2: 'two', 3: 'three', 4: 'four',5: 'five', 6: 'six', 7: 'seven', 8: 'eight', 9: 'nine'}
print(frame)
frame['name']=frame['numbers'].map(mapping)
print(frame)
frame['numbers'] = frame['numbers']*(frame['numbers'])
print(frame)
