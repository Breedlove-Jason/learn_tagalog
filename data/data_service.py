import pandas as pd

<<<<<<< HEAD

class DataManagement:

    def save_translations_to_csv(self, translation_dict, file_path):
        df = pd.DataFrame(
            list(translation_dict.items()), columns=["Tagalog", "English"]
        )
        df.to_csv(file_path, index=False)
=======
class DataManagement:
    def __init__(self, csv_file):
        self.csv_file = csv_file

    def read_translations_to_dict(self):
        """Reads translations from the CSV and creates a dictionary with associated audio paths."""
        try:
            df = pd.read_csv(self.csv_file)
            word_dict = {
                row['Tagalog']: {
                    'english': row['English'],
                    'audio': f"audio/{row['Tagalog']}.mp3"
                } for index, row in df.iterrows()
            }
            return word_dict
        except FileNotFoundError:
            print(f"No CSV file found at {self.csv_file}")
            return {}

    def save_translations_to_csv(self, translation_dict):
        """Saves translations and audio paths to CSV from a dictionary."""
        data = [{
            'Tagalog': key,
            'English': value['english'],
            'Audio': value['audio']
        } for key, value in translation_dict.items()]
        df = pd.DataFrame(data)
        df.to_csv(self.csv_file, index=False)
        print(f"Translations saved to {self.csv_file}")

    def update_or_add_translation(self, tagalog, english):
        """Updates or adds a new translation and associated audio path to the CSV."""
        df = pd.read_csv(self.csv_file)
        if tagalog in df['Tagalog'].values:
            df.loc[df['Tagalog'] == tagalog, 'English'] = english
        else:
            new_row = {
                'Tagalog': tagalog,
                'English': english,
                'Audio': f"audio/{tagalog}.mp3"
            }
            df = df.append(new_row, ignore_index=True)
        df.to_csv(self.csv_file, index=False)
        print(f"Updated translations saved to {self.csv_file}")

>>>>>>> a91b21e (tagalog audio files, test files)
