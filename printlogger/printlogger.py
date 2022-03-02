# -*- coding: utf-8 -*-

import os
import re
import inspect
from datetime import datetime
from termcolor import cprint


def todaydate(date_type=None):
    if date_type is None:
        return '%s' % datetime.now().strftime("%Y%m%d")
    elif date_type == "md":
        return '%s' % datetime.now().strftime("%m%d")
    elif date_type == "file":
        return '%s' % datetime.now().strftime("%Y%m%d_%H%M")
    elif date_type == "hour":
        return '%s' % datetime.now().strftime("%H")
    elif date_type == "ms":
        return '%s' % datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f")[:-3]
    elif date_type == "log_ms":
        return '%s' % datetime.now().strftime("%Y%m%d%H%M%S")
    elif date_type == "ms_text":
        return '%s' % datetime.now().strftime("%Y%m%d-%H%M%S%f")[:-3]


def check_dir(dir_path, create_if_missing=False, is_view=False):
    if os.path.isdir(dir_path):
        return_msg = f'Directory is exists :{dir_path}'
        return_color = "green"
        return_value = True
    else:
        if create_if_missing:
            os.makedirs(dir_path, exist_ok=True)
            return_msg = f'Create a Directory :{dir_path}'
            return_color = "green"
            return_value = True
        else:
            return_msg = f'Directory "{dir_path}" does not found'
            return_color = "red"
            return_value = False

    if is_view:
        cprint(return_msg, return_color)

    return return_value


def check_file(filename, path=None, is_view=False):
    return_msg = None
    return_color = None

    orig_path = os.getcwd()
    if path:
        if check_dir(path):
            # path Change
            os.chdir(path)

    if os.path.isfile(filename):
        if path:
            os.chdir(orig_path)
            return_msg = f'File is exists : {filename}'
            return_color = 'green'
            return_value = os.path.join(path, filename)
        else:
            return_value = os.path.join(filename)
    else:
        return_msg = f'Check file : file "{filename}" does Not Found is file'
        return_color = 'red'
        return_value = False

    if is_view:
        cprint(return_msg, return_color)

    return return_value


class Color:
    # TextColor : Text Color
    grey = 'grey'
    red = 'red'
    green = 'green'
    yellow = 'yellow'
    blue = 'blue'
    magenta = 'magenta'
    cyan = 'cyan'
    white = 'white'


class BgColor:
    """
    :param BackGroundColor(Text highlights) : Text Background color
    """
    grey = 'on_grey'
    red = 'on_red'
    green = 'on_green'
    yellow = 'on_yellow'
    blue = 'on_blue'
    magenta = 'on_magenta'
    cyan = 'on_cyan'
    white = 'on_white'


