# PROMPT COMPOSER TOOLS
# Created by AI Wiz Art (Stefano Flore)
# Version: 1.6
# https://stefanoflore.it
# https://ai-wiz.art
import os

from .nodes.custom_lists import PromptComposerCustomLists
from .nodes.effect import PromptComposerEffect
from .nodes.styler import PromptComposerStyler
from .nodes.text_multiple import promptComposerTextMultiple
from .nodes.text_single import PromptComposerTextSingle
from .nodes.grouping import PromptComposerGrouping
from .nodes.merge import PromptComposerMerge
from .nodes import utils

# Setup vars
script_dir = os.path.dirname(__file__)

NODE_CLASS_MAPPINGS = {
    "PromptComposerCustomLists": PromptComposerCustomLists(script_dir),
    "PromptComposerTextSingle": PromptComposerTextSingle,
    "promptComposerTextMultiple": promptComposerTextMultiple,
    "PromptComposerStyler": PromptComposerStyler(script_dir),
    "PromptComposerEffect": PromptComposerEffect(script_dir),
    "PromptComposerGrouping": PromptComposerGrouping,
    "PromptComposerMerge": PromptComposerMerge,
}

NODE_DISPLAY_NAME_MAPPINGS = {
    "PromptComposerCustomLists": "Prompt Composer Custom Lists",
    "PromptComposerTextSingle": "Prompt Composer Single Text",
    "promptComposerTextMultiple": "Prompt Composer Multiple Text",
    "PromptComposerStyler": "Prompt Composer Styler (deprecated!)",
    "PromptComposerEffect": "Prompt Composer Effect (deprecated!)",
    "PromptComposerGrouping": "Prompt Composer Grouping",
    "PromptComposerMerge": "Prompt Composer Merge",
}

# Generate the widgets for each folder of custom lists
sub_custom_lists = utils.subCustomLists(script_dir + "/custom-lists")

for folder_name, widget_data in sub_custom_lists.items():
    class_name = "PromptComposerListFolders" + folder_name.capitalize()
    
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
    new_class = type(class_name, (object,), class_attrs)

    # Add the new class to the mappings
    NODE_CLASS_MAPPINGS[class_name] = new_class
    NODE_DISPLAY_NAME_MAPPINGS[class_name] = f"Prompt Composer List - {folder_name.capitalize()}"