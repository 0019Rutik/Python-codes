call = {'aman':23,'rahul':24,'sandhya':26,'tan':21,'piyush':21,'dand':26,'rang':23}

#print(call.items())

call2 =call.copy()

#print(call2)
call2.update({'don':23})
call2.popitem()
print(call2)