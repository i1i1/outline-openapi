# openapi_client.CommentsApi

All URIs are relative to *https://app.getoutline.com/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**comments_create_post**](CommentsApi.md#comments_create_post) | **POST** /comments.create | Create a comment
[**comments_delete_post**](CommentsApi.md#comments_delete_post) | **POST** /comments.delete | Delete a comment
[**comments_list_post**](CommentsApi.md#comments_list_post) | **POST** /comments.list | List all comments
[**comments_update_post**](CommentsApi.md#comments_update_post) | **POST** /comments.update | Update a comment


# **comments_create_post**
> CommentsCreatePost200Response comments_create_post(comments_create_post_request=comments_create_post_request)

Create a comment

Create a comment

### Example

* Bearer (JWT) Authentication (http):

```python
import openapi_client
from openapi_client.models.comments_create_post200_response import CommentsCreatePost200Response
from openapi_client.models.comments_create_post_request import CommentsCreatePostRequest
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
    api_instance = openapi_client.CommentsApi(api_client)
    comments_create_post_request = openapi_client.CommentsCreatePostRequest() # CommentsCreatePostRequest |  (optional)

    try:
        # Create a comment
        api_response = api_instance.comments_create_post(comments_create_post_request=comments_create_post_request)
        print("The response of CommentsApi->comments_create_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CommentsApi->comments_create_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **comments_create_post_request** | [**CommentsCreatePostRequest**](CommentsCreatePostRequest.md)|  | [optional] 

### Return type

[**CommentsCreatePost200Response**](CommentsCreatePost200Response.md)

### Authorization

[http](../README.md#http)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**401** | The API key is missing or otherwise invalid. |  -  |
**403** | The current API key is not authorized to perform this action. |  -  |
**404** | The specified resource was not found. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **comments_delete_post**
> AttachmentsDeletePost200Response comments_delete_post(collections_delete_post_request=collections_delete_post_request)

Delete a comment

Delete a comment

### Example

* Bearer (JWT) Authentication (http):

```python
import openapi_client
from openapi_client.models.attachments_delete_post200_response import AttachmentsDeletePost200Response
from openapi_client.models.collections_delete_post_request import CollectionsDeletePostRequest
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
    api_instance = openapi_client.CommentsApi(api_client)
    collections_delete_post_request = openapi_client.CollectionsDeletePostRequest() # CollectionsDeletePostRequest |  (optional)

    try:
        # Delete a comment
        api_response = api_instance.comments_delete_post(collections_delete_post_request=collections_delete_post_request)
        print("The response of CommentsApi->comments_delete_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CommentsApi->comments_delete_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **collections_delete_post_request** | [**CollectionsDeletePostRequest**](CollectionsDeletePostRequest.md)|  | [optional] 

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
**401** | The API key is missing or otherwise invalid. |  -  |
**403** | The current API key is not authorized to perform this action. |  -  |
**404** | The specified resource was not found. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **comments_list_post**
> CommentsListPost200Response comments_list_post(comments_list_post_request=comments_list_post_request)

List all comments

This method will list all comments matching the given properties.

### Example

* Bearer (JWT) Authentication (http):

```python
import openapi_client
from openapi_client.models.comments_list_post200_response import CommentsListPost200Response
from openapi_client.models.comments_list_post_request import CommentsListPostRequest
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
    api_instance = openapi_client.CommentsApi(api_client)
    comments_list_post_request = openapi_client.CommentsListPostRequest() # CommentsListPostRequest |  (optional)

    try:
        # List all comments
        api_response = api_instance.comments_list_post(comments_list_post_request=comments_list_post_request)
        print("The response of CommentsApi->comments_list_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CommentsApi->comments_list_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **comments_list_post_request** | [**CommentsListPostRequest**](CommentsListPostRequest.md)|  | [optional] 

### Return type

[**CommentsListPost200Response**](CommentsListPost200Response.md)

### Authorization

[http](../README.md#http)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**401** | The API key is missing or otherwise invalid. |  -  |
**403** | The current API key is not authorized to perform this action. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **comments_update_post**
> CommentsCreatePost200Response comments_update_post(comments_update_post_request=comments_update_post_request)

Update a comment

Update a comment

### Example

* Bearer (JWT) Authentication (http):

```python
import openapi_client
from openapi_client.models.comments_create_post200_response import CommentsCreatePost200Response
from openapi_client.models.comments_update_post_request import CommentsUpdatePostRequest
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
    api_instance = openapi_client.CommentsApi(api_client)
    comments_update_post_request = openapi_client.CommentsUpdatePostRequest() # CommentsUpdatePostRequest |  (optional)

    try:
        # Update a comment
        api_response = api_instance.comments_update_post(comments_update_post_request=comments_update_post_request)
        print("The response of CommentsApi->comments_update_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CommentsApi->comments_update_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **comments_update_post_request** | [**CommentsUpdatePostRequest**](CommentsUpdatePostRequest.md)|  | [optional] 

### Return type

[**CommentsCreatePost200Response**](CommentsCreatePost200Response.md)

### Authorization

[http](../README.md#http)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**401** | The API key is missing or otherwise invalid. |  -  |
**403** | The current API key is not authorized to perform this action. |  -  |
**404** | The specified resource was not found. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

