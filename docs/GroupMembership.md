# GroupMembership


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Unique identifier for the object. | [optional] [readonly] 
**group_id** | **str** | Identifier for the associated group. | [optional] [readonly] 
**user_id** | **str** | Identifier for the associated user. | [optional] [readonly] 
**user** | [**User**](User.md) |  | [optional] 

## Example

```python
from openapi_client.models.group_membership import GroupMembership

# TODO update the JSON string below
json = "{}"
# create an instance of GroupMembership from a JSON string
group_membership_instance = GroupMembership.from_json(json)
# print the JSON string representation of the object
print(GroupMembership.to_json())

# convert the object into a dict
group_membership_dict = group_membership_instance.to_dict()
# create an instance of GroupMembership from a dict
group_membership_form_dict = group_membership.from_dict(group_membership_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


