# proxy-scrape

Scrape Amazon Android app websites using rotating proxies. A user would input a Amazon Android app url link and a page will be rendered with app title, version, change logs, and original release date.

## Getting Started

Clone the repo, setup virtual env, install requirements.txt, run flask server

### Prerequisites

Anyone using this repo should know basic virtual env, flask commands, and basic knowledge of python.

Were going to need to install pip, virtualenv, and the packages listed in the requirements.txt file. 

Currently only have Mac terminal commands. I think it works with Git shell as well for Windows users.
Follow instructions below after opening a shell CLI.

If there are any questions to help get started please post them!

### Installing
clone the repo 
```
git clone https://github.com/Luv2C0de/proxy-scrape.git
```

Install pip

```
sudo easy_install pip
```
Install virtualenv

```
pip install virtualenv
```

Next step is to activate virtualenv and navigate to cloned repo directory

```
source env/bin/activate
```

Install packages from requirements.txt

```
pip install -r /path/to/requirements.txt
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

N/A

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
