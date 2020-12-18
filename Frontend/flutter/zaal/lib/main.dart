import 'package:flutter/material.dart';
import 'package:provider/provider.dart';


import 'package:zaal/ui/homepage.dart';
import 'package:zaal/ui/login_screen.dart';
import 'package:zaal/ui/register_screen.dart';
import 'package:zaal/ui/splash_screen.dart';

import 'blocs/authentication.dart';
import 'data/user.dart';

void main() {
  runApp(MyApp());
}

class MyApp extends StatelessWidget {
  @override
  Widget build(BuildContext context) {
    Future<User> getUserData() => UserPreferences().getUser();

    return MultiProvider(
      providers: [
        ChangeNotifierProvider(create: (_) => AuthProvider()),
        ChangeNotifierProvider(create: (_) => UserProvider()),
      ],
      child: MaterialApp(
          title: 'Flutter Demo',
          theme: ThemeData(
            primarySwatch: Colors.blue,
            visualDensity: VisualDensity.adaptivePlatformDensity,
          ),
          home: FutureBuilder(
              future: getUserData(),
              builder: (context, snapshot) {
                switch (snapshot.connectionState) {
                  case ConnectionState.none:
                  case ConnectionState.waiting:
                    return CircularProgressIndicator();
                  default:
                    if (snapshot.hasError)
                      return Text('Error: ${snapshot.error}');
                    else if (snapshot.data.token == null)
                      return Login();
                    else
                      UserPreferences().removeUser();
                    return MyHomePage();
                }
              }),
          routes: {
            '/home': (context) => MyHomePage(),
            '/login': (context) => Login(),
            '/register': (context) => Register(),
          }),
    );
  }
}