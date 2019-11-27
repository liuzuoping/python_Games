import numpy as np
import curses
import copy
from curses import wrapper
import os

stdscr = curses.initscr()
# 分数
score = 0
# 判断是否获胜
win = 0
#
FILENAME = 'out.npy'


# 是否更改棋盘


# 初始化
def init():
    # 初始化棋盘
    # 初始棋盘 2 或 4 的随机数字
    if FILENAME not in os.listdir():
        np.save(FILENAME, 0)
    init_board = choice(np.zeros((4, 4), dtype=np.int))
    return init_board


# 游戏进程
def game(board, stdscr, rscore):
    global score
    global change
    # curses.noecho()
    # 屏幕不显示用户输入的字符
    curses.noecho()
    while 1:
        # stdscr.getch()
        # 读取用户输入的字符
        order = stdscr.getch()

        # move()对用户移动的响应
        current_board, change = move(order, board)
        # change 为 1 随机产生 2 或 4
        if change:
            current_board = choice(board)

        # 打印棋盘
        print_board(stdscr, current_board, rscore)

        # 当棋盘被填满，判断是否游戏结束
        if (current_board != 0).all():
            fail(current_board)

        # win 为 1 打印获胜提示
        if win:
            stdscr.addstr('You win')


# 随机产生 2 或 4
def choice(board):
    udict = {}
    # 统计0的个数
    count = 0
    for i in range(4):
        for j in range(4):
            # board[i,j] 为 0
            # eg. {0:(1,3),1:(2,1),3:(3,2)}
            # 根据 key 可以获得元素 0 在棋盘上的位置
            if not board[i, j]:
                udict[count] = (i, j)
                count += 1
    # np.random.randint(0, count)
    # 产生 [0,count) 范围内的随机数
    random_number = np.random.randint(0, count)
    # np.random.choice([2,2,2,4])
    # 随机选取列表 [2,2,2,4] 中的元素
    two_or_four = np.random.choice([2, 2, 2, 4])
    # 更改棋盘上 0 元素为随机数
    board[udict[random_number]] = two_or_four
    return board


# 基础移动
def basic(board):
    global score
    global win
    # 以右移为基础移动

    for i in range(4):
        flag = 1
        while flag:
            flag = 0
            j = 2
            while j >= 0:
                if board[i, j] != 0:
                    if board[i, j + 1] == board[i, j]:
                        board[i, j + 1] = 2 * board[i, j]
                        if board[i, j + 1] == 2048:
                            win = 1
                        board[i, j] = 0
                        score += 100
                        flag = 1

                    elif board[i, j + 1] == 0:
                        temp = board[i, j]
                        board[i, j] = board[i, j + 1]
                        board[i, j + 1] = temp
                        flag = 1

                j -= 1
    return board


# 右移
def move_right(board):
    return basic(board)


# 上移
def move_up(board):
    # 逆置 + 转置
    board = board[::-1, ::-1].T
    board = basic(board)
    board = board[::-1, ::-1].T
    return board


# 左移
def move_left(board):
    # 逆置
    board = board[::-1, ::-1]
    board = basic(board)
    board = board[::-1, ::-1]
    return board


# 下移
def move_down(board):
    # 转置
    board = board.T
    board = basic(board)
    board = board.T
    return board


# 移动
def move(order, board):
    # ord 求码值
    global score
    global win
    change = 1
    tempboard = copy.deepcopy(board)

    # 退出游戏
    if order == ord('q'):
        save_score(score)
        exit()
    # 重置游戏
    elif order == ord('r'):
        win = 0
        save_score(score)
        score = 0
        stdscr.clear()
        wrapper(main)
    # 胜利后，只有退出和重置游戏
    elif win:
        change = 0
        newboard = tempboard
        return newboard, change
    # 上下左右移动
    elif order == ord('w'):
        newboard = move_up(board)
    elif order == ord('s'):
        newboard = move_down(board)
    elif order == ord('a'):
        newboard = move_left(board)
    elif order == ord('d'):
        newboard = move_right(board)

    # 按其他键程序不响应
    else:
        newboard = board

    if (newboard == tempboard).all():
        change = 0

    return newboard, change


# 游戏失败
def fail(board):
    # 判断是否失败
    global score
    diff1 = board[:, 1:] - board[:, :-1]
    diff2 = board[1:, :] - board[:-1, :]
    inter = (diff1 != 0).all() and (diff2 != 0).all()
    if inter:
        save_score(score)
        stdscr.addstr('You lose')


# # 排行榜
# def ranking(score):
#     rank_score = np.load(FILENAME)
#     if rank_score < score:
#         rank_score = score
#         np.save(FILENAME, rank_score)
#     return rank_score

# 加载最高分
def load_score():
    rank_score = np.load(FILENAME)
    return rank_score


# 保存最高分
def save_score(score):
    rscore = load_score()
    if score > rscore:
        np.save(FILENAME, score)


#
def compare_score(score, rscore):
    if score > rscore:
        rscore = score
    return rscore


# 打印棋盘
def print_board(stdscr, board, rscore):
    global score
    rscore = compare_score(score, rscore)
    # stdscr.clear()
    # 清除屏幕
    stdscr.clear()
    stdscr.addstr('得分：' + str(score) + '\n')
    stdscr.addstr('历史最高：' + str(rscore) + '\n')
    for i in range(4):
        stdscr.addstr('-' * 22 + '\n')
        for j in range(4):
            stdscr.addstr('|')
            if board[i, j]:
                stdscr.addstr('{:^4d}'.format(board[i, j]))
            else:
                stdscr.addstr('    '.format())
        stdscr.addstr('|')
        stdscr.addstr('\n')
    stdscr.addstr('-' * 22 + '\n')


# 主程序

def main(stdscr):
    # 初始化程序
    init_board = init()
    rscore = load_score()
    # 打印棋盘
    print_board(stdscr, init_board, rscore)
    # 游戏主进程
    game(init_board, stdscr, rscore)


if __name__ == "__main__":
    wrapper(main)