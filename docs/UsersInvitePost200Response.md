# UsersInvitePost200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**sent** | [**List[Invite]**](Invite.md) |  | [optional] 
**users** | [**List[User]**](User.md) |  | [optional] 

## Example

```python
from openapi_client.models.users_invite_post200_response import UsersInvitePost200Response

# TODO update the JSON string below
json = "{}"
# create an instance of UsersInvitePost200Response from a JSON string
users_invite_post200_response_instance = UsersInvitePost200Response.from_json(json)
# print the JSON string representation of the object
print(UsersInvitePost200Response.to_json())

# convert the object into a dict
users_invite_post200_response_dict = users_invite_post200_response_instance.to_dict()
# create an instance of UsersInvitePost200Response from a dict
users_invite_post200_response_form_dict = users_invite_post200_response.from_dict(users_invite_post200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


