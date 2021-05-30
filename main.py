import json
import os
import click


def battle_ground_card():
    card_data = list()
    dirpath = os.path.dirname(__file__)
    filepath = os.path.join(dirpath, "card_info/data.json")
    f = open(filepath, "r", encoding='utf-8')
    data = json.loads(f.read())
    for i in data:
        if i['type'] == 'MINION':
            card_data.append(i)
    for i in card_data:
        print(i)
    print(len(card_data))

def main():
    @click.option('--bye', is_flag=True, help="say good bye.")
    @click.option('--hello', is_flag=True, help="say hello.")
    @click.option('-v', '--version', is_flag=True, help="Show version of this program.")
    @click.argument('name')
    @click.command()

if __name__ == '__main__':
    battle_ground_card()
    #main()

