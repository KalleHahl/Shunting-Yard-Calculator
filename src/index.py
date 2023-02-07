from src.algorithms.postfix import to_postfix
from src.algorithms.count import count

while True:

    try:
        calc = input('\ncalculation: \n\n')
    except:
        print(f"\nerror with ^, make sure to press twice and then space")
        continue
    if calc == 'quit':
        break

    value = count(to_postfix(calc))
    print(f"\n= {value}\n")
