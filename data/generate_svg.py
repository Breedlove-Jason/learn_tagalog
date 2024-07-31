import svgwrite
import os


def create_svg_from_text(word, filename):
    directory = "../static/svg/"  # Ensure this path is correct
    os.makedirs(directory, exist_ok=True)  # Ensure the directory exists
    full_path = os.path.join(directory, f"{filename}.svg")
    dwg = svgwrite.Drawing(full_path, profile="tiny")

    # Create a text element without style in constructor
    text_element = dwg.text(word, insert=(10, 20), fill="white")

    # Apply style using the 'update' method
    text_element.update(
        {"font-size": "20px", "font-family": "'Permanent Marker', cursive"}
    )

    # Add the styled text element to the drawing
    dwg.add(text_element)

    dwg.save()


def process_words(file_path):
    import pandas as pd  # Ensure pandas is installed

    # Read the CSV file into a DataFrame
    df = pd.read_csv(file_path)

    # Iterate through each row in the DataFrame
    for index, row in df.iterrows():
        tagalog_word = row["Tagalog"]  # Adjust the column name as necessary
        english_word = row["English"]  # Adjust the column name as necessary
        create_svg_from_text(tagalog_word, f"tagalog_{index}")
        create_svg_from_text(english_word, f"english_{index}")


if __name__ == "__main__":
    translations_path = "translations.csv"  # Adjust this path if needed
    process_words(translations_path)
