
def combs(a):
   if len(a) == 0:
      return [[]]
   cs = []
   for c in combs(a[1:]):
      cs += [c, c+[a[0]]]
   
   return cs
   
def generate_pair(input_list):
   temp_list = combs(input_list)
   empty_list =[]
   for x in temp_list:
      if len(x)>=2:
         empty_list.append(x)
   return empty_list

print(generate_pair([1,2,3,4]))


