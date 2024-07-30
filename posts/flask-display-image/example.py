from flask import Flask, send_file
import requests
from io import BytesIO

app = Flask(__name__)

@app.route('/card/<int:card_id>')
def display_image(card_id):
    # The URL of the image you want to display
    image_url = f'https://gatherer.wizards.com/Handlers/Image.ashx?multiverseid={card_id}&type=card'

    # Fetch the image from the URL
    response = requests.get(image_url)
    
    # Check if the request was successful
    if response.status_code == 200:
        # Create an in-memory binary stream of the image
        image_stream = BytesIO(response.content)
        
        # Send the image as a response
        return send_file(image_stream, mimetype='image/png')
    else:
        # Handle the error case
        return "Failed to retrieve image", response.status_code

if __name__ == '__main__':
    app.run(debug=True)

