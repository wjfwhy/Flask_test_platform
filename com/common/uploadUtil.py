# -*- coding: UTF-8 -*-
import logging
import os
import shutil

from com.common.getPath import Path


class FileUpload:
    def save_file(self, request_file, path):
        try:
            file = request_file
            file_name = file.filename
            upload_path = os.path.join(Path().get_current_path(), path,
                                       file_name)
            result = self.exists_path(upload_path, path, file_name)
            if result:
                upload_path = result[0]
                file_name = result[1]
            file.save(upload_path)
            file_size = os.path.getsize(upload_path)
            file_type = file.filename[file.filename.rfind('.') + 1:]
            return {'file_size': file_size, 'file_type': file_type, 'file_name': file_name, 'file_path': path}
        except Exception as e:
            logging.error(str(e))
            return None

    def delete_files(self, *args):
        try:
            for item in args:
                for data in item:
                    file_path = os.path.join(Path().get_current_path(), data[6],
                                             data[1])
                    os.remove(file_path)
            return True
        except Exception as e:
            logging.error(str(e))
            return False

    def exists_path(self, upload_path, path, file_name):
        if os.path.exists(upload_path):
            upload_path = os.path.join(Path().get_current_path(), path,
                                       'R' + file_name)
            file_name = 'R' + file_name
            return self.exists_path(upload_path, path, file_name)
        else:
            return [upload_path, file_name]

    def delete_reports(self, *args, path):
        try:
            for item in args:
                for data in item:
                    file_path = os.path.join(Path().get_current_path(), path,
                                             str(data[1]))
                    if os.path.isdir(file_path):
                        shutil.rmtree(file_path)
                    else:
                        os.remove(file_path)
            return True
        except Exception as e:
            logging.error(str(e))
            return False
