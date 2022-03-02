#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# pip install git+https://github.com/HonamSong/printlogger.git

from printlogger.printlogger import *


def test_logging_print():
    logging = Logging(log_mode="print")
    logging.custom("aa", "yellow", "info", is_view=True)

    logging = Logging(log_mode="print", view_line_num=True,)
    logging.custom("show line num test", "yellow", "info", is_view=True)

    logging = Logging(log_mode="print", view_line_num=True, view_func_name=True)
    logging.custom("show line num + func test", "yellow", "info", is_view=True)

    logging = Logging(log_mode="print", view_line_num=True, view_func_name=True, view_file_name=True )
    logging.custom("show line num + func test + file name ", "yellow", "info", is_view=True)

    logging = Logging(log_mode="print", view_line_num=True, view_file_name=True)
    logging.custom("show line num  + file name ", "yellow", "info", is_view=True)

    logging = Logging(log_mode="print", view_file_name=True)
    logging.custom("show file name ", "yellow", "info", is_view=True)

    logging = Logging(log_mode="print", view_func_name=True, view_file_name=True)
    logging.custom("show func test + file name ", "yellow", "info", is_view=True)

    logging = Logging(log_mode="print", view_line_num=True,view_func_name=True, view_file_name=True, log_time_format="%Y-%m-%d_%H:%M" )
    logging.custom("log time format test", "yellow", "info", is_view=True)

    del logging


def test_logging_write():
    logging = Logging(log_mode="write")
    pmsg = "ba"
    print(f'only write : {pmsg}')
    logging.custom(pmsg, "yellow", "info", is_view=True)

    logging = Logging(log_mode="write", log_path="./test")
    pmsg = "bb"
    print(f'only write : {pmsg} ,  log_path = ./test')
    logging.custom(pmsg, "yellow", "info", is_view=True)

    logging = Logging(log_mode="write", log_path="./test", log_file="bc.log")
    pmsg = "bc"
    print(f'only write : {pmsg} ,  log_path = ./test , log_file = bc.log')
    logging.custom(pmsg, "yellow", "info", is_view=True)

    pmsg = "bd"
    logging = Logging(log_mode="write", log_path=f"./test/test_{pmsg}", log_file=f"{pmsg}.log", view_line_num=True)
    print(f'only write : {pmsg} ,  log_path = ./test/test_{pmsg} , log_file = {pmsg}.log / show line num')
    logging.custom(pmsg, "yellow", "info", is_view=True)

    pmsg = "be"
    logging = Logging(log_mode="write", log_path=f"./test/test_{pmsg}", log_file=f"{pmsg}.log", view_line_num=True, view_func_name=True)
    print(f'only write : {pmsg} ,  log_path = ./test/test_{pmsg} , log_file = {pmsg}.log / show line num + func')
    logging.custom(pmsg, "yellow", "info", is_view=True)

    pmsg = "bf"
    logging = Logging(log_mode="write", log_path=f"./test/test_{pmsg}", log_file=f"{pmsg}.log", view_line_num=True, view_file_name=True)
    print(f'only write : {pmsg} ,  log_path = ./test/test_{pmsg} , log_file = {pmsg}.log / show line num + file')
    logging.custom(pmsg, "yellow", "info", is_view=True)

    pmsg = "bg"
    logging = Logging(log_mode="write", log_path=f"./test/test_{pmsg}", log_file=f"{pmsg}.log", view_line_num=True, view_func_name=True, view_file_name=True)
    print(f'only write : {pmsg} ,  log_path = ./test/test_{pmsg} , log_file = {pmsg}.log / show line num + func + file')
    logging.custom(pmsg, "yellow", "info", is_view=True)

    pmsg = "bi"
    logging = Logging(log_mode="write", log_path=f"./test/test_{pmsg}", log_file=f"{pmsg}.log", view_line_num=True, view_func_name=True, view_file_name=True, log_time_format="%Y-%m-%d_%H:%M_%S")
    print(f'only write : {pmsg} ,  log_path = ./test/test_{pmsg} , log_file = {pmsg}.log / log time format')
    logging.custom(pmsg, "yellow", "info", is_view=True)


