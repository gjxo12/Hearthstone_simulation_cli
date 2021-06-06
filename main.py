import click
import sys
from pyfiglet import Figlet
# from clint.textui import puts, colored, indent


#필요한 내용: 내 미니언수, 상대 미니언 수, -> 사용할 카드? (name으로 받기?), 영웅 선택?(구현 매우 나중에)


@click.option('-v', '--version', is_flag=True, help="Show version of this program.")
#@click.command()
def main():
    f = Figlet(font='chartri') # cricket, slant,colossal chartri avatar
    print(f.renderText('H Simulator CLI'))
    print(sys.argv[1]) # 아군 미니언 수
    print(sys.argv[2]) # 상대 미니언 수

    # CLI clear?
    # ==============================================================
    # 아군 미언수에 따른 하수인 이름 공백으로, ex) 방패병? 노미,  ...
    # 상대 미니언수에 따른 하수인 이름 공백으로 ex) 위습, 고철로봇 ...
    # CLI clear
    # ==============================================================
    # 시뮬레이션

    #@click.command()

if __name__ == '__main__':
    #attle_ground_card()
    main()

