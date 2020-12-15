class User {
  final int id;
  final String type;
  final String title;

  User.fromJson(Map json)
      : id = json['entity_id'],
        type = json['entity_type'],
        title = json['title'];
}