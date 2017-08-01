import requests
import json
import  unittest

#A class that provides incoming web hooks for sending message

class WebHook:

  # Returns the response code for the request
  # @param Takes url as an argument
  # @param Takes body of the request
  # @param Takes header of the request
  # @return Response status code
  #   pattern
  

   def  postMesssage(self, url, params, head):
      params=json.dumps(params)
      response= requests.post(url, params, head)

      if(response.status_code == 200) :
         return "pass"
      
      else:
         return "fail"


class WebHookTest(unittest.TestCase):
    """
    Check the message is posted and the status code is 200 
    """
    def test_postMessage(self):
      headers = {'content-type' : 'application/json'}
      URL = 'https://hooks.slack.com/services/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'
      PARAMS= {'text': '#bring an umbrella whenever it\'s raining'}
      test1 = WebHook()
      self.assertEqual("pass",test1.postMesssage(URL,PARAMS,headers))

    """
    Check the message is not posted and return status code 404
    """
    def test_invalidUrl(self):
      headers = {'content-type' : 'application/json'}
      URL = 'https://hooks.slack.com/services/T6EDHB1AA/B6FBXNQRZ/KTGhGSU0rqNR89n62Uf'
      PARAMS= {'text': '#bring an umbrella whenever it\'s raining'}
      test2 = WebHook()
      self.assertEqual("fail",test2.postMesssage(URL,PARAMS,headers))


if __name__ == '__main__':
    unittest.main()
