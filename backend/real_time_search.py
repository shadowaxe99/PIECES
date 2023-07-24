```python
from flask import Flask, request, jsonify
from database import SearchResultSchema, searchResults
from some_external_travel_api import ExternalTravelAPI

app = Flask(__name__)

@app.route('/search', methods=['POST'])
def perform_real_time_search():
    search_params = request.json
    results = ExternalTravelAPI.search(search_params)
    
    # Validate and serialize search results
    result_data, errors = SearchResultSchema(many=True).load(results)
    if errors:
        return jsonify(errors), 400

    # Store search results
    searchResults.extend(result_data)

    return jsonify(SearchResultSchema(many=True).dump(searchResults)), 200
```