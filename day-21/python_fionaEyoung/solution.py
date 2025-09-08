from operator import sub
from itertools import pairwise
# Numeric keypad
# +---+---+---+
# | 7 | 8 | 9 |
# +---+---+---+
# | 4 | 5 | 6 |
# +---+---+---+
# | 1 | 2 | 3 |
# +---+---+---+
#     | 0 | A |
#     +---+---+
#
# Directional keypad
#     +---+---+
#     | ^ | A |
# +---+---+---+
# | < | v | > |
# +---+---+---+

NUM_KEY = {'7': (0,0), '8': (0,1), '9': (0,2),
           '4': (1,0), '5': (1,1), '6': (1,2),
           '1': (2,0), '2': (2,1), '3': (2,2),
                       '0': (3,1), 'A':(3,2)}

DIR_KEY = {         '^':(0,1),'A':(0,2),
          '<':(1,0),'v':(1,1),'>':(1,2)}

def v_to_button(start, end, key_dict=DIR_KEY):
    return tuple(map(sub, key_dict[end], key_dict[start]))

# def v_to_dir(start, end):
#     return tuple(map(sub, DIR_KEY[end], DIR_KEY[start]))

def dir_keys(v):
    return {
            '<':max(v[1]//-1, 0),
            '>':max(v[1], 0),
            '^':max(v[0]//-1, 0),
            'v':max(v[0], 0)
    }

def button_seqence(target_buttons, key_dict=DIR_KEY):
    return ''.join(''.join( [k*i for k, i in dir_keys(v_to_button(s,e,key_dict=key_dict)).items() if i]+['A'] ) for s,e in pairwise('A'+target_buttons) )

fname = 'test.txt'
with open(fname, 'r') as f:
    codes = [l.strip() for l in f.readlines()]
codes

for code in codes:
    print(button_seqence(button_seqence(button_seqence(code, key_dict=NUM_KEY))))


<<vAA>A>^AvAA<^A>A<<vA>>^AvA^A<vA>^A<<vA>^A>AAvA^A<<vA>A>^AAAvA<^A>A
<vA<AA>>^AvAA<^A>A<v<A>>^AvA^A<vA>^A<v<A>^A>AAvA^A<v<A>A>^AAAvA<^A>A

<<vA>>^AAAvA^A<<vAA>A>^AvAA<^A>A<<vA>A>^AAAvA<^A>A<vA>^A<A>A
<v<A>>^AAAvA^A<vA<AA>>^AvAA<^A>A<v<A>A>^AAAvA<^A>A<vA>^A<A>A

<<vAA>A>^AAvA<^A>AvA^A<<vA>>^AAvA^A<vA>^AA<A>A<<vA>A>^AAAvA<^A>A
<<vAA>A>^AAvA<^A>AvA^A<<vA>>^AAvA^A<vA>^AA<A>A<<vA>A>^AAAvA<^A>A

<v<A  >>^AA <vA  <A >>^AA vAA <^A >A <vA>^A<A>A<vA>^A<A>A<v<A>A>^AAvA<^A>A
<<vAA >A    >^AA vA <^A   >AA vA  ^A <vA>^A<A>A<vA>^A<A>A<<vA>A>^AAvA<^A>A


<AA v<AA >>^A
^^<<A           >A  >A vvA
4               5   6  A

<v<A>>^AvA^A<vA<AA>>^AAvA<^A>AAvA^A<vA>^AA<A>A<v<A>A>^AAAvA<^A>A
<<vA>>^AvA^A<<vAA>A>^AAvA<^A>AAvA^A<vA>^AA<A>A<<vA>A>^AAAvA<^A>A

#
# <vA<AA>>^AvAA<^A>A<v<A>>^AvA^A<vA>^A<v<A>^A>AAvA^A<v<A>A>^AAAvA<^A>A
# <v<A>>^AAAvA^A<vA<AA>>^AvAA<^A>A<v<A>A>^AAAvA<^A>A<vA>^A<A>A
# <v<A>>^A<vA<A>>^AAvAA<^A>A<v<A>>^AAvA^A<vA>^AA<A>A<v<A>A>^AAAvA<^A>A
# <v<A>>^AA<vA<A>>^AAvAA<^A>A<vA>^A<A>A<vA>^A<A>A<v<A>A>^AAvA<^A>A
# <v<A>>^AvA^A<vA<AA>>^AAvA<^A>AAvA^A<vA>^AA<A>A<v<A>A>^AAAvA<^A>A

#%%
dir_keys(v_to_number('A',0))
v_to_number(8,'A')
v_to_dir('A', '<')

code = '029A'
num_buttons = [k*i for k, i in dir_keys(v_to_number(0,2)).items() if i]
num_buttons

num_dirs = ''.join(''.join([k*i for k, i in dir_keys(v_to_button(s,e,key_dict=NUM_KEY)).items() if i]+['A'])
                   for s,e  in pairwise('A'+code))
num_dirs

dirs_dirs = ''.join(''.join([k*i for k, i in
                 dir_keys(v_to_button(s,e)).items() if i]+['A'])
        for s,e  in pairwise('A'+num_dirs)
    )

dirs_dirs_dirs = ''.join(''.join([k*i for k, i in
                 dir_keys(v_to_button(s,e)).items() if i]+['A'])
        for s,e  in pairwise('A'+dirs_dirs)
    )

dirs_dirs_dirs
button_seqence(['A']+code, key_dict=NUM_KEY)
button_seqence(button_seqence(button_seqence(code, key_dict=NUM_KEY)))


'<<vAA>A>^AvAA<^A>A<<vA>>^AvA^A<vA>^A<<vA>^A>AAvA^A<<vA>A>^AAAvA<^A>A'
'<vA<AA>>^AvAA<^A>A<v<A>>^AvA^A<vA>^A<v<A>^A>AAvA^A<v<A>A>^AAAvA<^A>A'
'<<vA>>^A<A>AvA<^AA>A<vAAA>^A'
'v<<A>>^A<A>AvA<^AA>A<vAAA>^A'
# <vA <AA >>^A vAA <^A >A    <v<A>>^AvA^A<vA>^A<v<A>^A>AAvA^A<v<A>A>^AAAvA<^A>A
# v   <<  A    >>  ^   A     <A >A           vA <^AA >A          <vAAA >^A
# <            A             ^  A            >  ^^   A           vvv   A
# 0                          2               9                   A
