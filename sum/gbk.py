# -*-coding:utf-8-*-

SRC_DIR = r"C:\Users\19484\Documents\LDA\sum\new"
NEED_OPR_FILE_SUFFIX = [".cpp", ".h", ".txt"]

import os
import sys
import unicode


def get_dir_file_list_by_type(input_dir, suffix):
    all_files = []
    get_dir_all_files(input_dir, all_files)

    result_list = []
    for file in all_files:
        if file.endswith(suffix):
            result_list.append(file)
        elif file.endswith(suffix.upper()):
            result_list.append(file)

    result_list.sort()
    return result_list


def get_dir_all_files(input_dir, all_files):
    file_list = os.listdir(input_dir)
    for file in file_list:
        cur_path = os.path.join(input_dir, file)
        if os.path.isdir(cur_path):
            get_dir_all_files(cur_path, all_files)
        else:
            all_files.append(cur_path)

    return all_files


def convert(file):
    if not os.path.exists(file):
        print("not find file:%s" % file)
        return

    print("convert:%s" % file)

    notepad.open(file.encode('utf8'))
    notepad.runMenuCommand("Encoding", "Convert to UTF-8")
    notepad.save()
    notepad.close()

    bak_file_name = file + ".bak"
    if os.path.exists(bak_file_name):
        os.remove(bak_file_name)


def file_list_convert(file_list, out_enc="UTF-8"):
    for file_name in file_list:
        convert(file_name)


opr_src_dir = unicode(SRC_DIR, 'utf-8')

opr_file_type_info = "opr file type:[%s]" % ",".join(NEED_OPR_FILE_SUFFIX)

PRINT_INFO_PREFIX = "----------------------------------------------------------"
print("%sstart:%s%s" % (PRINT_INFO_PREFIX, opr_file_type_info, PRINT_INFO_PREFIX))

# opr_src_dir = os.getcwd()
# opr_src_dir = r"D:\svn\5.0\edpf\inc-test"


for suffix in NEED_OPR_FILE_SUFFIX:
    print("start opr file type:[%s]" % suffix)
    file_list = get_dir_file_list_by_type(opr_src_dir, suffix)
    file_list_convert(file_list)
    print("finish opr file type:[%s]" % suffix)

print("%send:%s%s" % (PRINT_INFO_PREFIX, opr_file_type_info, PRINT_INFO_PREFIX))