#!/usr/bin/env python3
# -*- coding: utf-8 -*-


from printlogger.printlogger import *


def test_logging_print():
    logging = Logging(log_mode="print")
    logging.log_print("aa", "yellow","info", is_print=True)

    logging = Logging(log_mode="print", show_line_num=True,)
    logging.log_print("show line num test", "yellow","info", is_print=True)

    logging = Logging(log_mode="print", show_line_num=True,show_func_name=True )
    logging.log_print("show line num + func test", "yellow","info", is_print=True)

    logging = Logging(log_mode="print", show_line_num=True,show_func_name=True, show_file_name=True )
    logging.log_print("show line num + func test + file name ", "yellow","info", is_print=True)

    logging = Logging(log_mode="print", show_line_num=True,show_file_name=True )
    logging.log_print("show line num  + file name ", "yellow","info", is_print=True)

    logging = Logging(log_mode="print", show_file_name=True )
    logging.log_print("show file name ", "yellow","info", is_print=True)

    logging = Logging(log_mode="print", show_func_name=True, show_file_name=True )
    logging.log_print("show func test + file name ", "yellow","info", is_print=True)

    logging = Logging(log_mode="print", show_line_num=True,show_func_name=True, show_file_name=True ,log_time_format="%Y-%m-%d_%H:%M" )
    logging.log_print("log time format test", "yellow","info", is_print=True)

    del logging

def test_logging_write():
    logging = Logging(log_mode="write")
    pmsg = "ba"
    print(f'only write : {pmsg}')
    logging.log_print(pmsg, "yellow","info", is_print=True)

    logging = Logging(log_mode="write", log_path="./test")
    pmsg = "bb"
    print(f'only write : {pmsg} ,  log_path = ./test')
    logging.log_print(pmsg, "yellow","info", is_print=True)

    logging = Logging(log_mode="write", log_path="./test", log_file="bc.log")
    pmsg = "bc"
    print(f'only write : {pmsg} ,  log_path = ./test , log_file = bc.log')
    logging.log_print(pmsg, "yellow","info", is_print=True)

    pmsg = "bd"
    logging = Logging(log_mode="write", log_path=f"./test/test_{pmsg}", log_file=f"{pmsg}.log", show_line_num=True)
    print(f'only write : {pmsg} ,  log_path = ./test/test_{pmsg} , log_file = {pmsg}.log / show line num')
    logging.log_print(pmsg, "yellow","info", is_print=True)

    pmsg = "be"
    logging = Logging(log_mode="write", log_path=f"./test/test_{pmsg}", log_file=f"{pmsg}.log", show_line_num=True, show_func_name=True)
    print(f'only write : {pmsg} ,  log_path = ./test/test_{pmsg} , log_file = {pmsg}.log / show line num + func')
    logging.log_print(pmsg, "yellow","info", is_print=True)

    pmsg = "bf"
    logging = Logging(log_mode="write", log_path=f"./test/test_{pmsg}", log_file=f"{pmsg}.log", show_line_num=True, show_file_name=True)
    print(f'only write : {pmsg} ,  log_path = ./test/test_{pmsg} , log_file = {pmsg}.log / show line num + file')
    logging.log_print(pmsg, "yellow","info", is_print=True)

    pmsg = "bg"
    logging = Logging(log_mode="write", log_path=f"./test/test_{pmsg}", log_file=f"{pmsg}.log", show_line_num=True, show_func_name=True, show_file_name=True)
    print(f'only write : {pmsg} ,  log_path = ./test/test_{pmsg} , log_file = {pmsg}.log / show line num + func + file')
    logging.log_print(pmsg, "yellow","info", is_print=True)

    pmsg = "bi"
    logging = Logging(log_mode="write", log_path=f"./test/test_{pmsg}", log_file=f"{pmsg}.log", show_line_num=True, show_func_name=True, show_file_name=True, log_time_format="%Y-%m-%d_%H:%M_%S")
    print(f'only write : {pmsg} ,  log_path = ./test/test_{pmsg} , log_file = {pmsg}.log / log time format')
    logging.log_print(pmsg, "yellow","info", is_print=True)

