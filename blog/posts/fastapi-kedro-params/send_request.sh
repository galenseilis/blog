curl -X POST "http://127.0.0.1:8000/run-kedro/" -H "Content-Type: application/json" -d '{
    "project_name": "spaceflights-pandas",
    "params": {
        "test_size": "0.3",
        "random_state": "2018"
    }
}'