def test_logging_all():
    logging = Logging(log_mode="all")
    pmsg = "ca"
    print(f'all mode : {pmsg}')
    logging.custom(pmsg, "yellow", "info", is_view=True)

    logging = Logging(log_mode="all", log_path="./test")
    pmsg = "cb"
    print(f'all mode : {pmsg} ,  log_path = ./test')
    logging.custom(pmsg, "yellow", "info", is_view=True)

    logging = Logging(log_mode="all", log_path="./test", log_file="bc.log")
    pmsg = "cc"
    print(f'all mode : {pmsg} ,  log_path = ./test , log_file = bc.log')
    logging.custom(pmsg, "yellow", "info", is_view=True)

    pmsg = "cd"
    logging = Logging(log_mode="all", log_path=f"./test/test_{pmsg}", log_file=f"{pmsg}.log", view_line_num=True)
    print(f'all mode : {pmsg} ,  log_path = ./test/test_{pmsg} , log_file = {pmsg}.log / show line num')
    logging.custom(pmsg, "yellow", "info", is_view=True)

    pmsg = "ce"
    logging = Logging(log_mode="all", log_path=f"./test/test_{pmsg}", log_file=f"{pmsg}.log", view_line_num=True, view_func_name=True)
    print(f'all mode : {pmsg} ,  log_path = ./test/test_{pmsg} , log_file = {pmsg}.log / show line num + func')
    logging.custom(pmsg, "yellow", "info", is_view=True)

    pmsg = "cf"
    logging = Logging(log_mode="all", log_path=f"./test/test_{pmsg}", log_file=f"{pmsg}.log", view_line_num=True, view_file_name=True)
    print(f'all mode : {pmsg} ,  log_path = ./test/test_{pmsg} , log_file = {pmsg}.log / show line num + file')
    logging.custom(pmsg, "yellow", "info", is_view=True)

    pmsg = "cg"
    logging = Logging(log_mode="all", log_path=f"./test/test_{pmsg}", log_file=f"{pmsg}.log", view_line_num=True, view_func_name=True, view_file_name=True)
    print(f'all mode : {pmsg} ,  log_path = ./test/test_{pmsg} , log_file = {pmsg}.log / show line num + func + file')
    logging.custom(pmsg, "yellow", "info", is_view=True)

    pmsg = "ci"
    logging = Logging(log_mode="all", log_path=f"./test/test_{pmsg}", log_file=f"{pmsg}.log", view_line_num=True, view_func_name=True, view_file_name=True, log_time_format="%Y-%m-%d_%H:%M_%S")
    print(f'all mode : {pmsg} ,  log_path = ./test/test_{pmsg} , log_file = {pmsg}.log / log time format')
    logging.custom(pmsg, "yellow", "info", is_view=True)

    pmsg = "ci_error"
    logging = Logging(log_mode="all", log_path=f"./test/test_{pmsg}", log_file=f"{pmsg}.log", view_line_num=True, view_func_name=True, view_file_name=True, log_time_format="%Y-%m-%d_%H:%M_%S")
    print(f'all mode : {pmsg} ,  log_path = ./test/test_{pmsg} , log_file = {pmsg}.log / log time format')
    logging.custom(pmsg, "yellow", "error", is_view=True)

    pmsg = "ci_debug"
    logging = Logging(log_mode="all", log_path=f"./test/test_{pmsg}", log_file=f"{pmsg}.log", view_line_num=True, view_func_name=True, view_file_name=True, log_time_format="%Y-%m-%d_%H:%M_%S")
    print(f'all mode : {pmsg} ,  log_path = ./test/test_{pmsg} , log_file = {pmsg}.log / log time format')
    logging.custom(pmsg, "yellow", "debug", is_view=True)

    pmsg = "ci_warnning"
    logging = Logging(log_mode="all", log_path=f"./test/test_{pmsg}", log_file=f"{pmsg}.log", view_line_num=True, view_func_name=True, view_file_name=True, log_time_format="%Y-%m-%d_%H:%M_%S")
    print(f'all mode : {pmsg} ,  log_path = ./test/test_{pmsg} , log_file = {pmsg}.log / log time format')
    logging.custom(pmsg, "yellow", "warn", is_view=True)

    pmsg = "ci_warnning"
    logging = Logging(log_mode="all", log_path=f"./test/test_{pmsg}", log_file=f"{pmsg}.log", view_line_num=True, view_func_name=True, view_file_name=True, log_time_format="%Y-%m-%d_%H:%M_%S.%f")
    print(f'all mode : {pmsg} ,  log_path = ./test/test_{pmsg} , log_file = {pmsg}.log / log time format')
    logging.custom(pmsg, "yellow", "warn", is_view=True)


def test_log_info():
    pmsg = "info_test_aa"
    logging = Logging(log_mode="all", log_path=f"./test/test_{pmsg}", log_file=f"{pmsg}.log", view_line_num=True, view_func_name=True, view_file_name=True)
    print(f'all mode : {pmsg} ,  log_path = ./test/test_{pmsg} , log_file = {pmsg}.log / log time format')
    logging.info(pmsg, is_view=True)

    pmsg = "info_test_ab"
    logging = Logging(log_mode="all", log_path=f"./test/test_{pmsg}", log_file=f"{pmsg}.log", view_line_num=True, view_func_name=True, view_file_name=True, view_log=False)
    print(f'all mode : {pmsg} ,  log_path = ./test/test_{pmsg} , log_file = {pmsg}.log / log time format, view_log=False')
    logging.info(pmsg, is_view=True)

    pmsg = "info_test_ab"
    logging = Logging(log_mode="all", log_path=f"./test/test_{pmsg}", log_file=f"{pmsg}.log", view_line_num=True, view_func_name=True, view_file_name=True)
    print(f'all mode : {pmsg} ,  log_path = ./test/test_{pmsg} , log_file = {pmsg}.log / log time format')
    logging.info(pmsg, is_view=False)


