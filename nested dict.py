#nested dictionaries
employee_data={
    'E101':{'name':'lakshmi',
            'department':'IT',
            'salary':45000,
            'experience':3},
    'E102':{'name':'prasanna',
            'department':'HR',
            'salary':35000,
            'experience':2},
    'E103':{'name':'mani',
            'department':'software engineer',
            'salary':50000,
            'experience':4},
    'E104':{'name':'vasanthi',
            'department':'project manager',
            'salary':55000,
            'experience':5}}
print(len(employee_data))
#Display all employee records.
print(employee_data)
#Print the salary of employee E102.
print(employee_data['E102']['salary'])
#Update the salary of employee E103.
employee_data['E103']['salary']=60000
print(employee_data['E103'])
#Add a new employee E105.
employee_data['E105']={'name':'geetha',
                       'department':'marketing',
                       'salary':35000,
                       'experience':1}
print(employee_data)
#Delete employee E101.
del employee_data['E101']
print(employee_data)
#Print all employee IDs.
print(employee_data.keys())
#print all values in the data
print(employee_data.values())
#print market from marketing
print(employee_data['E105']['department'][:6])
print(employee_data['E105']['department'][::2])
employee_data.popitem()
print(employee_data)
print('project manager' in employee_data['E104'])
#get(),setdefault()
employee_data['E103'].get('branch')
print(employee_data['E103'])
employee_data['E103'].setdefault('branch',['cse','ece'])
print(employee_data['E103'])


