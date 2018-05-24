# Juju

![juju](https://emojipedia-us.s3.amazonaws.com/thumbs/120/apple/129/potato_1f954.png)

## About Juju

Juju is a REST application framework with expressive, elegant structure. We believe development must be an enjoyable and creative experience to be truly fulfilling. Juju attempts to take the liability of organising the code as much as possible, making it a very easy to start developing your project within minutes, deployment is also very easy, whether you will deploy locally, on Docker, or creating microservices with server deployment, we've got you covered with easy to manage configuration, some of Juju features:

- Simple, fast routing engine using Classful resource views declaration.
- Powerful yet easy to use middleware, simply utilize decorators which everyone loves.
- Expressive, intuitive database ORM. Although the framework is ORM agnostic, Juju ORM comes enabled out of the box. PonyORM is available to use out of the box as well, but it is not enabled by default, SqlAlchemy is also supported out of the box with minor configuration changes.
- Database agnostic schema migrations (Orator, and SQLAlchemy ORM, Pony still doesn't support migrations).
- Uses Gunicorn server out of the box (feel free to use whatever you like).
- Easy to use command line tool.
- Database tasks command line tool.
- Easy to manage extension deployment.

Juju is extendable, Flask runs at the heart of Juju makes it very easy to benefit from Flask ecosystem. Juju is accessible, yet powerful, providing tools needed for large, robust applications.

## Learning Juju

Documentation hasn't completed yet, but will be available ASAP.

### Installation and running

* `git clone https://github.com/laith43d/juju.git`
* `python3 -m venv venv`
* `source venv/bin/activate`
* `pip install -r requirements.txt`
* `pip install --editable .`
* Use `juju` command to build your application, or you can build everything manually.
* Use `python db.py` to manage database tasks from the command line.
* Quick start guide as well as video tutorials will be available soon.

## Contributing

Thank you for considering contributing to the Juju framework! The contribution guide will be published after the documentation, however feel free to contribute by making PRs or creating issues if you find anything needs to be fixed.

## Security Vulnerabilities

If you discover a security vulnerability within Juju, please don't hesitate to create an issue.

## License

The Juju framework is an open-source software licensed under [MIT license](https://opensource.org/licenses/MIT).

