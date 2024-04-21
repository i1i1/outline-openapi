# openapi_client.AttachmentsApi

All URIs are relative to *https://app.getoutline.com/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**attachments_create_post**](AttachmentsApi.md#attachments_create_post) | **POST** /attachments.create | Create an attachment
[**attachments_delete_post**](AttachmentsApi.md#attachments_delete_post) | **POST** /attachments.delete | Delete an attachment
[**attachments_redirect_post**](AttachmentsApi.md#attachments_redirect_post) | **POST** /attachments.redirect | Retrieve an attachment


# **attachments_create_post**
> AttachmentsCreatePost200Response attachments_create_post(attachments_create_post_request=attachments_create_post_request)

Create an attachment

Creating an attachment object creates a database record and returns the inputs needed to generate a signed url and upload the file from the client to cloud storage.

### Example

* Bearer (JWT) Authentication (http):

```python
import openapi_client
from openapi_client.models.attachments_create_post200_response import AttachmentsCreatePost200Response
from openapi_client.models.attachments_create_post_request import AttachmentsCreatePostRequest
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://app.getoutline.com/api
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://app.getoutline.com/api"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): http
configuration = openapi_client.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.AttachmentsApi(api_client)
    attachments_create_post_request = openapi_client.AttachmentsCreatePostRequest() # AttachmentsCreatePostRequest |  (optional)

    try:
        # Create an attachment
        api_response = api_instance.attachments_create_post(attachments_create_post_request=attachments_create_post_request)
        print("The response of AttachmentsApi->attachments_create_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AttachmentsApi->attachments_create_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **attachments_create_post_request** | [**AttachmentsCreatePostRequest**](AttachmentsCreatePostRequest.md)|  | [optional] 

### Return type

[**AttachmentsCreatePost200Response**](AttachmentsCreatePost200Response.md)

### Authorization

[http](../README.md#http)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**400** | The request failed one or more validations. |  -  |
**401** | The API key is missing or otherwise invalid. |  -  |
**403** | The current API key is not authorized to perform this action. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **attachments_delete_post**
> AttachmentsDeletePost200Response attachments_delete_post(attachments_redirect_post_request=attachments_redirect_post_request)

Delete an attachment

Deleting an attachment is permanant. It will not delete references or links to the attachment that may exist in your documents.

### Example

* Bearer (JWT) Authentication (http):

```python
import openapi_client
from openapi_client.models.attachments_delete_post200_response import AttachmentsDeletePost200Response
from openapi_client.models.attachments_redirect_post_request import AttachmentsRedirectPostRequest
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://app.getoutline.com/api
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://app.getoutline.com/api"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): http
configuration = openapi_client.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.AttachmentsApi(api_client)
    attachments_redirect_post_request = openapi_client.AttachmentsRedirectPostRequest() # AttachmentsRedirectPostRequest |  (optional)

    try:
        # Delete an attachment
        api_response = api_instance.attachments_delete_post(attachments_redirect_post_request=attachments_redirect_post_request)
        print("The response of AttachmentsApi->attachments_delete_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AttachmentsApi->attachments_delete_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **attachments_redirect_post_request** | [**AttachmentsRedirectPostRequest**](AttachmentsRedirectPostRequest.md)|  | [optional] 

### Return type

[**AttachmentsDeletePost200Response**](AttachmentsDeletePost200Response.md)

### Authorization

[http](../README.md#http)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**400** | The request failed one or more validations. |  -  |
**401** | The API key is missing or otherwise invalid. |  -  |
**403** | The current API key is not authorized to perform this action. |  -  |
**404** | The specified resource was not found. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **attachments_redirect_post**
> attachments_redirect_post(attachments_redirect_post_request=attachments_redirect_post_request)

Retrieve an attachment

Load an attachment from where it is stored based on the id. If the attachment is private then a temporary, signed url with embedded credentials is generated on demand.

### Example

* Bearer (JWT) Authentication (http):

```python
import openapi_client
from openapi_client.models.attachments_redirect_post_request import AttachmentsRedirectPostRequest
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://app.getoutline.com/api
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://app.getoutline.com/api"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): http
configuration = openapi_client.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.AttachmentsApi(api_client)
    attachments_redirect_post_request = openapi_client.AttachmentsRedirectPostRequest() # AttachmentsRedirectPostRequest |  (optional)

    try:
        # Retrieve an attachment
        api_instance.attachments_redirect_post(attachments_redirect_post_request=attachments_redirect_post_request)
    except Exception as e:
        print("Exception when calling AttachmentsApi->attachments_redirect_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **attachments_redirect_post_request** | [**AttachmentsRedirectPostRequest**](AttachmentsRedirectPostRequest.md)|  | [optional] 

### Return type

void (empty response body)

### Authorization

[http](../README.md#http)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**302** | The url for the attachment |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

