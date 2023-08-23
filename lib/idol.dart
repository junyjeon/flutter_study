class Idol {
  final String name;
  final int membersCount;

  Idol(this.name, this.membersCount);

  void sayName() {
    print('Hello, I am $name.');
  }

  void sayMembersCount() {
    print('We are $membersCount members.');
  }
}

class BoyGroup extends Idol {
  BoyGroup(
    String name,
    int membersCount,
  ) : super(
          name,
          membersCount,
        );

  @override
  void sayName() {
    print('Hello, I am $name.');
  }
}
