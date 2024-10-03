from typing import Dict, Type
from . import utils

def create_list_folders_class(class_name: str, node_data: Dict[str, dict]) -> Type[object]:
    """
    Dynamically create a custom list class (node)

    Args:
        class_name (str): The name of the class to be created.
        node_data (dict): A dictionary containing the data to be used in the node.

    Returns:
        type: A dynamically created class with the specified name and attributes.
    """    
    class_attrs = {
        'RETURN_TYPES': ("STRING",),
        'RETURN_NAMES': ("text_out",),
        'FUNCTION': "generatePrompt",
        'CATEGORY': f"AI WizArt/Prompt Composer Tools",
        
        'INPUT_TYPES': classmethod(lambda cls, node_data=node_data: {
            "optional": {
                "text_in_opt": ("STRING", {"forceInput": True}),
            },
            "required": node_data
        }),
        'generatePrompt': utils.generate_prompt
    }

    # Dynamically create the class using `type()` and return it
    return type(class_name, (object,), class_attrs)