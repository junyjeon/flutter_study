### 문서 주석

```dart
/// 문서주석
```

## 비동기 언어

## Null Safety Spread Operator Collection If Hot Reroading JIT AOT JavaScript 컴파일

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
${}
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

### 함수는 메소드를 포함하는 더 큰 개념. 메소드는 클래스에 정의된 함수.

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

## dart의 프라이빗 변수(private variable)는 같은 파일 내에서만 접근 가능한 변수.

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

## extends 상속

클래스의 기능을 다른 클래스에 부여
그냥 갖다 쓰는거
별 다른 특이점 없음

## super는 상속한 부모 클래스를 칭한다.

BoyGroup(String name, int mebersCount,) :
super(name, membersCount); // 상속받은 클래스의 생성자. 멤버 변수 초기화.
==
BoyGroup(super.name, super.membersCount,); //똑같음

편의성 프로그램 확장 프로그램 투명 창 위에 템플릿 windows stikcy note

## 오버라이드

부모 클래스, 인터페이스에 정의된 매소드(함수)를 재정의 할 때 사용
상속해준 클래스의 함수를 재정의해 사용
@override
void sayName(){
//내용 변경
}

## 인터페이스 implements

공통으로 필요한 기능을 정의만 해두는 역할.
typedef에 함수의 이름과 반환형, 매개변수만 정의해두는 것 처럼

인터페이스는 class의 멤버변수와 기능의 템플릿을 정의만 해두어서 메모리에 저장해두면 다른 메모리가 복사해 가져다 쓰는거지

class GirlGroup implements Idol {}
클래스의 기능을 모두 재정의 하게 된다.

## impeller 3.13 2023/08/13 버전인 flutter에서는 impeller렌더링 기술을 사용한다. https://docs.flutter.dev/perf/impeller

## WebAssembly(Wasm)는 C, C++, Rust 등의 저수준 언어로 작성된 코드를 웹에서 실행할 수 있게 하는 이진 명령어 형식입니다. 이를 통해 C++로 작성된 코드를 WebAssembly 모듈로 컴파일하고, 웹 브라우저나 Flutter 웹 앱에서 로드하여 실행할 수 있습니다.

## flutter performance 체크 가능. https://docs.flutter.dev/tools/devtools/performance#import-and-export

## flutter 최신 소식은 모두 여기에. https://medium.com/flutter

## skia라는 게 있는데 잘 모르겠다. 나중에 공부 https://skia.org/docs/user/modules/canvaskit/

## 디자이너들에게 보여줄 Template APP들 https://flutterawesome.com/tag/challenge/ https://flutterawesome.com/tag/apps-tag/

## Google이 사용하고 알려주는 flutter 정보들. https://io.google/2023/program/intl/ko/?q=workshop,codelab,learning-pathway,demo
