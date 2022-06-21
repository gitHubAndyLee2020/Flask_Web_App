# this is possible because it is a __init__.py file
from website import create_app

app = create_app()

# this specifies that the app will only start running from the main file
# debug=True means any time the code changes, the server will restart
# debug=True should be removed at production
if __name__ == '__main__':
  app.run(debug=True)
