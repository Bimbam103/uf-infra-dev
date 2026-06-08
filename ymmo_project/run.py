from app import create_app

app = create_app()

if __name__ == '__main__':
    # Mode debug activé pour voir les modifications en temps réel
    app.run(debug=True, host='0.0.0.0', port=5000)