# MSP17-bilderrahmen-frontendtests

This repository is part of the ['Ich-Zeig-Dir-Was'-Bilderrahmen project](https://github.com/informatik-mannheim/bilderrahmen-msp17). The test cover the functionality on the [Ionic-App](https://github.com/informatik-mannheim/MSP17-bilderrahmen-ionicapp) and the [Webapp](https://github.com/informatik-mannheim/MSP17-bilderrahmen-webapp).

## Prerequisites

- 3 Google test accounts:
	- test account 1, which has images uploaded through the [Webapp](https://github.com/informatik-mannheim/MSP17-bilderrahmen-webapp )
    - test account 2, which is already used for the ionic app. It will always and delete images on tear down.
    - test account 3, not used in the [Ionic-App](https://github.com/informatik-mannheim/MSP17-bilderrahmen-ionicapp). Only needed for one Testcase. If you only want to use one account, skip that test in todo.
- At least one Android test device (physical)
- Test Browser for Selenium (see [Set up Selenium for Firefox and Chrome](https://michalzalecki.com/setup-selenium-with-geckodriver-and-chromedriver/):)
    - Firefox (needs geckodriver) or
    - Chrome (needs chromedriver)
- Tests are written in python3 and requires the following packages:
    - [Appium-Python-Client](https://github.com/appium/python-client) v0.13 
    - [Selenium](https://github.com/SeleniumHQ/selenium/tree/master/py) v3.4.0
- [Appium](https://github.com/appium/appium) v1.6.5 
- [Android SDK](https://developer.android.com/studio/releases/sdk-tools.html) platform tools: adb and fastboot


## Installing
Clone this repository or download it as ZIP:

```
https://github.com/informatik-mannheim/MSP17-bilderrahmen-frontendtests.git
```

or

```
git clone https://github.com/informatik-mannheim/MSP17-bilderrahmen-frontendtests.git
```
## Test environment settings
Set test environment in the *testEnvironmentValues.py*:
 - capabilities (Devices)
 - ports for appium server
 - set the test accounts

## Running tests
Start appium Server. Two devices need two different ports.

Run all tests
```
python3 testSuite.py --browser Firefox
```
or run webapp tests only
```
python3 test_webapp.py --browser Chrome
```
or run ionicapp tests only
```
python3 test_ionicapp.py
```


## License
This project is licensed under the Apache-2.0 License - see the [LICENSE](LICENSE) file for details.