def test_logging_all():
    logging = Logging(log_mode="all")
    pmsg = "ca"
    print(f'all mode : {pmsg}')
    logging.log_print(pmsg, "yellow","info", is_print=True)

    logging = Logging(log_mode="all", log_path="./test")
    pmsg = "cb"
    print(f'all mode : {pmsg} ,  log_path = ./test')
    logging.log_print(pmsg, "yellow","info", is_print=True)

    logging = Logging(log_mode="all", log_path="./test", log_file="bc.log")
    pmsg = "cc"
    print(f'all mode : {pmsg} ,  log_path = ./test , log_file = bc.log')
    logging.log_print(pmsg, "yellow","info", is_print=True)

    pmsg = "cd"
    logging = Logging(log_mode="all", log_path=f"./test/test_{pmsg}", log_file=f"{pmsg}.log", show_line_num=True)
    print(f'all mode : {pmsg} ,  log_path = ./test/test_{pmsg} , log_file = {pmsg}.log / show line num')
    logging.log_print(pmsg, "yellow","info", is_print=True)

    pmsg = "ce"
    logging = Logging(log_mode="all", log_path=f"./test/test_{pmsg}", log_file=f"{pmsg}.log", show_line_num=True, show_func_name=True)
    print(f'all mode : {pmsg} ,  log_path = ./test/test_{pmsg} , log_file = {pmsg}.log / show line num + func')
    logging.log_print(pmsg, "yellow","info", is_print=True)

    pmsg = "cf"
    logging = Logging(log_mode="all", log_path=f"./test/test_{pmsg}", log_file=f"{pmsg}.log", show_line_num=True, show_file_name=True)
    print(f'all mode : {pmsg} ,  log_path = ./test/test_{pmsg} , log_file = {pmsg}.log / show line num + file')
    logging.log_print(pmsg, "yellow","info", is_print=True)

    pmsg = "cg"
    logging = Logging(log_mode="all", log_path=f"./test/test_{pmsg}", log_file=f"{pmsg}.log", show_line_num=True, show_func_name=True, show_file_name=True)
    print(f'all mode : {pmsg} ,  log_path = ./test/test_{pmsg} , log_file = {pmsg}.log / show line num + func + file')
    logging.log_print(pmsg, "yellow","info", is_print=True)

    pmsg = "ci"
    logging = Logging(log_mode="all", log_path=f"./test/test_{pmsg}", log_file=f"{pmsg}.log", show_line_num=True, show_func_name=True, show_file_name=True, log_time_format="%Y-%m-%d_%H:%M_%S")
    print(f'all mode : {pmsg} ,  log_path = ./test/test_{pmsg} , log_file = {pmsg}.log / log time format')
    logging.log_print(pmsg, "yellow","info", is_print=True)

    pmsg = "ci_error"
    logging = Logging(log_mode="all", log_path=f"./test/test_{pmsg}", log_file=f"{pmsg}.log", show_line_num=True, show_func_name=True, show_file_name=True, log_time_format="%Y-%m-%d_%H:%M_%S")
    print(f'all mode : {pmsg} ,  log_path = ./test/test_{pmsg} , log_file = {pmsg}.log / log time format')
    logging.log_print(pmsg, "yellow","error", is_print=True)

    pmsg = "ci_debug"
    logging = Logging(log_mode="all", log_path=f"./test/test_{pmsg}", log_file=f"{pmsg}.log", show_line_num=True, show_func_name=True, show_file_name=True, log_time_format="%Y-%m-%d_%H:%M_%S")
    print(f'all mode : {pmsg} ,  log_path = ./test/test_{pmsg} , log_file = {pmsg}.log / log time format')
    logging.log_print(pmsg, "yellow","debug", is_print=True)

    pmsg = "ci_warnning"
    logging = Logging(log_mode="all", log_path=f"./test/test_{pmsg}", log_file=f"{pmsg}.log", show_line_num=True, show_func_name=True, show_file_name=True, log_time_format="%Y-%m-%d_%H:%M_%S")
    print(f'all mode : {pmsg} ,  log_path = ./test/test_{pmsg} , log_file = {pmsg}.log / log time format')
    logging.log_print(pmsg, "yellow","warn", is_print=True)

    pmsg = "ci_warnning"
    logging = Logging(log_mode="all", log_path=f"./test/test_{pmsg}", log_file=f"{pmsg}.log", show_line_num=True, show_func_name=True, show_file_name=True, log_time_format="%Y-%m-%d_%H:%M_%S.%f")
    print(f'all mode : {pmsg} ,  log_path = ./test/test_{pmsg} , log_file = {pmsg}.log / log time format')
    logging.log_print(pmsg, "yellow","warn", is_print=True)

def main():

    test_logging_print()
    print("\n\n\n\n\n\n")
    test_logging_write()
    print("\n\n\n\n\n\n")

    test_logging_all()
    print("\n\n\n\n\n\n")

if __name__ == '__main__':
    main()

