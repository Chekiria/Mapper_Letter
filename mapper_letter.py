

mappers = [{"id_account":"159", "Name":"Kiria", "gender":"m"},{"id_account":"205", "Name":"Zhenia", "gender":"f"}]
result = [{'id':'159', 'remap':'8', 'check':'90'}, {'id':'205', 'remap':'7', 'check':'56'}]
remap = [{'id':'159', 'date':'08-11-18', 'check':'mfmfm mfmfm mfmfm mfmfm'}, {'id':'159', 'date':'08-11-19', 'check':'ltldo ltrl lerl'}]

for n in result:
    print('''Привет.
На этой неделе валидаторы проверили %s твоих проектов, из которых %s ремапов.
Процент ремапов - %s''' % (n.get('check'), n.get('remap'), round((int(n.get('remap'))/int(n.get('check'))*100),2)))
    print('Твои ремапы:')
if n.get('id')== remap.get('id'):
    print(remap.get('date'))

