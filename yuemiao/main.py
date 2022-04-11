import function
import urls
import headers
if __name__ == '__main__':
    url=urls.user_detail;
    print(url)
    session="eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpYXQiOjE2NDYwMjAzNzguMDEzMTAyMywiZXhwIjoxNjQ2MDIzOTc4LjAxMzEwMjMsInN1YiI6IllOVy5WSVAiLCJqdGkiOiIyMDIyMDIyODExNTI1OCIsInZhbCI6InB6UkVBUUlBQUFBUU9UVTROMkppTldNMFpHTmpZV0prWXh4dmNYSTFielZHTmxCa2RtaEhjMWd0VFdKelptdGFNRXN3TFZVNEFCeHZcclxuVlRJMldIUTJSMHBXTjJod1lTMXdRM1I2WTJwdE4yOU1hWEJORERFM01TNHhOUzR4T0M0NE53QUFBQUFBQUFBPSJ9.njUEFkfezXVdRGfXXHjX-Mhsu3HiBNeFawdMn_vkR8Y"
    print(headers.get_user_heaer(session))
    print(function.function(url,headers.get_user_heaer(session),None))
