import 'package:flushbar/flushbar.dart';
import 'package:flutter/material.dart';
import 'package:provider/provider.dart';
import 'package:zaal/blocs/authentication.dart';
import 'package:zaal/data/user.dart';

class Register extends StatefulWidget {
  @override
  _RegisterState createState() => _RegisterState();
}

class _RegisterState extends State<Register> {
  final formKey = new GlobalKey<FormState>();

  String _username, _password, _confirmPassword;

  @override
  Widget build(BuildContext context) {
    AuthProvider auth = Provider.of<AuthProvider>(context);

    final usernameField = TextFormField(
      autofocus: false,
      validator: (value) => value.isEmpty ? "Майл хаяг оруулна уу" : null,
      onSaved: (value) => _username = value,
      decoration: InputDecoration(
          icon: Icon(Icons.email), labelText: "Майл хаяг"),
    );

    final passwordField = TextFormField(
      autofocus: false,
      obscureText: true,
      validator: (value) => value.isEmpty ? "Нууц үг" : null,
      onSaved: (value) => _password = value,
      decoration: InputDecoration(
          icon: Icon(Icons.lock), labelText: "Нууц үг"),
    );

    final confirmPassword = TextFormField(
      autofocus: false,
      validator: (value) {
        if (_confirmPassword != _password) {
          return "Нууц үг зөрж байна";
        }
        if (value.isEmpty) {
          return "Нууц үг оруулна уу";
        }
        return null;
      },
      onSaved: (value) => _confirmPassword = value,
      obscureText: true,
      decoration: InputDecoration(
          icon: Icon(Icons.lock), labelText: "Нууц үг давтах"),
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
          onPressed: () {},
        ),
        FlatButton(
          padding: EdgeInsets.only(left: 0.0),
          child: Text("Нэвтрэх", style: TextStyle(fontWeight: FontWeight.w300)),
          onPressed: () {
            Navigator.pushReplacementNamed(context, '/login');
          },
        ),
      ],
    );

    void doRegister() {
      final form = formKey.currentState;
      form.save();
      if (_confirmPassword != _password) {
        Flushbar(
          title: "Алдаа",
          message: "Нууц үг зөрж байна",
          duration: Duration(seconds: 100),
          flushbarStyle: FlushbarStyle.GROUNDED,
        ).show(context);
        return;
      } else {
        if (form.validate()) {
          auth
              .register(_username, _password, _confirmPassword)
              .then((response) {
            if (response['status']) {
              User user = response['data'];
              Provider.of<UserProvider>(context, listen: false).setUser(user);
              Navigator.pushReplacementNamed(context, '/home');
            } else {
              Flushbar(
                title: "Алдаа",
                message: response
                    .toString()
                    .substring(3, response.toString().length - 1),
                duration: Duration(seconds: 100),
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
      }
    }

    ;

    return Scaffold(
      body: Container(
        padding: EdgeInsets.all(40.0),
        child: Form(
          key: formKey,
          child: Column(
            crossAxisAlignment: CrossAxisAlignment.start,
            children: [
              SizedBox(height: 215.0),
              Text("Майл хаяг"),
              SizedBox(height: 5.0),
              usernameField,
              SizedBox(height: 15.0),
              Text("Нууц үг"),
              SizedBox(height: 10.0),
              passwordField,
              SizedBox(height: 15.0),
              Text("Нууц үг давтах"),
              SizedBox(height: 10.0),
              confirmPassword,
              SizedBox(height: 20.0),
              auth.registeredInStatus == Status.Registering
                  ? loading
                  : RaisedButton(
                      onPressed: doRegister,
                      child: Text("Бүртгүүлэх"),
                    ),
              SizedBox(height: 5.0),
              forgotLabel
            ],
          ),
        ),
      ),
    );
  }
}
