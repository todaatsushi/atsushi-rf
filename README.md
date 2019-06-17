# Restaurant Roulette (atsushi-rf)
Restaurant Roulette - given a London Tube stop, gives you a restaurant to go to! Uses Django, VueJS and the Zomato API.

## Getting Started

These instructions will get you a copy of the project up and running on your local machine.

### Installing

Using a virtual env (recommended), install dependancies from requirements.txt.

```
pip install -r requirements.txt
```

### .env variables
RR expects:
* SECRET_KEY - Django secret key
* ZOMATO_API_KEY - A [Zomato API secret key](https://developers.zomato.com/api)
* DEBUG - Debug configuration ('True' for debug mode)

Put them in a .env file and set with:
```
set -a; source .env; set +a;
```

## Extra installation notes
RR does not have any models to migrate so it is ready to go.
## Deployment

To serve static files make sure [Whitenoise](http://whitenoise.evans.io/en/stable/django.html) is configured properly and run
```
python manage.py collectstatic
```

## Built With

* [Django](https://docs.djangoproject.com/en/2.2/) - The web framework used
* [Bulma](https://getuikit.com/docs/introduction) - CSS framework
* VueJS(https://vuejs.org/) - JavaScript framework

## Authors

* **Me, Atsushi Toda** - [GitHub](https://github.com/broadsinatlanta) - [Actual atsushi.dev site](https://www.atsushi.dev)

## License

This project is licensed under the MIT License.

