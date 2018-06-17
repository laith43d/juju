from config.settings import create_app

app_instance = create_app()


if __name__ == '__main__':
    app_instance.run()