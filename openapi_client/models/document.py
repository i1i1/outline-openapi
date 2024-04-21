# coding: utf-8

"""
    Outline API

    # Introduction  The Outline API is structured in an RPC style. It enables you to programatically interact with all aspects of Outline’s data – in fact, the main application is built on exactly the same API.  The API structure is available as an [openapi specification](https://github.com/outline/openapi) if that’s your jam – it can be used to generate clients for most programming languages.  # Making requests  Outline’s API follows simple RPC style conventions where each API endpoint is a method on `https://app.getoutline.com/api/method`. Both `GET` and `POST` methods are supported but it’s recommended that you make all call using POST. Only HTTPS is supported and all response payloads are JSON.  When making `POST` requests, request parameters are parsed depending on Content-Type header. To make a call using JSON payload, you must pass Content-Type: application/json header, here’s an example using CURL:  ``` curl https://app.getoutline.com/api/documents.info \\ -X 'POST' \\ -H 'authorization: Bearer MY_API_KEY' \\ -H 'content-type: application/json' \\ -H 'accept: application/json' \\ -d '{\"id\": \"outline-api-NTpezNwhUP\"}' ```  Or, with JavaScript:  ```javascript const response = await fetch(\"https://app.getoutline.com/api/documents.info\", {   method: \"POST\",   headers: {     Accept: \"application/json\",     \"Content-Type\": \"application/json\",     Authorization: \"Bearer MY_API_KEY\"   } })  const body = await response.json(); const document = body.data; ```  # Authentication  To access API endpoints, you must provide a valid API key. You can create new API keys in your [account settings](https://app.getoutline.com/settings). Be careful when handling your keys as they give access to all of your documents, you should treat them like passwords and they should never be committed to source control.  To authenticate with API, you can supply the API key as a header (`Authorization: Bearer YOUR_API_KEY`) or as part of the payload using `token` parameter. Header based authentication is highly recommended so that your keys don’t accidentally leak into logs.  Some API endpoints allow unauthenticated requests for public resources and they can be called without an API key.  # Errors  All successful API requests will be returned with a 200 or 201 status code and `ok: true` in the response payload. If there’s an error while making the request, the appropriate status code is returned with the error message:  ``` {   \"ok\": false,   \"error\": \"Not Found\" } ```  # Pagination  Most top-level API resources have support for \"list\" API methods. For instance, you can list users, documents, and collections. These list methods share common parameters, taking both `limit` and `offset`.  Responses will echo these parameters in the root `pagination` key, and also include a `nextPath` key which can be used as a handy shortcut to fetch the next page of results. For example:  ``` {   ok: true,   status: 200,   data: […],   pagination: {     limit: 25,     offset: 0,     nextPath: \"/api/documents.list?limit=25&offset=25\"   } } ```  # Policies  Most API resources have associated \"policies\", these objects describe the current API keys authorized actions related to an individual resource. It should be noted that the policy \"id\" is identical to the resource it is related to, policies themselves do not have unique identifiers.  For most usecases of the API, policies can be safely ignored. Calling unauthorized methods will result in the appropriate response code – these can be used in an interface to adjust which elements are visible. 

    The version of the OpenAPI document: 0.1.0
    Contact: hello@getoutline.com
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from datetime import datetime
from pydantic import BaseModel, ConfigDict, Field, StrictBool, StrictFloat, StrictInt, StrictStr
from typing import Any, ClassVar, Dict, List, Optional, Union
from openapi_client.models.user import User
from typing import Optional, Set
from typing_extensions import Self

class Document(BaseModel):
    """
    Document
    """ # noqa: E501
    id: Optional[StrictStr] = Field(default=None, description="Unique identifier for the object.")
    collection_id: Optional[StrictStr] = Field(default=None, description="Identifier for the associated collection.", alias="collectionId")
    parent_document_id: Optional[StrictStr] = Field(default=None, description="Identifier for the document this is a child of, if any.", alias="parentDocumentId")
    title: Optional[StrictStr] = Field(default=None, description="The title of the document.")
    full_width: Optional[StrictBool] = Field(default=None, description="Whether this document should be displayed in a full-width view.", alias="fullWidth")
    emoji: Optional[StrictStr] = Field(default=None, description="An emoji associated with the document.")
    text: Optional[StrictStr] = Field(default=None, description="The text content of the document, contains markdown formatting")
    url_id: Optional[StrictStr] = Field(default=None, description="A short unique ID that can be used to identify the document as an alternative to the UUID", alias="urlId")
    collaborators: Optional[List[User]] = None
    pinned: Optional[StrictBool] = Field(default=None, description="Whether this document is pinned in the collection")
    template: Optional[StrictBool] = Field(default=None, description="Whether this document is a template")
    template_id: Optional[StrictStr] = Field(default=None, description="Unique identifier for the template this document was created from, if any", alias="templateId")
    revision: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, description="A number that is auto incrementing with every revision of the document that is saved")
    created_at: Optional[datetime] = Field(default=None, description="The date and time that this object was created", alias="createdAt")
    created_by: Optional[User] = Field(default=None, alias="createdBy")
    updated_at: Optional[datetime] = Field(default=None, description="The date and time that this object was last changed", alias="updatedAt")
    updated_by: Optional[User] = Field(default=None, alias="updatedBy")
    published_at: Optional[datetime] = Field(default=None, description="The date and time that this object was published", alias="publishedAt")
    archived_at: Optional[datetime] = Field(default=None, description="The date and time that this object was archived", alias="archivedAt")
    deleted_at: Optional[datetime] = Field(default=None, description="The date and time that this object was deleted", alias="deletedAt")
    __properties: ClassVar[List[str]] = ["id", "collectionId", "parentDocumentId", "title", "fullWidth", "emoji", "text", "urlId", "collaborators", "pinned", "template", "templateId", "revision", "createdAt", "createdBy", "updatedAt", "updatedBy", "publishedAt", "archivedAt", "deletedAt"]

    model_config = ConfigDict(
        populate_by_name=True,
        validate_assignment=True,
        protected_namespaces=(),
    )


    def to_str(self) -> str:
        """Returns the string representation of the model using alias"""
        return pprint.pformat(self.model_dump(by_alias=True))

    def to_json(self) -> str:
        """Returns the JSON representation of the model using alias"""
        # TODO: pydantic v2: use .model_dump_json(by_alias=True, exclude_unset=True) instead
        return json.dumps(self.to_dict())

    @classmethod
    def from_json(cls, json_str: str) -> Optional[Self]:
        """Create an instance of Document from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self) -> Dict[str, Any]:
        """Return the dictionary representation of the model using alias.

        This has the following differences from calling pydantic's
        `self.model_dump(by_alias=True)`:

        * `None` is only added to the output dict for nullable fields that
          were set at model initialization. Other fields with value `None`
          are ignored.
        * OpenAPI `readOnly` fields are excluded.
        * OpenAPI `readOnly` fields are excluded.
        * OpenAPI `readOnly` fields are excluded.
        * OpenAPI `readOnly` fields are excluded.
        * OpenAPI `readOnly` fields are excluded.
        * OpenAPI `readOnly` fields are excluded.
        * OpenAPI `readOnly` fields are excluded.
        """
        excluded_fields: Set[str] = set([
            "id",
            "revision",
            "created_at",
            "updated_at",
            "published_at",
            "archived_at",
            "deleted_at",
        ])

        _dict = self.model_dump(
            by_alias=True,
            exclude=excluded_fields,
            exclude_none=True,
        )
        # override the default output from pydantic by calling `to_dict()` of each item in collaborators (list)
        _items = []
        if self.collaborators:
            for _item in self.collaborators:
                if _item:
                    _items.append(_item.to_dict())
            _dict['collaborators'] = _items
        # override the default output from pydantic by calling `to_dict()` of created_by
        if self.created_by:
            _dict['createdBy'] = self.created_by.to_dict()
        # override the default output from pydantic by calling `to_dict()` of updated_by
        if self.updated_by:
            _dict['updatedBy'] = self.updated_by.to_dict()
        # set to None if published_at (nullable) is None
        # and model_fields_set contains the field
        if self.published_at is None and "published_at" in self.model_fields_set:
            _dict['publishedAt'] = None

        # set to None if deleted_at (nullable) is None
        # and model_fields_set contains the field
        if self.deleted_at is None and "deleted_at" in self.model_fields_set:
            _dict['deletedAt'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of Document from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "id": obj.get("id"),
            "collectionId": obj.get("collectionId"),
            "parentDocumentId": obj.get("parentDocumentId"),
            "title": obj.get("title"),
            "fullWidth": obj.get("fullWidth"),
            "emoji": obj.get("emoji"),
            "text": obj.get("text"),
            "urlId": obj.get("urlId"),
            "collaborators": [User.from_dict(_item) for _item in obj["collaborators"]] if obj.get("collaborators") is not None else None,
            "pinned": obj.get("pinned"),
            "template": obj.get("template"),
            "templateId": obj.get("templateId"),
            "revision": obj.get("revision"),
            "createdAt": obj.get("createdAt"),
            "createdBy": User.from_dict(obj["createdBy"]) if obj.get("createdBy") is not None else None,
            "updatedAt": obj.get("updatedAt"),
            "updatedBy": User.from_dict(obj["updatedBy"]) if obj.get("updatedBy") is not None else None,
            "publishedAt": obj.get("publishedAt"),
            "archivedAt": obj.get("archivedAt"),
            "deletedAt": obj.get("deletedAt")
        })
        return _obj

