import requests
from stripper import strip_tags

def getDirection(origin, destination):
  payload = {'origin': origin, 'destination': destination}
  response = requests.get("http://maps.googleapis.com/maps/api/directions/json", params=payload)
  jsonResponse = response.json()
  legRoute = jsonResponse.routes[0].legs[0];
  directionStr = "Distance : " + legRoute.distance.value + "\n"
  directionStr += "Direction: \n"
  steps = legRoute.steps
  for idx, step in enumerate(steps):
    directionStr += str(idx) + ". " + strip_tags(step.html_instructions) + "\n"

  return directionStr
