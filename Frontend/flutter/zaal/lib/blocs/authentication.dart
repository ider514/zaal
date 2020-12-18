import 'dart:async';
import 'dart:convert';

import 'package:flutter/material.dart';
import 'package:http/http.dart';

import 'package:zaal/data/api.dart';
import 'package:zaal/data/user.dart';

enum Status {
  NotLoggedIn,
  NotRegistered,
  LoggedIn,
  Registered,
  Authenticating,
  Registering,
  LoggedOut
}

class AuthProvider with ChangeNotifier {
  Status _loggedInStatus = Status.NotLoggedIn;
  Status _registeredInStatus = Status.NotRegistered;

  Status get loggedInStatus => _loggedInStatus;
  Status get registeredInStatus => _registeredInStatus;

  Future<Map<String, dynamic>> login(String email, String password) async {
    var result;
    var loginData = new Map<String, dynamic>();
    loginData['username'] = email;
    loginData['password'] = password;
    _loggedInStatus = Status.Authenticating;
    notifyListeners();

    Response response = await post(
      AppUrl.login,
      body: loginData,
    );
    // Error authenticating
    if (response.statusCode != 200 && response.statusCode != 400) {
      result = {"error": "failed"};
      print("123here");
      _loggedInStatus = Status.NotLoggedIn;
      notifyListeners();
      return result;
    }
    // Successful login
    if (response.statusCode == 200) {
      final Map<String, dynamic> responseData = json.decode(response.body);

      var userData = {"email": email, "token": responseData["token"]};

      User authUser = User.fromJson(userData);

      UserPreferences().saveUser(authUser);

      _loggedInStatus = Status.LoggedIn;
      notifyListeners();

      result = {'status': true, 'message': 'Successful', 'user': authUser};
    } else {
      _loggedInStatus = Status.NotLoggedIn;
      notifyListeners();
      result = {
        'status': false,
        'message': json.decode(response.body)['error']
      };
    }
    return result;
  }

  Future<Map<String, dynamic>> register(
      String email, String password, String passwordConfirmation) async {
    var registrationData = new Map<String, dynamic>();

    registrationData['email'] = email;
    registrationData['password'] = password;
    registrationData['password2'] = passwordConfirmation;

    _registeredInStatus = Status.Registering;
    notifyListeners();

    return await post(AppUrl.register, body: registrationData)
        .then(onValue)
        .catchError(onError);
  }

  Future<FutureOr> onValue(Response response) async {
    var result;
    final Map<String, dynamic> responseData = json.decode(response.body);
    // Http unsuccessful
    if (response.statusCode != 200) {
      _registeredInStatus = Status.NotRegistered;
      notifyListeners();
      result = {'': 'Уучлаарай, холболтын алдаа гарлаа'};
      return result;
    }
    // Email already exists
    if (responseData["email"][0].contains("already exists")) {
      result = {'': 'Бүртгэлтэй майл хаяг байна.'};
      _registeredInStatus = Status.NotRegistered;
      notifyListeners();
      return result;
    }
    // Invalid email
    if (responseData["email"][0].contains("valid email")) {
      result = {'': 'Майл хаяг биш байна.'};
      _registeredInStatus = Status.NotRegistered;
      notifyListeners();
      return result;
    }
    // Success registering
    if (responseData["response"].contains("successfully registered")) {
      User authUser = User.fromJson(responseData);

      UserPreferences().saveUser(authUser);

      result = {
        'status': true,
        'message': 'Successfully registered',
        'data': authUser
      };
    } else {
      result = {
        'status': false,
        'message': 'Registration failed',
        'data': responseData
      };
    }

    return result;
  }

  static onError(error) {
    print("the error is $error.detail");
    return {'status': false, 'message': 'Unsuccessful Request', 'data': error};
  }
}
