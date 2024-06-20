import requests
import pprint
#RESTful API (Representational State Transfer API):
#stateless as is http
#JSON and dictionary easy to convert between.
class RestClient:
  def __init__(self, base_url):
    self.base_url = base_url

  def get(self, endpoint):
    response = requests.get(f"{self.base_url}{endpoint}")
    return response.json()

  def post(self, endpoint, data):
    response = requests.post(f"{self.base_url}{endpoint}", json=data)
    return response.json()

  def put(self, endpoint, data):
    response = requests.put(f"{self.base_url}{endpoint}", json=data)
    return response.json()

  def delete(self, endpoint):
    response = requests.delete(f"{self.base_url}{endpoint}")
    return response.status_code

# Usage example
if __name__ == "__main__":
  api_client = RestClient("https://jsonplaceholder.typicode.com")

  # GET request
  posts = api_client.get("/posts")
  #print("GET /posts:", posts)

  # POST request
  new_post = {
      "title": "foo",
      "body": "bar",
      "userId": 1
  }
  created_post = api_client.post("/posts", new_post)
  print("POST /posts:", created_post)

  # PUT requests
  updated_post1 = {
      "id": 1,
      "title": "Updated Title 1",
      "body": "This is the updated body 1",
      "userId": 1
  }
  updated_response1 = api_client.put("/posts/1", updated_post1)
  # print("PUT /posts/1 (1st update):", updated_response1)
  pp = pprint.PrettyPrinter(indent=4)
  pp.pprint("PUT /posts/1 (1st update):")
  pp.pprint(updated_response1)

  updated_post2 = {
      "id": 2,
      "title": "Updated Title 2",
      "body": "This is the updated body 2",
      "userId": 1
  }
  updated_response2 = api_client.put("/posts/2", updated_post2)
  # print("PUT /posts/2 (2nd update):", updated_response2)
  pp.pprint("PUT /posts/2 (2nd update):")
  pp.pprint(updated_response2)

  # Fetch all posts again after PUTs (corrected line)
  all_posts = api_client.get("/posts/1")  # Get all posts to ensure latest data

  # Print data retrieved after PUTs
  #NOTE: for this case as the server is fake, this is going to return the default date and not what was set!
  print("GET /posts (after PUTs):")
  pp = pprint.PrettyPrinter(indent=4)
  print("\nNOTE: for this case as the server is fake, this is going to return the default date and not what was set!\n")
  pp.pprint(all_posts)

  # DELETE request
  # delete_response = api_client.delete("/posts/1")
  # print("DELETE /posts/1:", delete_response)