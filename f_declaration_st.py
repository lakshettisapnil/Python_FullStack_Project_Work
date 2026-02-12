def student_data(info):
    print(f'name: {info[0]}')
    print(f'Course: {info[1]}')
    print(f'year: {info[2]}')
    print('------------end------------')



data = [['Swapnil', 'PFs', '2025'],
        ['abhi', 'DA', '2025'], 
        ['siri', 'DSA', '2025'],
        ['ravi', 'Java', '2026']      
]
for i in data:
    student_data(i)

