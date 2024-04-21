# CommentsListPost200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**List[Document]**](Document.md) |  | [optional] 
**policies** | [**List[Policy]**](Policy.md) |  | [optional] 
**pagination** | [**Pagination**](Pagination.md) |  | [optional] 

## Example

```python
from openapi_client.models.comments_list_post200_response import CommentsListPost200Response

# TODO update the JSON string below
json = "{}"
# create an instance of CommentsListPost200Response from a JSON string
comments_list_post200_response_instance = CommentsListPost200Response.from_json(json)
# print the JSON string representation of the object
print(CommentsListPost200Response.to_json())

# convert the object into a dict
comments_list_post200_response_dict = comments_list_post200_response_instance.to_dict()
# create an instance of CommentsListPost200Response from a dict
comments_list_post200_response_form_dict = comments_list_post200_response.from_dict(comments_list_post200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


