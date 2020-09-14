import zipfile
import os
import shutil


def unzip(file_name):
    unzip_format = zipfile.is_zipfile(file_name)
    if unzip_format:
        zip_file = zipfile.ZipFile(file_name)
        file_list = file_name.split('/')
        file_list[-1] = 'CheckInfoWorkSpace'
        file_path = '/'.join(file_list)
        if os.path.isdir(file_path):
            shutil.rmtree(file_path)
        os.mkdir(file_path)
        for names in zip_file.namelist():
            zip_file.extract(names, file_path + '/')
        zip_file.close()
    else:
        print('Need Zip Format, Please Check!!!')
    return file_path


def format_str(target_str):
    target_str = target_str.replace('=', '')
    target_str = target_str.replace('*MV', '*0.001')
    target_str = target_str.replace('*MA', '*0.001')
    target_str = target_str.replace('*UV', '*0.000001')
    target_str = target_str.replace('*UA', '*0.000001')
    target_str = target_str.replace('*V', '*1')
    target_str = target_str.replace('*A', '*1')
    target_str = target_str.replace('*NS', '*1')
    target_str = target_str.replace('*US', '*1000')
    target_str = target_str.replace('*MS', '*1000000')
    target_str = target_str.replace('*GHZ', '*1')
    target_str = target_str.replace('*MHZ', '*0.001')
    target_str = target_str.replace('*KHZ', '*0.000001')

    return target_str
