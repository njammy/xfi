import sys
import os

class TxtReader():

    @staticmethod
    def load_file(file_path: str):
        try:
            with open(file_path, 'r', encoding='utf-8', errors='replace') as file:
                lines = [line.strip() for line in file]
            return lines
        except FileNotFoundError:
            print(f"Error: File '{file_path}' not found.")
            return None
        except Exception as e:
            print(f"Error reading file '{file_path}': {e}")
            exit(1) 