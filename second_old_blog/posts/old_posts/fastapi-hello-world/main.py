from fastapi import FastAPI

# Create an instance of FastAPI
app = FastAPI()


# Define a route for the root URL
@app.get("/")
def read_root():
    return {"message": "Hello, World!"}


# Run the application
if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="127.0.0.1", port=8000)
