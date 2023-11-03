from flask import Flask, request, jsonify
import util


app = Flask(__name__)


@app.route('/get_city', methods=['GET'])
def get_city():
    response = jsonify({
        'city': util.get_city()
    })
    response.headers.add('Access-Control-Allow-Origin','*')
    return response

@app.route('/predict_home_prices', methods=['GET','POST'])
def predict_home_prices():
    city= (request.form['city'])
    bedroom = float(request.form['bedroom'])
    bathroom = float(request.form['bathroom'])
    sqft_living = float(request.form['sqft_living'])
    sqft_lot = float(request.form['sqft_lot'])
    floors = int(request.form['floors'])
    view = int(request.form['view'])
    condition = int(request.form['condition'])
    sqft_basement = float(request.form['sqft_basement'])

    response = jsonify({
        'estimated_price':util.get_estimated_price((city, bedroom, bathroom, sqft_living, sqft_lot, floors, view, condition, sqft_basement))
    })
    response.headers.set('Access-Control-Allow-Origin','*')
    response.headers.set('Access-Control-Allow-Headers', 'Content-Type,Authorization')
    response.headers.set('Access-Control-Allow-Methods', 'GET,POST')
    return response


if __name__ == "__main__":
    print("starting python flask server")
    util.load_saved_artificats()
    app.run()