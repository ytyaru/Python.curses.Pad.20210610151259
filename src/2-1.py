#!/usr/bin/env python3
# coding: utf8
import os, curses

# なぜかsubpad()がうまく描画できない。
# curses.newpad()を使う。
# 注意: screen.refresh(), screen.getkey()を使うとダメ。上書きされてしまって何も表示されなくなる。pad.refresh(), pad.getkey()を使うべき。
class Main:
    def __init__(self, screen, msg, color_index=1):
        self.__screen = screen
        self.__msg = msg
        self.__color_index = color_index
        self.__init_cursor()
        self.__init_color_pair()
        self.__pad = curses.newpad(curses.LINES * 3, curses.COLS * 3)
        self.__subpad = self.__pad.subpad(curses.LINES * 3-1, curses.COLS * 3-1)
        self.__draw()
        self.__input()
    def __init_cursor(self): curses.curs_set(0)
    def __init_color_pair(self):
        if not curses.has_colors(): raise Exception('このターミナルは色を表示できません。')
        if not curses.can_change_color(): raise Exception('このターミナルは色を変更できません。')
        curses.use_default_colors()
        for i in range(1, curses.COLORS):
            curses.init_pair(i, i, curses.COLOR_BLACK)
    def __draw(self):
#        self.__pad.addstr('newpad')
#        self.__subpad.move(2, 1)
#        self.__subpad.setsyx(2, 1)
        try:
            for i in range(1, curses.COLORS):
#                self.__pad.addstr(str(i).rjust(3), curses.A_REVERSE | curses.color_pair(i))
                self.__subpad.addstr(str(i).rjust(3), curses.A_REVERSE | curses.color_pair(i))
        except curses.error: pass
#        except curses.ERR: pass
        self.__pad.addstr(7, 0, self.__msg, curses.A_REVERSE | curses.color_pair(self.__color_index))
#        self.__subpad.addstr(7, 0, self.__msg, curses.A_REVERSE | curses.color_pair(self.__color_index))
#        self.__pad.refresh(0, 0, 0, 0, curses.LINES-1, curses.COLS-1)
        self.__subpad.refresh(0, 0, 0, 0, curses.LINES-1, curses.COLS-1)
    def __input(self):
        self.__pad.keypad(True)
        self.__pad.getkey()


if __name__ == "__main__":
    curses.wrapper(Main, 'Hello', color_index=2)

