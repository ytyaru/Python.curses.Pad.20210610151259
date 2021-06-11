#!/usr/bin/env python3
# coding: utf8
import os, curses

# curses.doupdate()を使う。window.refresh()でも行われるため、２つ以上のwindowがないと効果がない。２つの窓を用意してみた。
class Main:
    def __init__(self, screen, msg, color_index=1):
        self.__screen = screen
        self.__msg = msg
        self.__color_index = color_index
        self.__x = 0
        self.__y = 0
        self.__init_cursor()
        self.__init_color_pair()
        self.__newpad = curses.newpad(curses.LINES*3, curses.COLS*3)
        self.__subpad1 = self.__newpad.subpad(curses.LINES*3, curses.COLS*3, 0, 0)
        self.__subpad2 = self.__newpad.subpad(curses.LINES*3, curses.COLS*3, 0, 0)
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
        try:
            for i in range(1, curses.COLORS):
                self.__subpad1.addstr(str(i).rjust(3), curses.A_REVERSE | curses.color_pair(i))
        except curses.ERR: pass
        self.__subpad2.addstr(7, 0, self.__msg, curses.A_REVERSE | curses.color_pair(self.__color_index))
        self.__newpad.refresh(self.__y,self.__x,0,0,curses.LINES-1, curses.COLS-1)
    def __input(self):
        self.__newpad.keypad(True)
        while True:
            key = self.__newpad.getch()
            if   curses.KEY_UP == key: self.__y -= 1 if 0 < self.__y else 0
            elif curses.KEY_DOWN == key: self.__y += 1 if  self.__y < self.__newpad.getmaxyx()[0] - curses.LINES else 0
            elif curses.KEY_LEFT == key: self.__x -= 1 if 0 < self.__x else 0
            elif curses.KEY_RIGHT == key: self.__x += 1 if self.__x < self.__newpad.getmaxyx()[1] - curses.COLS else 0
            else: break
            self.__newpad.refresh(self.__y,self.__x,0,0,curses.LINES-1, curses.COLS-1)
            curses.napms(5)

if __name__ == "__main__":
    curses.wrapper(Main, 'Hello', color_index=2)

