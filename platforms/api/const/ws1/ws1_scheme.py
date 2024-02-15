from cores.const.__const import Const


class CustomerScheme(Const):
    CreateCustomerSuccessScheme = {
        "type": "object",
        "properties": {
            "id": {"type": "string"},
            "status": {"type": "string"},
            "identifiers": {
                "type": "array",
                "items": {
                    "identifier_type": {"type": "string"},
                    "identifier": {"type": "string"}
                }
            },
            "customer_details": {
                "type": "object",
                "properties": {
                    "title": {"type": "string"},
                    "first_name": {"type": "string"},
                    "middle_name": {"type": "string"},
                    "last_name": {"type": "string"},
                    "dob": {"type": "string"},
                    "gender": {"type": "string"},
                    "nationality": {"type": "string"},
                    "email_address": {"type": "string"},
                    "mobile_phone_number": {"type": "string"},
                    "home_phone_number": {"type": "string"},
                    "business_phone_number": {"type": "string"},
                    "contact_method": {"type": "string"},
                    "country_of_residence": {"type": "string"},
                    "country_of_taxation": {"type": "string"},
                    "accessibility": {"type": "string"},
                    "external_customer_id": {"type": "string"}
                }
            },
            "additional_details": {
                "type": "object",
                "properties": {}
            }
        },
        "required": ["id", "status", "identifiers", "customer_details"]
    }
