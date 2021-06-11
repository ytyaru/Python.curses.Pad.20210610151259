#!/usr/bin/env python3
# coding: utf8
import os, curses

# 複数のnewpad()を使う。なぜかoverlay()できない。最後にrefresh()したpadが描画されるようだ。
class Main:
    def __init__(self, screen, msg, color_index=1):
        self.__screen = screen
        self.__msg = msg
        self.__color_index = color_index
        self.__init_cursor()
        self.__init_color_pair()
        self.__pad1 = curses.newpad(curses.LINES, curses.COLS)
        self.__pad2 = curses.newpad(curses.LINES, curses.COLS)
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
        self.__pad1.addstr(0, 0, 'win1----', curses.A_REVERSE | curses.color_pair(1))
        self.__pad1.refresh(0,0,0,0,curses.LINES,curses.COLS)
        self.__pad2.addstr(1, 0, 'win2----', curses.A_REVERSE | curses.color_pair(2))
        self.__pad2.refresh(0,0,0,0,curses.LINES,curses.COLS)
#        self.__pad2.overlay(self.__pad1)
#        self.__pad1.overlay(self.__pad2)
        """
        self.__pad1.noutrefresh(0,0,0,0,curses.LINES,curses.COLS)
        self.__pad2.noutrefresh(0,0,0,0,curses.LINES,curses.COLS)
        self.__pad1.addstr(0, 0, 'win1', curses.A_REVERSE | curses.color_pair(1))
        self.__pad2.addstr(1, 0, 'win2', curses.A_REVERSE | curses.color_pair(2))
        self.__pad2.overlay(self.__pad1)
        curses.doupdate()
        """

        """
        self.__pad1.addstr(0, 0, 'win1----', curses.A_REVERSE | curses.color_pair(1))
        self.__pad1.refresh(0,0,0,0,curses.LINES,curses.COLS)
        self.__pad2.addstr(1, 0, 'win2----', curses.A_REVERSE | curses.color_pair(2))
        self.__pad2.refresh(0,0,0,0,curses.LINES,curses.COLS)
        self.__pad2.overlay(self.__pad1)
        """
    def __input(self):
#        self.__screen.getkey()
        self.__pad1.keypad(True)
        self.__pad1.getkey()
#        self.__pad2.keypad(True)
#        self.__pad2.getkey()


if __name__ == "__main__":
    curses.wrapper(Main, 'Hello', color_index=2)

