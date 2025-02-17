from flask import Flask, jsonify
import openai
import pandas as pd
from flask_cors import CORS

app = Flask(__name__)
CORS(app, resources={r"/*": {"origins": "*"}})
# OpenAI API Key
openai.api_key = 

@app.route('/forecast', methods=['GET'])

def forecast():
    # Load the historical data (from Excel or CSV)
    # data = pd.read_excel('data.xlsx')
    data = [
        {
            "Jan":200,
            "Feb": 300,
            "Mar": 500,
        }
    ]
    
    # Prepare the historical data for the OpenAI model
    historical_data = data.to_string(index=False)

    # # Create the prompt for OpenAI to forecast
    #  prompt = f"""
    # Here is the historical revenue data:

    {historical_data}

    # Based on this data, forecast the next 12 months of revenue. Provide your forecast in the format of Month: Revenue, Month: Revenue.
    # """
    
    # # Get forecast from OpenAI
    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=prompt,
        max_tokens=100,
        temperature=0.7,
    )
    
    forecast = response.choices[0].text.strip()
    
    # Return the forecast as JSON
    return jsonify({
        'forecast': data
    })

if __name__ == '__main__':
    app.run(debug=True)

