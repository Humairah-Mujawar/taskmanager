import requests

tasks = [ 
    {"title": "Learn Django", "description": "Build a demo project"}, 
    {"title": "Prepare interview", "description": "Review Django concepts"} 
    ]

for t in tasks:
    requests.post("http://127.0.0.1:8000/tasks/", json=t)