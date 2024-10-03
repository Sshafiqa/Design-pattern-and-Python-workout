import requests

# GET request
response = requests.get('https://jsonplaceholder.typicode.com/posts/1')
print("GET Response:\n", response.json())

# POST request
new_post = {
    "userId": 1,
    "id": 101,
    "title": "foo",
    "body": "bar"
}
response = requests.post('https://jsonplaceholder.typicode.com/posts', json=new_post)
print("POST Response:\n", response.json())

# PUT request
updated_post = {
    "userId": 1,
    "id": 1,
    "title": "foo updated",
    "body": "bar updated"
}
response = requests.put('https://jsonplaceholder.typicode.com/posts/1', json=updated_post)
print("PUT Response:\n", response.json())

# DELETE request
response = requests.delete('https://jsonplaceholder.typicode.com/posts/1')
print("DELETE Response Status Code:\n", response.status_code)
