# ща как напишем каунт векторайзер, ух!

from typing import List


class CountVectorizer:

    """Класс CountVectorizer принимает на вход список слов и возвращает матрицу
    частоты встречаемых слов"""

    def __init__(self, delimiter: str = ' '):
        self.delimiter = delimiter
        self.features = []

    def get_feature_names(self) -> List[str]:

        """Получаем список слов, встречающихся в текстах"""

        if len(self.features) == 0:
            raise ValueError('Input list is empty')
        return self.features

    def _corpus_features(self, corpus: List[str]) -> None:

        """Добавляем в список слов новые слова, ранее не встречавшиеся"""

        new_features = []
        old_features = [
            word.lower() for text in corpus
            for word in text.split()
        ]

        for word in old_features:
            if word not in new_features:
                new_features.append(word)
        self.features = list(new_features)

    def _get_word_matrix(self, corpus: List[str]) -> List[List[int]]:

        """Создаем матрицу частоты встречаемых слов"""

        word_matrix = []
        for text in corpus:
            word_matrix.append([])
            for word in self.features:
                feature_names = [word.lower() for word in text.split()]
                word_matrix[-1].append(feature_names.count(word))
        return word_matrix

    def fit_transform(self, corpus) -> List[List[int]]:

        """Создает матрицу частоты вхождений слов на основе исходного текста"""

        self._corpus_features(corpus)
        word_matrix = self._get_word_matrix(corpus)
        return word_matrix


if __name__ == '__main__':

    corpus = [
        'Crock Pot Pasta Never boil pasta again',
        'Pasta Pomodoro Fresh ingredients Parmesan to taste'
    ]
    vectorizer = CountVectorizer()
    count_matrix = vectorizer.fit_transform(corpus)

    print(count_matrix)
    assert count_matrix == [[1, 1, 2, 1, 1, 1, 0, 0, 0, 0, 0, 0],
                            [0, 0, 1, 0, 0, 0, 1, 1, 1, 1, 1, 1]]

    feature_list = vectorizer.get_feature_names()
    assert feature_list == ['crock', 'pot', 'pasta', 'never',
                            'boil', 'again', 'pomodoro', 'fresh',
                            'ingredients', 'parmesan', 'to', 'taste']
    print(feature_list)
