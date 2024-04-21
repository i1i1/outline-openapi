# GroupsListPost200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**List[Group]**](Group.md) |  | [optional] 
**pagination** | [**Pagination**](Pagination.md) |  | [optional] 

## Example

```python
from openapi_client.models.groups_list_post200_response import GroupsListPost200Response

# TODO update the JSON string below
json = "{}"
# create an instance of GroupsListPost200Response from a JSON string
groups_list_post200_response_instance = GroupsListPost200Response.from_json(json)
# print the JSON string representation of the object
print(GroupsListPost200Response.to_json())

# convert the object into a dict
groups_list_post200_response_dict = groups_list_post200_response_instance.to_dict()
# create an instance of GroupsListPost200Response from a dict
groups_list_post200_response_form_dict = groups_list_post200_response.from_dict(groups_list_post200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