def test_log_warn():
    pmsg = "warn_test_aa"
    logging = Logging(log_mode="all", log_path=f"./test/test_{pmsg}", log_file=f"{pmsg}.log", view_line_num=True, view_func_name=True, view_file_name=True)
    print(f'all mode : {pmsg} ,  log_path = ./test/test_{pmsg} , log_file = {pmsg}.log / log time format')
    logging.warn(pmsg, is_view=True)

    pmsg = "warn_test_ab"
    logging = Logging(log_mode="all", log_path=f"./test/test_{pmsg}", log_file=f"{pmsg}.log", view_line_num=True, view_func_name=True, view_file_name=True, view_log=False)
    print(f'all mode : {pmsg} ,  log_path = ./test/test_{pmsg} , log_file = {pmsg}.log / log time format, view_log=False')
    logging.warn(pmsg, is_view=True)

    pmsg = "warn_test_ab"
    logging = Logging(log_mode="all", log_path=f"./test/test_{pmsg}", log_file=f"{pmsg}.log", view_line_num=True, view_func_name=True, view_file_name=True)
    print(f'all mode : {pmsg} ,  log_path = ./test/test_{pmsg} , log_file = {pmsg}.log / log time format')
    logging.warn(pmsg, is_view=False)


def test_log_error():
    pmsg = "error_test_aa"
    logging = Logging(log_mode="all", log_path=f"./test/test_{pmsg}", log_file=f"{pmsg}.log", view_line_num=True, view_func_name=True, view_file_name=True)
    print(f'all mode : {pmsg} ,  log_path = ./test/test_{pmsg} , log_file = {pmsg}.log / log time format')
    logging.error(pmsg, is_view=True)

    pmsg = "error_test_ab"
    logging = Logging(log_mode="all", log_path=f"./test/test_{pmsg}", log_file=f"{pmsg}.log", view_line_num=True, view_func_name=True, view_file_name=True, view_log=False)
    print(f'all mode : {pmsg} ,  log_path = ./test/test_{pmsg} , log_file = {pmsg}.log / log time format, view_log=False')
    logging.error(pmsg, is_view=True)

    pmsg = "error_test_ab"
    logging = Logging(log_mode="all", log_path=f"./test/test_{pmsg}", log_file=f"{pmsg}.log", view_line_num=True, view_func_name=True, view_file_name=True)
    print(f'all mode : {pmsg} ,  log_path = ./test/test_{pmsg} , log_file = {pmsg}.log / log time format')
    logging.error(pmsg, is_view=False)


def test_log_debug():
    pmsg = "debug_test_aa"
    logging = Logging(log_mode="all", log_path=f"./test/test_{pmsg}", log_file=f"{pmsg}.log", view_line_num=True, view_func_name=True, view_file_name=True)
    print(f'all mode : {pmsg} ,  log_path = ./test/test_{pmsg} , log_file = {pmsg}.log / log time format')
    logging.debug(pmsg, is_view=True)

    pmsg = "debug_test_ab"
    logging = Logging(log_mode="all", log_path=f"./test/test_{pmsg}", log_file=f"{pmsg}.log", view_line_num=True, view_func_name=True, view_file_name=True, view_log=False)
    print(f'all mode : {pmsg} ,  log_path = ./test/test_{pmsg} , log_file = {pmsg}.log / log time format, view_log=False')
    logging.debug(pmsg, is_view=True)

    pmsg = "debug_test_ab"
    logging = Logging(log_mode="all", log_path=f"./test/test_{pmsg}", log_file=f"{pmsg}.log", view_line_num=True, view_func_name=True, view_file_name=True)
    print(f'all mode : {pmsg} ,  log_path = ./test/test_{pmsg} , log_file = {pmsg}.log / log time format')
    logging.debug(pmsg, is_view=False)

    pmsg = "debug_test_ab"
    logging = Logging(log_mode="all", log_path=f"./test/test_{pmsg}", log_file=f"{pmsg}.log", view_line_num=True, view_file_name=True)
    print(f'all mode : {pmsg} ,  log_path = ./test/test_{pmsg} , log_file = {pmsg}.log / log time format')
    logging.debug(pmsg)


def main():

    test_logging_print()
    print("\n\n\n\n\n\n")
    test_logging_write()
    print("\n\n\n\n\n\n")

    test_logging_all()
    print("\n\n\n\n\n\n")

    test_log_info()
    print("\n\n\n\n\n\n")
    test_log_warn()
    print("\n\n\n\n\n\n")
    test_log_error()
    print("\n\n\n\n\n\n")
    test_log_debug()
    print("\n\n\n\n\n\n")


if __name__ == '__main__':
    main()

