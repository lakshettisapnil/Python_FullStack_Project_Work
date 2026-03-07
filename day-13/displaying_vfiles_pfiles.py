list_vs_ps = ['birthday.png', 'aniversary.mp4', 'marriage.png', 'haldi.png', 'election.mp4']
user_input = set(input("select the file name: ").split(','))
ph = set()
vd = set()
for i in list_vs_ps:
    if i.endswith('.png'):
        ph.add(i)
    else:
        vd.add(i)
print('Photos'.center(30,'-'))
for user in ph:
    if user in user_input:
        print(f'{user}-sent')
print('Videos'.center(30,'-'))
for user in vd:
    if user in user_input:
        print(f'{user}-sent')