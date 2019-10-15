import matplotlib.pyplot as plt
filename = ("lirik_indo_raya.txt")
with open(filename,"r") as f:
  string = f.read()
  string_list = string.split()
  string_dict = dict()
  print(string_list)
  for word in string_list:
    if word in string_dict:
      string_dict[word] = string_dict[word] + 1
    else:
      string_dict[word] = 1
  print(string_dict)
  count_list = string_dict.values()
  indentation = list(range(1, len(count_list) + 1))
  b1 = plt.barh(indentation, sorted(count_list),color = ("green"))
  # barh to make the chart horizontal
  plt.yticks(indentation, string_list)
  #  ticks is the information of value in x
  plt.title("histogram data")
  plt.xlabel("frequencies")
  plt.ylabel("lyrics")
  keylist = []
  valuelist = []
  sorteddict = {}
  for key,values in string_dict.items():
    valuelist.append(values)

  for value in sorted(valuelist,reverse = True):
    for key in string_dict:
      if (value == string_dict[key]):
        sorteddict[key] = value
  print(sorteddict)

  plt.show()

import matplotlib.pyplot as plt
# dict = {'rowin' : '4', 'sunny' : '7', 'jeco' : '4'}
#
# keylist = []
# valuelist = []
# sorteddict = {}
#
# for key,values in dict.items():
#     valuelist.append(values)
#
# for value in sorted(valuelist,reverse=True):
#     for key in dict:
#         if value == dict[key]:
#             sorteddict[key] = value
#
# print(sorteddict)
