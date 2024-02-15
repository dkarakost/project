from website import create_app

app = create_app()

if __name__ == '__main__': # to run the flask application
    app.run(debug=True) #the dubug=True means that when we change something to the code the server reruns
