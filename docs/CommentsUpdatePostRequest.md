# CommentsUpdatePostRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | 
**data** | **object** |  | 

## Example

```python
from openapi_client.models.comments_update_post_request import CommentsUpdatePostRequest

# TODO update the JSON string below
json = "{}"
# create an instance of CommentsUpdatePostRequest from a JSON string
comments_update_post_request_instance = CommentsUpdatePostRequest.from_json(json)
# print the JSON string representation of the object
print(CommentsUpdatePostRequest.to_json())

# convert the object into a dict
comments_update_post_request_dict = comments_update_post_request_instance.to_dict()
# create an instance of CommentsUpdatePostRequest from a dict
comments_update_post_request_form_dict = comments_update_post_request.from_dict(comments_update_post_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


