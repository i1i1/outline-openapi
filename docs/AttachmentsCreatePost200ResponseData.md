# AttachmentsCreatePost200ResponseData


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**max_upload_size** | **float** |  | [optional] 
**upload_url** | **str** |  | [optional] 
**form** | **object** |  | [optional] 
**attachment** | [**Attachment**](Attachment.md) |  | [optional] 

## Example

```python
from openapi_client.models.attachments_create_post200_response_data import AttachmentsCreatePost200ResponseData

# TODO update the JSON string below
json = "{}"
# create an instance of AttachmentsCreatePost200ResponseData from a JSON string
attachments_create_post200_response_data_instance = AttachmentsCreatePost200ResponseData.from_json(json)
# print the JSON string representation of the object
print(AttachmentsCreatePost200ResponseData.to_json())

# convert the object into a dict
attachments_create_post200_response_data_dict = attachments_create_post200_response_data_instance.to_dict()
# create an instance of AttachmentsCreatePost200ResponseData from a dict
attachments_create_post200_response_data_form_dict = attachments_create_post200_response_data.from_dict(attachments_create_post200_response_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


