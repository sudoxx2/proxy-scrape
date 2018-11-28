# proxy-scrape

Scrape Amazon Android app websites using random user agents. A user would input a Amazon Android app url link and a page will be rendered with app title, version, change logs, and original release date.

## Getting Started

1. Make sure you have Python2 or Python3 installed
2. Clone the repo
3. Setup virtual environment
4. Install dependencies from requirements.txt
5. Run flask server

Using virtual environment is optional(although I still need to test this on a clean mac environment)

### Prerequisites


Were going to need to install pip, virtualenv, and the packages listed in the requirements.txt file. 

Currently only have Mac terminal commands. I think it works with Git shell as well for Windows users.

If there are any questions to help get started please post them!

### Installing

1. Open the terminal

2. Clone the repo 
```
git clone https://github.com/Luv2C0de/proxy-scrape.git
```

3. Install pip

```
sudo easy_install pip
```
4. Install virtualenv

```
sudo -H pip install virtualenv
```
5. Navigate to the cloned repo directory
6. Create a virtualenv

```
virtualenv env
```

7. Activate virtualenv

```
source env/bin/activate
```

8. Install packages from requirements.txt

```
pip install -r requirements.txt
```

### Running App

1. Open terminal and navigate to cloned repo
2. Activate the source if not activated yet
```
source env/bin/activate
```
3. Run the python file 'app.py'
```
python app.py
```
4. Navigate to localhost in browser where app is being ran and input a android amazon url
5. Hit search and see results on next page


## Contributing

Friend at work - Giving awesome feedback for readme and code quality :)
Not sure if he wants to be named

## Authors

* **Peter Moung** - *Initial work* 

## License

This project is licensed under the MIT License - see the [LICENSE](https://github.com/Luv2C0de/second-chances-hackathon-2018/blob/master/LICENSE) file for details

## Acknowledgments

* I always love to code for the community!

## Problems faced

* Grabbing certain data on the page with BeautifulSoup(Amazon pages have a lot of repeated tag content)
* Amazon captcha stopping us from scraping
* Refactoring - code cleanliness + readability
* Handling exceptions
* Bundling a final app
