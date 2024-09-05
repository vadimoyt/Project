lst = ['боб', 'дед', 'слово', 'шалаш', 'калаш', 'потом', 'реверс', 'комок', 'abccba']
print(list(filter(lambda x: list(reversed(x)) == list(x), lst)))

