import requests


def requestURL(baseurl, params):
    """This function accepts a URL path and a params diction as inputs.
        It calls requests.get() with those inputs, and returns the full URL
        of the data you want to get."""

    req = requests.Request(method='GET', url=baseurl, params=params)
    prepped = req.prepare()
    return prepped.url


some_base_url = "https://google.com/search"
some_params_dictionary = {"q": "violins and guitars", "tbm": "isch"}
print(requestURL(some_base_url, some_params_dictionary))

# Problem-1

"""
requests-8-1: If the results you are getting back from a call to "requests.get()" are not
              what you expected, what’s the first thing you should do?
--> A. look at the .url attribute of the Response object
--> B. look at the first few characters of the .text attribute of the Response object
--> C. look at the .status attribute of the response object
--> D. look carefully at your code and compare it to the sample code here
"""

# Problem-2

"""
requests-8-2: In a full python environment, if there is a runtime error and you don’t get
              a Response object back from the call to requests.get(), what should you do?
--> A. look at the .url attribute of the Response object
--> B. look at the values you passed in to requests.get()
--> C. invoke the requestURL() function with the same parameters you used to invoke requests.get()
--> D. look carefully at your code and compare it to the sample code here
"""

# Problem-3

"""
requests-8-3: In a runestone environment, if there is a runtime error and you don’t get
              a Response object back from the call to requests.get(), what should you do?
--> A. look at the .url attribute of the Response object
--> B. look at the values you passed in to requests.get()
--> C. invoke the requestURL() function with the same parameters you used to invoke requests.get()
--> D. look carefully at your code and compare it to the sample code here
"""
