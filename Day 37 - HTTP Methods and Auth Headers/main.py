# 1. HTTP Requests

# GET - requests.get()
# We have being using the get method until now from the requests module.

# POST - requests.post()
# Instead of receiving the information, we are sending data to the API Endpoint in order to updated it (like a spreadsheet in Google Sheets)
# We will be using this method to create the Pixela habit tracker app.

# PUT - requests.put()
# Will change an existent set of data

# DELETE - requests.delete()
# Will delete a given data set

# 2. Advanced authentication using HTTP headers

# The header is a more secure way of authenticating than API keys because it cannot be intercepted in the browser or be clearly visible
# headers = {
# 	"X-USER-TOKEN": TOKEN
# }
# response = requests.post(url=coding_graph_endpoint, headers=headers, json=pixel_config)


# 3. Formatting the date using datetime module and method strftime
#https://www.w3schools.com/python/python_datetime.asp

from datetime import datetime

today_date = datetime.now()
print(today_date.strftime("%Y%m%d"))

any_other_day = datetime(year=2024, month=9, day=2)
print(any_other_day.strftime("%Y%m%d"))