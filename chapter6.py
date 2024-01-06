# alien = {'color': 'green', 'points':5}
# print(alien['color'])
# print(alien['points'])
#
# alien['x'] = 0
# alien['y'] = 1
#
# del alien['x']
# print(alien)

# favorite = {
#     'jen':'python',
#     'sarah':'c',
#     'edward':'rust',
#     'phil':'python',
# }
# # for key,value in favorite.items():
# #     print(f"\nkey:{key}")
# #     print(f"value:{value}")
# for language in set(favorite.values()):
#     print(language.title())

# rivers = {
#     'nile' : 'egypt',
#     'yang' : 'china',
#     'missibi' : 'usa',
# }
# for river_name in rivers.keys():
#     print(river_name)
#
# for river_c in rivers.values():
#     print(river_c)

#嵌套

aliens = []
for alien_number in range(30):
    new_alien = {
        'color' : 'green',
        'name' : 'bob',
    }
    aliens.append(new_alien)
#创建一个alien列表 每个元素是一个字典

for alien in aliens[:3]:
    if alien['color'] == 'green':
        alien['color'] = 'yellow'
        alien['name'] = 'nancy'

print(aliens)