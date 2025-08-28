import codecs
import re
from typing import Optional

def delete_html_tags(html_file: str, result_file: str = 'cleaned.txt') -> None:


    with codecs.open(html_file, 'r', encoding='utf-8') as file:
        html_content: str = file.read()

    cleaned_text: str = re.sub(r'<[^>]+>', '', html_content)

    lines: list[str] = cleaned_text.splitlines()

    cleaned_lines: list[str] = [line.rstrip() for line in lines if line.strip()]

    with codecs.open(result_file, 'w', encoding='utf-8') as file:
        file.write('\n'.join(cleaned_lines))


if __name__ == "__main__":
    input_path = 'D:\\WinUsers\\UserCom\\Downloads\\draft.html'  # Replace your username and address with your own.
    output_path = 'D:\\WinUsers\\UserCom\\Downloads\\cleaned.txt'
    delete_html_tags(input_path, output_path)