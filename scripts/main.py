import re
from functools import cached_property

class TextAnalyzer:
    def __init__(self, text):
        self.text = text
        self.special_chars = "!\"#$%&'()*+,-./:;<=>?@[\\]^_`{|}~±÷×€£¥¢₹₽₴«»„"''"'’…·•¶§©®™°µ†‡◊"
        self.numbers = '0123456789'
    
    def clean_text(self): # чистка текста (спец. символы)
        return ''.join(char for char in self.text if char not in self.special_chars)
            
    def remove_spaces(self, text=None): # чистка текста (пробелы)
        target = text if text is not None else self.text
        return target.replace(' ', '')

    def remove_numbers(self, text=None):  # чистка текста (цифры)
        target = text if text is not None else self.text
        return ''.join(char for char in target if char not in self.numbers)

    def all_transforms(self): # все вышеперечисленные
        cleaned = self.clean_text()
        no_numbers = self.remove_numbers(cleaned)
        return self.remove_spaces(no_numbers)       

    def split_sentences(self): # разделение на предложения
        pattern = r'(?<=[.!?])\s+(?=[А-ЯA-Z])|(?<=[.!?])$'
        sentences = re.split(pattern, self.text)
        return [s.strip() for s in sentences if s.strip()]

    def split_words(self): # разделение на слова
        cleaned = self.remove_numbers(self.clean_text())
        return [word for word in cleaned.split() if word]

    def count_chars(self): # подсчёт символов (с пробелами и со всеми трансформациями)
        return len(self.all_transforms()), len(self.text)
    
    def aux_count_chars(self): # подсчёт символов каждого преобразования
        return len(self.clean_text()), len(self.remove_numbers()), len(self.remove_spaces())

    def count_words(self): # подсчёт слов
        return len(self.split_words())

    def count_sentences(self): # подсчёт предложений
        return len(self.split_sentences())

    def extract_emails(self): # поиск email-адресов
        email_pattern = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
        return set(re.findall(email_pattern, self.text))

    def extract_urls(self): # извлечение ссылок extract_urls()
        url_pattern = r'https?://(?:[-\w.]|(?:%[\da-fA-F]{2}))+[/\w\.-]*\??[/\w\.-=&%]*|www\.[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}[/\w\.-]*\??[/\w\.-=&%]*'
        return set(re.findall(url_pattern, self.text))
    
    def extract_phone_numbers(self): # поиск телефонных номеров 
        phone_number_pattern = r'(?:\+\d{1,3}[\s-]?)?\(?\d{1,4}\)?[\s-]?(?:\d[\s-]?){6,12}\d'
        return set(re.findall(phone_number_pattern, self.text))

    def extract_context(self, search_target): # поиск предложений, содержащих искомую строку
        sentences = self.split_sentences()
        return [sentence for sentence in sentences if search_target in sentence]

    def sentence_index_range(self, search_target): # возвращает количество и позиции всех вхождений строки 
        mentions = []
        start = 0
        while True:
            pos = self.text.find(search_target, start)
            if pos == -1:
                break
            mentions.append(pos)
            start = pos + 1
        return len(mentions), mentions