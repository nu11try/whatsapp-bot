import json
import os


class Config:
    def __init__(self):
        self.root_path = os.getcwd()
        self.__config_file_path = f'{self.root_path}/config.json'

        with open(self.__config_file_path, 'r') as file:
            self.__config_file = json.JSONDecoder().decode(file.read())

    def get_time_range(self):
        return {
            'min': self.__config_file['time_range']['min'],
            'max': self.__config_file['time_range']['max']
        }
