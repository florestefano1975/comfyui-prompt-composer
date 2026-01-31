# PROMPT COMPOSER TOOLS
# Created by AI Wiz Art (Stefano Flore)
# Version: 1.7
# https://stefanoflore.it
# https://ai-wiz.art

import os

from .nodes.custom_lists import PromptComposerCustomLists
from .nodes.effect import PromptComposerEffect
from .nodes.styler import PromptComposerStyler
from .nodes.text_multiple import PromptComposerTextMultiple
from .nodes.text_single import PromptComposerTextSingle
from .nodes.grouping import PromptComposerGrouping
from .nodes.merge import PromptComposerMerge
from .nodes.list_folders import create_list_folders_class
from .nodes import utils

# Setup vars
script_dir = os.path.dirname(__file__)

NODE_CLASS_MAPPINGS = {
    # Fixed nodes (classes only, no args)
    "PromptComposerCustomLists": PromptComposerCustomLists,
    "PromptComposerStyler": PromptComposerStyler,
    "PromptComposerEffect": PromptComposerEffect,

    # Unchanged nodes
    "PromptComposerTextSingle": PromptComposerTextSingle,
    "promptComposerTextMultiple": PromptComposerTextMultiple,
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
sub_custom_lists = utils.sub_custom_lists(
    os.path.join(script_dir, "custom-lists")
)

for folder_name, widget_data in sub_custom_lists.items():
    class_name = "PromptComposerListFolders" + folder_name.capitalize()
    new_class = create_list_folders_class(class_name, widget_data)

    # Classes only — still correct here
    NODE_CLASS_MAPPINGS[class_name] = new_class
    NODE_DISPLAY_NAME_MAPPINGS[class_name] = (
        f"Prompt Composer List - {folder_name.capitalize()}"
    )
