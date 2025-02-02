from fastapi import FastAPI, Query
from fastapi.middleware.cors import CORSMiddleware
import json

app = FastAPI()

# Enable CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["GET"],
    allow_headers=["*"],
)

# Load marks data
with open("q-vercel-python.json", "r") as file:  
    marks_list = json.load(file)
    # print(marks_list)

# Convert list to a dictionary for fast lookup
marks_data = {entry["name"]: entry["marks"] for entry in marks_list}

@app.get("/api")
def get_marks(name: list[str] = Query([])):
    result = [marks_data.get(n, None) for n in name]
    return {"marks": result}

'''
git init
git add .
git commit -m "Initial commit"
Create the repository in the Github website and then connect remotely
git remote add origin https://github.com/vitoiitmBSc/Just_check_again
# This will push the file in to the repository
git push -u origin master check again

'''