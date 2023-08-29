void main() {
  var name = 'nico';
  print("Hello! ${name.toUpperCase()}!");

  Dictionary dict = Dictionary();
  dict.add('apple', '사과');
  print(dict.get('apple'));
  dict.showAll();
  dict.delete('apple');
  dict.showAll();
  dict.showAll();
  dict.count();
  dict.upsert('banana', '바나나');
  dict.showAll();
  dict.exists('banana');
  dict.bulkAdd({'cherry': '체리', 'durian': '두리안'});
  dict.showAll();
  dict.bulkDelete(['durian', 'banana']);
  dict.showAll();
}

class Dictionary {
  Map<String, String> words = {};

  void add(word, definition) {
    words[word] = definition;
  }

  String get(word) {
    return words[word]!;
  }

  void delete(word) {
    words.remove(word);
  }

  void update(word, definition) {
    words[word] = definition;
  }

  void showAll() {
    words.forEach((key, value) {
      print('$key : $value');
    });
  }

  void count() {
    print(words.length);
  }

  void upsert(word, definition) {
    words.containsKey(word) ? update(word, definition) : add(word, definition);
  }

  void exists(word) {
    words.containsKey(word) ? print('Exist') : print('Does not exist.');
  }

  void bulkAdd(Map<String, String> newWord) {
    words.addAll(newWord);
  }

  void bulkDelete(List<String> deleteWord) {
    for (var word in deleteWord) {
      words.remove(word);
    }
  }
}
