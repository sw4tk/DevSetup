
def profile_validator(profile):
    required = ['name','description','tools']
    for key in required:
        if key not in profile:
            raise ValueError(f"Profile is missing required field: {key}")
        
    if not profile['name'].strip():
        raise ValueError("Profile 'name' field cannot be empty")

    if not profile['description'].strip():
        raise ValueError("Profile 'description' field cannot be empty")
        
    if not isinstance(profile['name'], str):
        raise ValueError("Profile 'name' field must be a string")

    if not isinstance(profile['description'], str):
        raise ValueError("Profile 'description' field must be a string")

    if not isinstance(profile['tools'], list):
        raise ValueError("Profile 'tools' field must be a list")
    
    if len(profile['tools']) == 0:
        raise ValueError("Profile must contain at least one tool")
    
    for tool in profile['tools']:
        if not isinstance(tool, str):
            raise ValueError("Profile 'tools' field must contain only strings")
