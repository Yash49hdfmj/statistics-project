from flask import Flask, render_template, request
import os
base_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))  # go one level up

app = Flask(
    __name__,
    template_folder=os.path.join(base_dir, 'frontend', 'templates'),
    static_folder=os.path.join(base_dir, 'frontend', 'static')
)
# Dummy ranges and values — replace with real data loading if needed
overall_qual = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
garage_cars = [0, 1, 2, 3, 4]
full_bath = [0, 1, 2, 3]
fireplaces = [0, 1, 2, 3]
year_built = list(range(1900, 2024))  # or load from dataset

# Min/max values (based on script.js)
grliv_min, grliv_max = 334, 5642
bsmt_min, bsmt_max = 0, 6110
firstflr_min, firstflr_max = 334, 4692

@app.route('/', methods=['GET', 'POST'])
def home():
    predicted_price = None

    if request.method == 'POST':
        # Example: Extract form values
        data = {
            'OverallQual': int(request.form['OverallQual']),
            'GarageCars': int(request.form['GarageCars']),
            'FullBath': int(request.form['FullBath']),
            'Fireplaces': int(request.form['Fireplaces']),
            'YearBuilt': int(request.form['YearBuilt']),
            'GrLivArea': int(request.form['GrLivArea']),
            'TotalBsmtSF': int(request.form['TotalBsmtSF']),
            '1stFlrSF': int(request.form['1stFlrSF']),
        }

        # TODO: Add your ML model prediction here
        # predicted_price = model.predict([data.values()])

        # For now, mock prediction:
        predicted_price = 50000 + data['GrLivArea'] * 50

    return render_template(
        'index.html',
        overall_qual=overall_qual,
        garage_cars=garage_cars,
        full_bath=full_bath,
        fireplaces=fireplaces,
        year_built=year_built,
        grliv_min=grliv_min,
        grliv_max=grliv_max,
        bsmt_min=bsmt_min,
        bsmt_max=bsmt_max,
        firstflr_min=firstflr_min,
        firstflr_max=firstflr_max,
        predicted_price=predicted_price
    )

if __name__ == '__main__':
    app.run(debug=True)
