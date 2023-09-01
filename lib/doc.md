### 문서 주석

```dart
/// 문서주석
```

## 비동기 언어

## Null Safety Spread Operator Collection If Hot Reroading(Ctrl + s) JIT AOT JavaScript 컴파일

## JIT AOT

JIT: Just In Time 핫 리로드 변경된 코드만 컴파일
AOT: Ahead of Time 배포할 때.

### 변수 타입

- `dynamic`: 변수 타입이 한 번 사용 후 고정되지 않음
- `const`: 빌드타임. 실행하지 않았을 때 확정 값
- `final`: 런타임. 실행될 때 확정 값
- List 메서드
  - `add()`: 값 추가
  - `where()`: 매개변수로 함수를 사용하며 일치하는 값은 유지, iterable 추상 클래스로 반환
  - `map()`: 매개변수로 함수를 사용하며 현재 값을 대체, iterable 추상 클래스로 반환
  - `reduce()`: 매개변수로 함수를 사용하며 값을 추가, list로 반환
  - `fold(초깃값, 람다식)`: `reduce()`와 같지만 list, iterable 반환 형식을 정할 수 있음

### Map, Set

- `Map`: iterable 반환
  var numbers = [1, 2, 3]; #List<int> numbers
  - addAll
    map1.addAll(map2);
  - forEach
    각각에 대한 함수 실행.
    map1.forEach((key, value)) {
    print('$key: $value'); //각 키밸류 출력
    }
- `Set`: 중복 없는 값들의 집합
  var numbers = {1, 2, 3}; #Set<int> numbers

```dart
Set.from(List);
toList();
.keys.toList();
.values.toList();
```

- 변수가 `null`을 가지려면 타입 뒤에 `?` 붙이기 (예: `double?`)

### 연산자

- `??`: 앞의 매개변수가 `null`일 때
- `is`: 타입 비교 연산자 (예: `is String`, `is! String`)

### Enum과 Switch 문

```dart
enum Status { approved, pending, rejected, }

Status status = Status.approved;

switch (status) {
  case Status.approved: break;
  case Status.pending: break;
  case Status.rejected: break;
  default: // 처리
}
```

## collection if/for

컬렉션 = List, Set, Map
collection if #특정 조건이 참인 경우에만 컬렉션에 항목을 포함
collection for #루프를 돌아 컬렉션에 항목을 포함

### 반복문

- `for`: `for (int number in numberList){ print(number); }`
- `do-while`:

  ```dart
  do {
    total += 1;
  } while(total < 10);
  ```

### 람다와 익명 함수

- 익명함수: `() { func }`
- 람다함수: `() => func`

### typedef

```dart
typedef hi = void func(int x, int y);

void sum(int x, int y) {
    x + y;
}
hi hello = sum;

hello(1, 2);
// -> 3
```

### 예외 처리 (try-catch)

```dart
try{
    // 실행 해보기
    throw // 에러 발생 시키기
}catch{
    // 에러 발생시
}
```

### 기타 키워드와 메서드

- `Timer`, `Duration`
- `duration`, `toString`, `split`, `substring`
- `await`, `async`, `Future`
- `jsonDecode`, `[]`, `{}`

### named constructor와 fromJson

```dart
WebtoonModel.fromJson(Map<String, dynamic> json)
  : title = json['title'],
    thumb = json['thumb'],
    id = json['id'];
```

### 트리와 위젯 관련 내용

- `BuildContext`: 트리 내의 위치에 대한 핸들
- `FutureBuilder`, `ListView()`, `clipBehavior: Clip.hardEdge`
- `Hero()`: 위젯 추가 후 tag만 같게 설정 (예: `tag: id`)

## Scafold

## widget.~~

data는 statefulwidget으로 전달되고
다른 클래스에 있다면 widget.data 를 사용해서 받아오기 가능

## Container / margin 마진 넣을 수 있음

## Url launcher

Android: android/app/src/main/AndroidManifest.xml
Ios: ios/Runner/Info.plist

## 이상한 케이스들

```
  var name = 'nico';

  '$name.toUpperCase()' -> '$name.toUpperCase()' 그대로
  '${$name.toUpperCase()}' -> 'nico'
```

```
//가능
void main(){
    num age = 18;
    age = 1.11;
}
```

```
//같음
//List<>
  var x = [true];
  List<bool> x = [true];
```

------------------------- 정리 -------------------------

### Null Safety

