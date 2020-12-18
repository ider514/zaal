import 'package:flutter/material.dart';
import 'package:zaal/data/user.dart';

class Profile extends StatefulWidget {
  @override
  _ProfileState createState() => _ProfileState();
}

class _ProfileState extends State<Profile> {

  

  @override
  Widget build(BuildContext context) {
    void doLogout() {
    UserPreferences().removeUser();
    Navigator.pushReplacementNamed(context, '/login');
  }
    return Container(
      child: RaisedButton(child: Text("logout"),
      onPressed: doLogout,),
    );
  }
}