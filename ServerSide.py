from flask import Flask
from flask_restful import Api, Resource, reqparse

app = Flask(__name__)
api = Api(app)

data = [{
  "resourceType": "Patient",
  "id" : "xcda",
  "text": 
  [{
    "status": "generated",
    "div":"<div>\n \n <p>Henry Levin the 7th</p> \n \n </div>"
  }],
  "identifier": 
  [{
      "use": "usual",
      "type": 
			[{
			"coding": 
				[{
					"system": "http://hl7.org/fhir/v2/0203",
					"code": "MR"
				}]
			}],
	  
      "system": "urn:oid2.16.840.1.113883.19.5",
      "value": "12345"
   }],
  "active": "true", 
  "name": 
  [{
      "family": "Levin",
      "given": "Kevin"
  }],
  "gender": "Male",
  "birthDate": "2002-09-24",
  "managingOrganization": 
  [{
    "reference": "Organization/2.16.840.1.113883.19.5",
    "display": "University Health Network"
  }],
  "conditions": [
    "Diabetes",
    "High blood pressure",
    "Asthma"
  ]
}]

class Data(Resource):
    def get(self):
        return data, 200

      
api.add_resource(Data, "/")

app.run(debug=True)