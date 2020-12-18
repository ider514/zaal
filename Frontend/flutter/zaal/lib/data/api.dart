class AppUrl {
  static const String liveBaseURL = "";
  static const String localBaseURL = "http://127.0.0.1:8000";

  static const String baseURL = localBaseURL;
  static const String path = "/api/account";
  static const String login = baseURL + path + "/login";
  static const String register = baseURL + path + "/register";
  static const String forgotPassword = baseURL + path + "/forgot-password";
}