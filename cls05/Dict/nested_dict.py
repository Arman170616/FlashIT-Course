#nested dictionary

dicst = {
    'name': 'Tom',
    'age': 20,
    'brithdate': '1999-01-01',
    'birthplace': 'beijing',
    'education': {
        'primary': 'beijing primary school',
        'middle': 'beijing middle school',
        'high': 'beijing high school'
    }
  }

# print(dicst)
print(dicst['education']['high'])   #beijing high school
print(dicst['education']['middle']) #beijing middle school
