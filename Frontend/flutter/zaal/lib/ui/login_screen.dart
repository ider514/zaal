import 'package:flutter/material.dart';
import 'package:provider/provider.dart';
import 'package:zaal/blocs/authentication.dart';
import 'package:zaal/data/user.dart';
import 'package:flushbar/flushbar.dart';

class Login extends StatefulWidget {
  @override
  _LoginState createState() => _LoginState();
}

class _LoginState extends State<Login> {
  final formKey = new GlobalKey<FormState>();

  String _username, _password;

  @override
  Widget build(BuildContext context) {
    AuthProvider auth = Provider.of<AuthProvider>(context);

    final usernameField = TextFormField(
      autofocus: false,
      // validator: validateEmail,
      onSaved: (value) => _username = value,
      decoration: InputDecoration(
          icon: Icon(Icons.mail), labelText: "Майл хаяг"),
    );

    final passwordField = TextFormField(
      autofocus: false,
      obscureText: true,
      validator: (value) => value.isEmpty ? "Нууц үг оруулна уу" : null,
      onSaved: (value) => _password = value,
      decoration: InputDecoration(
          icon: Icon(Icons.lock), labelText: "Нууц үг"),
    );

    var loading = Row(
      mainAxisAlignment: MainAxisAlignment.center,
      children: <Widget>[
        CircularProgressIndicator(),
        Text(" Холбогдож байна... Хүлээнэ үү")
      ],
    );

    final forgotLabel = Row(
      mainAxisAlignment: MainAxisAlignment.spaceBetween,
      children: <Widget>[
        FlatButton(
          padding: EdgeInsets.all(0.0),
          child: Text("Нууц үг мартсан?",
              style: TextStyle(fontWeight: FontWeight.w300)),
          onPressed: () {
//            Navigator.pushReplacementNamed(context, '/reset-password');
          },
        ),
        FlatButton(
          padding: EdgeInsets.only(left: 0.0),
          child: Text("Бүртгүүлэх", style: TextStyle(fontWeight: FontWeight.w300)),
          onPressed: () {
            Navigator.pushReplacementNamed(context, '/register');
          },
        ),
      ],
    );

    var doLogin = () {
      final form = formKey.currentState;

      if (form.validate()) {
        form.save();

        final Future<Map<String, dynamic>> successfulMessage =
            auth.login(_username, _password);

        successfulMessage.then((response) {
          if (response["error"] == "failed") {
            Flushbar(
              title: "Алдаа",
              message: "Уучлаарай, холболтын алдаа гарлаа",
              duration: Duration(seconds: 3),
              flushbarStyle: FlushbarStyle.GROUNDED,
            ).show(context);
            return;
          }
          if (response['status']) {
            User user = response['user'];
            Provider.of<UserProvider>(context, listen: false).setUser(user);
            Navigator.pushReplacementNamed(context, '/home');
            return;
          }
          if (!response['status']) {
            Flushbar(
              title: "Алдаа",
              message: "Нэвтрэх эрх буруу байна.",
              duration: Duration(seconds: 3),
              flushbarStyle: FlushbarStyle.GROUNDED,
            ).show(context);
          }
        });
      } else {
        Flushbar(
          title: "Алдаа",
          message: "Маягтыг зөв бөглөнө үү",
          duration: Duration(seconds: 100),
          flushbarStyle: FlushbarStyle.GROUNDED,
        ).show(context);
      }
    };

    return Scaffold(
      body: SingleChildScrollView(
        child: Container(
          padding: EdgeInsets.all(40.0),
          child: Form(
            key: formKey,
            child: Column(
              crossAxisAlignment: CrossAxisAlignment.start,
              children: [
                SizedBox(height: 250.0),
                Text("Майл хаяг"),
                SizedBox(height: 5.0),
                usernameField,
                SizedBox(height: 20.0),
                Text("Нууц үг"),
                SizedBox(height: 5.0),
                passwordField,
                SizedBox(height: 20.0),
                auth.loggedInStatus == Status.Authenticating
                    ? loading
                    : RaisedButton(
                        onPressed: doLogin,
                        child: Text("Нэвтрэх"),
                        
                      ),
                SizedBox(height: 5.0),
                forgotLabel
              ],
            ),
          ),
        ),
      ),
    );
  }
}
