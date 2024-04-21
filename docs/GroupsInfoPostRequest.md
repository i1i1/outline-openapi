# GroupsInfoPostRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Unique identifier for the group. | 

## Example

```python
from openapi_client.models.groups_info_post_request import GroupsInfoPostRequest

# TODO update the JSON string below
json = "{}"
# create an instance of GroupsInfoPostRequest from a JSON string
groups_info_post_request_instance = GroupsInfoPostRequest.from_json(json)
# print the JSON string representation of the object
print(GroupsInfoPostRequest.to_json())

# convert the object into a dict
groups_info_post_request_dict = groups_info_post_request_instance.to_dict()
# create an instance of GroupsInfoPostRequest from a dict
groups_info_post_request_form_dict = groups_info_post_request.from_dict(groups_info_post_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