변수는 기본적으로 null이 될 수 없다. `int? digit`처럼 null이 될 수 있게 선언할 수 있다.

### Spread Operator (`...`)

컬렉션인 List, Set, Map을 다른 컬렉션에 삽입할 수 있다. `[...list1, ...set1]`와 같이 사용한다.

### Collection If와 For

컬렉션 내에서 조건부로 요소를 추가하거나 반복하여 요소를 추가할 수 있다.

### Hot Reloading

![Hot Reloading Icon](https://flutter.dev/assets/tools/vs-code/hot-reload@2x-4ba2b0d6b98e5c8a62b4f3e0b92f3a45f89fc369.png)
디버깅 중 앱을 다시 시작하지 않고 소스 코드의 변경 사항을 즉시 반영한다.

### JIT (Just-In-Time Compilation)

실시간으로 코드를 기계어로 변환하며, 컴파일러 최적화가 가능하다.

### AOT (Ahead-Of-Time Compilation)

미리 코드를 기계어로 변환하며, 컴파일러 최적화로 실행 속도를 향상시킨다.

### JavaScript 컴파일

Dart 코드를 웹 브라우저에서 실행할 수 있는 JavaScript로 완벽히 컴파일한다.

### 인스턴스(객체)는 생성된 클래스. Animal dog; -> 인스턴스

### 함수는 메소드를 포함하는 더 큰 개념. 메소드는 클래스에 정의된 함수

## named parameter

생성자(속성) : 멤버변수 = 매개변수

## named constructor

Idol(String name, int membersCount) // 네임드 파라미터(그냥 생성자)
: this.name = name, // ','로 여러개 처리
this.membersCount = membersCount;

//생성할때

- Idol.fromMap(Map<String, dynamic> map) //fromMap이라는 named 생성자. Idol.fromMap이라는 생성자를 만든거 같음.
  : this.name = map['name'],
  this.membersCount = map['membersCount'];
  ${}를 사용하면 하나 이상의 매개변수를 처리할 수 있다.

//사용할때

- Idol bts = Idol.fromMap({
  'name' = 'BTS',
  'membersCount' : 7,
  });

## dart의 프라이빗 변수(private variable)는 같은 파일 내에서만 접근 가능한 변수

```
class Idol {
var name; 변수
var \_name -> 프라이빗 변수
}
```

## int plus(int a, int b, [int? c = 1]) => a + b + (c ?? 0); plus(1,2) -> 4

## When do we use typedef?

When we want to create an alias for a type.

## getter, setter

- getter, setter 최근 객체지향 프로그래밍의 트렌드는 변수의 값을 불변성 특성으로 사용하기 때문에 세터는 거의 사용하지 않음.

```
String get name { // getter 프라이빗으로 선언된 _name 변수를 getter로 접근 가능
  return this._name;
}

set name(String name) { // setter
  this._name = name;
}

blackPink.name = '에이핑크' // setter
print(blackPink.name); // getter
```

# Dart에서는 클래스를 정의할 때 extends(상속), with(mixin), implements(인터페이스) 세 가지 키워드를 사용할 수 있다

```
class Bird extends Flyable with Swimmable implements Animal {

  @override
  void eat() => print('Eating');
}
```

class Bird extends Flyable with Swimmable implements Animal {
클래스 Bird는 Flyable의 모든 기능을 사용할 수 있고, Swimmable의

extends(상속)
하나만 상속 가능
Dart에선 @overriding 키워드를 생략하고 기능(생성자, 멤버변수, 메소드)을 오버라이딩 할 수 있다. 하지만 명시 하는게 공유 코드에서 좋을것임.

with(mixin)
여럿 상속 가능
생성자를 가질 수 없다.

implements(인터페이스)
인터페이스 ui
기능을 정의해둔다고 한다.
그냥 생성자, 멤버변수, 메소드의 템플릿을 정의 해둔다.

## extends 상속

클래스의 기능을 다른 클래스에 부여
class A extends B, C 여러개 상속 가능

## super는 상속한 부모 클래스를 칭한다

- BoyGroup(String name, int mebersCount,)
  : super(name, membersCount); // 상속받은 클래스의 생성자. 멤버 변수 초기화.
  ==

  BoyGroup(super.name, super.membersCount,); //똑같음

## 오버라이드

부모 클래스, 인터페이스에 정의된 매소드(함수)를 재정의 할 때 사용
상속해준 클래스의 함수를 재정의해 사용
@override
void sayName(){
//내용 변경
}

//인터페이스 -> 어떤 행동을 해야 한다.
//템플릿 -> 어떻게 해야한다.

## 인터페이스 implements

공통으로 필요한 기능을 정의만 해두는 역할.
typedef에 함수의 이름과 반환형, 매개변수만 정의해두는 것 처럼

인터페이스는 class의 멤버변수와 기능의 템플릿만 만들고 메모리에 저장해두면 다른 메모리가 복사해 쓰는거지

class GirlGroup implements Idol {}
모든 기능을 다시 정의 해야한다.

## 믹스인 Mixin //처음 보는 개념 > 혼합 코드?

원하는 함수(클래스 내 함수 (메소드))만 골라 사용할 수 있음. extend 대신 with로 사용

```
class Engine {
  void start() {
    print('Engine started');
  }
}

mixin CarMixin on Engine {
  void drive() {
    print('Driving');
  }
}

class Car extends Engine with CarMixin {
  // Car 클래스는 Engine을 상속받고 있으므로 CarMixin을 사용할 수 있습니다.
}

class Bicycle with CarMixin {
  // 컴파일 오류! Bicycle 클래스는 Engine을 상속받고 있지 않으므로 CarMixin을 사용할 수 없습니다.
}
```

## 추상 abstract

추상 메소드를 가질 수 있다.
자식 클래스는 추상 메소드를 다시 정의해야 한다.

class들. 기본 클래스, 인터페이스(멤버변수와 함수만 정의해둔 클래스)

## 추상, 인터페이스 차이

- 추상 클래스
  구현이 있는 메소드를 가질 수 있다.
  추상 클래스 하나만 상속받을 수 있다.
  공통된 기능을 재사용하고 확장성을 제공하는 데 사용됩니다.
- 인터페이스
  구현을 가질 수 없음
  여러 인터페이스를 불러올 수 있음
  인터페이스 내의 메소드를 모두 구현해야 함
  공통
  직접 인스턴스(객체)를 생성할 수 없음

## static

dart에서 스태틱은 클래스에 귀속된다.
static키워드는 인스턴스끼리 공유해야 하는 정보에 지정.
state를 대신 할 수 있어.
같은 클래스를 여러개 만들어면 static 클래스의 정보는 공유된다.
스태틱 변수는 this로 접근할 수 없다. 오류

## Cascade Operator

- ('..')
  인스턴스에서 속성, 멤버함수를 연속해 사용하는 기능이라는데 뭐지
  Idol blackpink = Idol('블랙핑크', 4)
  ..sayName()
  ..saymembersCount();
  이렇게 쓴대
  그냥 선언한 인스턴스의 메소드를 바로 실행한다.

## 제네릭

<>로 사용한다.

## 흔히 사용되는 제네릭 문자들

문자 | 설명
class Cache<T>{}
T T value; 변수 타입 표현
E List<E> 리스트 내부 요소 타입 표현
K Map<K, V> 키
V Map<K, V> 값

## impeller 3.13 2023/08/13 버전인 flutter에서는 impeller렌더링 기술을 사용한다. <https://docs.flutter.dev/perf/impeller>

## WebAssembly(Wasm)는 C, C++, Rust 등의 저수준 언어로 작성된 코드를 웹에서 실행할 수 있게 하는 이진 명령어 형식입니다. 이를 통해 C++로 작성된 코드를 WebAssembly 모듈로 컴파일하고, 웹 브라우저나 Flutter 웹 앱에서 로드하여 실행할 수 있습니다

## flutter performance 체크 가능. <https://docs.flutter.dev/tools/devtools/performance#import-and-export>

## flutter 최신 소식은 모두 여기에. <https://medium.com/flutter>

## skia라는 게 있는데 잘 모르겠다. 나중에 공부 <https://skia.org/docs/user/modules/canvaskit/>

## 디자이너들에게 보여줄 Template APP들 <https://flutterawesome.com/tag/challenge/> <https://flutterawesome.com/tag/apps-tag/> <https://flutterawesome.com/tag/templates/>

## Google이 사용하고 알려주는 flutter 정보들. <https://io.google/2023/program/intl/ko/?q=workshop,codelab,learning-pathway,demo>

## 상 받은 Wonderous 카피 해보자. 최고난이도

편의성 프로그램 확장 프로그램 투명 창 위에 템플릿 windows stikcy note

## 빌드 명령어 (size analysis tool)

flutter build apk --analyze-size (any host)
flutter build appbundle --analyze-size (any host)
flutter build ios --analyze-size (only macos host)
flutter build linux --analyze-size (only linux host)
flutter build macos --analyze-size (only macos host)
flutter build windows --analyze-size (only windows host)

## 폴더 구조에 정답은 없지만 일단 이 템플릿을 사용해보자

- screen 스크린 전체
- component 스크린을 구성하는데 공통으로 사용될 위젯
- model 모델들 모음
- const 상수 모음

## 플러터에서 지원하는 주변장치

센서, GPS, 카메라, 블루투스, 와이파이

//01 Splash Screen (로딩화면)
23/08/24 05:30 시작

나는 한 향수에 대한 리뷰에서 적절한 키워드들을 수집해서 데이터셋으로 만들거야.

이 데이터로 사용자가 알려준 키워드와 일치하는 향수들을 추천해주는 시스템을 만들려 하는데, 데이터를 수집하는 작업을 해줘.

아래처럼 각 항목 별로 특정 키워드나 문구를 기반으로 분류해줘.
전반적인 느낌:

키워드: '전반적', '느낌', '향기', '인상'
예시: "이 향수의 전반적인 느낌은 상쾌하다."
탑노트:

키워드: '처음', '시작', '탑노트', '시작향'
예시: "처음 맡았을 때의 느낌은 시트러스 계열이다."
미들노트:

키워드: '중간', '미들노트', '본향'
예시: "어느정도 시간이 지나니 꽃향이 느껴진다."
바텀노트:

키워드: '마지막', '바텀노트', '마무리향'
예시: "향이 사라지기 전에는 우디한 느낌이 남는다."
잔향:

키워드: '잔향', '남은 향기', '마지막 향'
예시: "잔향이 상쾌하게 남아 좋다."
지속력:

키워드: '지속', '오래간다', '지속력'
예시: "이 향수는 하루 종일 지속된다."
유사향수:

키워드: '비슷한 향수', '유사', '리마인드'
예시: "이 향수는 [브랜드명]의 [향수명]과 비슷하다."
비고:

키워드: '기타', '추가', '비고'
예시: "가격대비 퀄리티가 좋다."
긍정/부정:

긍정 키워드: '좋다', '만족', '추천'
부정 키워드: '별로', '실망', '아쉽다'
예시: "이 향수는 정말 좋다. 다만 가격이 조금 비싸다."

---

[context]
한 향수 리뷰를 분석하여 각 항목별로 키워드를 추출합니다. 추출한 키워드는 다른 사용자가 제공한 키워드와 비슷한 키워드를 가진 향수를 찾아 추천해줄 시스템을 만들기 위해 존재합니다.

[task]
향수 리뷰에서 [constraints]에 나열된 키워드들을 기반으로 해당 키워드를 포함하는 문장을 찾아주세요. 그리고 그 문장에서 주요 단어들을 추출해주세요.

[constraints]
전반적인 느낌: 키워드 - '전반적', '느낌', '향기', '인상'
탑노트: 키워드 - '처음', '시작', '탑노트', '시작향'
미들노트: 키워드 - '중간', '미들노트', '본향'
바텀노트: 키워드 - '마지막', '바텀노트', '마무리향'
잔향: 키워드 - '잔향', '남은 향기', '마지막 향'
지속력: 키워드 - '지속', '오래간다', '지속력'
유사향수: 키워드 - '비슷한 향수', '유사', '리마인드'
비고: 키워드 - '기타', '추가', '비고'
긍정/부정: 긍정 키워드 - '좋다', '만족', '추천', 부정 키워드 - '별로', '실망', '아쉽다'

향수 리뷰는 감정, 느낌, 향의 진행 과정, 지속 시간 등 다양한 정보를 포함하고 있습니다.

[extra]
추출한 주요 단어들을 JSON 형식으로 출력해주세요. 각 항목별로 주요 단어들을 리스트 형태로 제공해주세요. 예:

```json
{
  "탑노트": ["상쾌한", "무화과", "싱그러운"],
  ...
}
```

주요 단어나 문구의 빈도를 분석하여 반복적으로 등장하는 키워드를 주목해주세요.

---


커밋 메세지

최초 공개
- Update
- version
- Bump
- Remove
- Delete
- Inital
- Add
- Tweak
- Merge
- Reorder
- Fix
이런 단어로 커밋메세지 작성

끝나고 잡학사전 챌린지 책읽기
프롬프트 끝?
애니메이션,
TF-IDF, BERT 섞어쓰기
