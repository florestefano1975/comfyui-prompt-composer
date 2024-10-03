from . import utils

# Prompt Composer Custom Lists
def createListFoldersClass(class_name, widget_data):
    class_attrs = {
        'RETURN_TYPES': ("STRING",),
        'RETURN_NAMES': ("text_out",),
        'FUNCTION': "generatePrompt",
        'CATEGORY': f"AI WizArt/Prompt Composer Tools",
        
        'INPUT_TYPES': classmethod(lambda cls, widget_data=widget_data: {
            "optional": {
                "text_in_opt": ("STRING", {"forceInput": True}),
            },
            "required": widget_data
        }),
        'generatePrompt': utils.generatePrompt
    }

    # Dynamically create the class using `type()`
    return type(class_name, (object,), class_attrs)