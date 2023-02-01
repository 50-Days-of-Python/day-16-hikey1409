def sum_list(l):
  s = 0
  sdl=[]
  for i in l:
        if type(i) == list:
            sdl.extend(sum_list(i))
        else:
            sdl.append(i)
  for i in range(0,len(sdl)):
    s=sdl[i]+s
  # Write your logic here
  
  return s