class Logging:
    def __init__(self, log_path=None, log_file=None,
                 log_color='green', log_level='INFO', log_mode='print',
                 log_time_format=None, view_log=True,
                 view_line_num=False, view_file_name=False, view_func_name=False):

        self.log_path = log_path
        self.log_file = log_file
        self.log_color = log_color
        self.log_level = log_level
        self.log_mode = log_mode
        self.log_time_format = log_time_format
        self.view_log = view_log
        self.view_line_num = view_line_num
        self.view_file_name = view_file_name
        self.view_func_name = view_func_name

        """
        :param log_path: logging path name
        :param log_file: logging file name
        :param log_color: print log color
        :param log_level: logging level
        :param log_mode: print or loging mode ( default : print), [all|write|print]
        :param log_time_format : logging Time format (default YYYY-MM-DD HH:MM:SS:3F)
        :param view_view : View logs by default [True|False]
        :param view_line_num : view logs in line number
        :param view_func_name : view logs in function name + line number
        :param view_file_name : view logs in file name + line number
        :return:
        """

        if self.log_mode == 'write' or self.log_mode == 'all':
            if self.log_path:
                check_dir(self.log_path, create_if_missing=True)
            else:
                base_path = os.path.dirname(inspect.getmodule(inspect.stack()[1][0]).__file__)
                self.log_path = os.path.join(base_path, "logs")
                check_dir(self.log_path, create_if_missing=True)

            if not self.log_file:
                filename = os.path.basename(inspect.getmodule(inspect.stack()[1][0]).__file__)
                self.log_file = filename.replace('.py', f'_{todaydate()}.log')

            self.log_file = os.path.join(self.log_path, self.log_file)

    def log_write(self, log_msg, log_file=None):
        if not log_file:
            log_file = self.log_file
        print(f'log file : {log_file}')
        if log_msg:
            with open(log_file, 'a+') as f:
                f.write(f'{log_msg}\n')

    def log_level_check(self, color, level):
        # r_color = None
        # r_level = None

        if level.upper() == 'WARNING' or level.upper() == 'WARN':
            r_color = Color.magenta
            r_level = 'WARN'
        elif level.upper() == 'ERROR' or level.upper() == 'ERR':
            r_color = Color.red
            r_level = 'ERROR'
        elif level.upper() == 'DEBUG':
            r_color = Color.yellow
            r_level = 'DEBUG'
        else:
            r_color = color if color else self.log_color
            r_level = self.log_level

        return r_color, r_level

    def log_time_format_check(self):
        # log_time = None
        if self.log_time_format:
            format_regex = re.compile('\\.([0-9]){4,8}')
            log_time = datetime.now().strftime(self.log_time_format)
            if format_regex.search(log_time):
                log_time = datetime.now().strftime(self.log_time_format)[:-3]
        else:
            log_time = todaydate(date_type="ms")

        return log_time

    def log_print_format_check(self, level, call_name=None):
        # print_fmt = None

        if call_name:
            print_fmt = f'[{self.log_time_format_check()}] [{level.upper():5}] | {call_name}'
        else:
            print_fmt = f'[{self.log_time_format_check()}] [{level.upper():5}]'

        return print_fmt

    def call_check(self, line_num=None, func_name=None, file_name=None):
        call_source_location = line_num

        if self.view_func_name and not self.view_file_name:
            call_source_location = call_source_location.replace(call_source_location.split('.')[0], func_name)

        if self.view_file_name and not self.view_func_name:
            call_source_location = call_source_location.replace(call_source_location.split('.')[0], file_name)

        if self.view_func_name and self.view_file_name:
            call_name = f'{file_name}.{func_name}'
            call_source_location = call_source_location.replace(call_source_location.split('.')[0], call_name)

        if not self.view_line_num and not self.view_func_name and not self.view_file_name:
            call_source_location = False

        return call_source_location

    def printing(self, msg, color, is_view=True):
        if not self.view_log:
            is_view = False

        if self.log_mode == 'print' or not self.log_mode or self.log_mode == 'all':
            if is_view:
                cprint(msg, color)

        if self.log_mode == 'write' or self.log_mode == 'all':
            self.log_write(msg,)

    def custom(self, msg, color=None, level=None, is_view=True,):
        # user custom log

        # call line number , function name, file name
        # call_file_name = inspect.getmodule(inspect.stack()[1][0]).__file__.split("/")[-1]
        # call_func_name = inspect.currentframe().f_back.f_code.co_name
        call_source_location = self.call_check(
            line_num=f'line.{inspect.currentframe().f_back.f_lineno}',
            func_name=inspect.currentframe().f_back.f_code.co_name,
            file_name=inspect.getmodule(inspect.stack()[1][0]).__file__.split("/")[-1]
        )
        color, level = self.log_level_check(color, level)
        print_msg = f'{self.log_print_format_check(level, call_name=call_source_location)} | {msg}'

        self.printing(print_msg, color, is_view=is_view)

    def info(self, msg, is_view=True,):
        call_source_location = self.call_check(
            line_num=f'line.{inspect.currentframe().f_back.f_lineno}',
            func_name=inspect.currentframe().f_back.f_code.co_name,
            file_name=inspect.getmodule(inspect.stack()[1][0]).__file__.split("/")[-1]
        )

        print_msg = f'{self.log_print_format_check("info", call_name=call_source_location)} | {msg}'
        self.printing(print_msg, "green", is_view=is_view)

    def warn(self, msg, is_view=True,):
        call_source_location = self.call_check(
            line_num=f'line.{inspect.currentframe().f_back.f_lineno}',
            func_name=inspect.currentframe().f_back.f_code.co_name,
            file_name=inspect.getmodule(inspect.stack()[1][0]).__file__.split("/")[-1]
        )

        print_msg = f'{self.log_print_format_check("warn", call_name=call_source_location)} | {msg}'
        self.printing(print_msg, "magenta", is_view=is_view)

    def error(self, msg, is_view=True,):
        call_source_location = self.call_check(
            line_num=f'line.{inspect.currentframe().f_back.f_lineno}',
            func_name=inspect.currentframe().f_back.f_code.co_name,
            file_name=inspect.getmodule(inspect.stack()[1][0]).__file__.split("/")[-1]
        )

        print_msg = f'{self.log_print_format_check("error", call_name=call_source_location)} | {msg}'
        self.printing(print_msg, "red", is_view=is_view)

    def debug(self, msg, is_view=True,):
        call_source_location = self.call_check(
            line_num=f'line.{inspect.currentframe().f_back.f_lineno}',
            func_name=inspect.currentframe().f_back.f_code.co_name,
            file_name=inspect.getmodule(inspect.stack()[1][0]).__file__.split("/")[-1]
        )

        print_msg = f'{self.log_print_format_check("debug", call_name=call_source_location)} | {msg}'
        self.printing(print_msg, "yellow", is_view=is_view)

