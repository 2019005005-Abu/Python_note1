st={
    'name':'Rifat',
    'SystemId':'2019005005',
    'country':'Bangladesh'
    
    }

# iterate the dictionary
for key in st:print(key);
for value in st:print(value);
for i,j in st.items():print(i,'-',j);
# nestes d= dictioanry

nested_dic={
    'country':'Bangladesh',
    'capital':'Dhaka',
    'favporite_language':{
        'fronted_lang':['CSS','JS','React'],
        'backend_lang':['Python','Django','Flask']
    }
}

print(nested_dic);
keys=['a','b','c'];
values=10;
dictionary=st.fromkeys(keys,values);
print(dictionary);

k=['name','jobs','Jobs_type'];
v=['Rifat','SWE','Full stack developer']

d=dict.fromkeys(k,v);
print(d);

my__dict={
    'name':'Rifat',
    'age':25
}

my__dict.setdefault('name','unknown');
print(my__dict);
def function1(f_name,l_name):#Parameter
    return f'{f_name} {l_name} '
f1=function1('Abu Al Shahriar','Rifat');
print(f1);#Arguments

def fun (*args):
    print(args);
fun('Bangladesh');

def fun1(k1,k2,k3):
    print('flower',k1,k2,k3);
fun1(k1='Rose',k2='WaterLily',k3='merrygold');


#using known key worddef Fun2(**kw):
def Fun2(**kw):
    print('flower:', kw.get('flower', 'No flower specified'))
    print('fruits:', kw.get('fruits', 'No fruits specified'))

Fun2(flower='Lotus', fruits='Mango')


def Fun3(**kw):
    flowerIs='flower:',kw.get('flower','No flower');
    fruitsIs='fruits:',kw.get('fruits','No fruits');
    print(flowerIs);
    print(fruitsIs);
Fun3(flower='Lotus',fruits='Mango');

def CountryName(name='Japan'):
    print(f'My country name :',name);
CountryName();

