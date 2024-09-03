
from app import App
from manual import Manual

if __name__ == "__main__":
    app: App = App()

    Manual.introduction()
    while app.running:
        app.run()

