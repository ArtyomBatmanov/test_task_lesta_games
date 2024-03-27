## Тестовое задание
Реализовать веб-приложение. В качестве интерфейса сделать страницу с формой для загрузки текстового файла, после загрузки и обработки файла отображается таблица с 50 словами с колонками:
- слово
- tf, сколько раз это слово встречается в тексте
- idf, обратная частота документа 

Вывод упорядочить по уменьшению idf.

Ознакомиться с tfidf можно здесь: [tfidf](https://ru.wikipedia.org/wiki/TF-IDF). 

P.S. Не совсем было понятно как вычисляется IDF, в описании сказано: 
"Вычислим IDF как десятичный логарифм отношения количества всех документов к количеству документов, содержащих слово «слово»"
Как я понял, у нас только один документ, поэтому я построил вычисления так: 
"Вычислим IDF как десятичный логарифм отношения количества всех слов к количеству слов «слово»"