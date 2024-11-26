t_ = (45,4.5,'hai',(4,5),[2.5,3],45)
print(t_)
print(type(t_))

'single value'
t_1 = (45,)
print(t_,type(t_1))

'constructor'
print(tuple())
print(tuple('Python'),
      tuple([4,5.3,True]),
      tuple({'a','b','c'}),
      tuple({3:45,False:45}))
