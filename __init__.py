# PROMPT COMPOSER TOOLS
# Created by AI Wiz Art (Stefano Flore)
# Version: 1.6
# https://stefanoflore.it
# https://ai-wiz.art

# Weight min, max and step values
WEIGHT_MIN = 0
WEIGHT_MAX = 1.95
WEIGHT_STEP = 0.05

# Weight display format (number or slider)
WEIGHT_DISPLAY = "slider"

######## DO NOT MODIFY BELOW THIS LINE ########

import os

WEIGHT_LABEL_SUFFIX = " (weight)"

script_dir = os.path.dirname(__file__)

# Read txt file

def pmReadTxt(file_path):
    with open(file_path, 'r') as file:
        lines = file.readlines()
        values = [line.strip() for line in lines]

        return values

# Custom lists

def customLists(folder):
    custom_lists = {}

    for filename in os.listdir(folder):
        filepath = os.path.join(folder, filename)

        if os.path.isfile(filepath) and filename.lower().endswith('.txt'):
            values = pmReadTxt(folder + "/" + filename)
            values = ['-'] + values

            filename = os.path.splitext(filename)[0]

            custom_lists[str(filename)] = (values, { "default" : values[0]})
            custom_lists[str(filename) + WEIGHT_LABEL_SUFFIX] = ("FLOAT", {
                "default": 1,
                "min": WEIGHT_MIN,
                "max": WEIGHT_MAX,
                "step": WEIGHT_STEP,
                "display": WEIGHT_DISPLAY
            })

    custom_lists["active"] = ("BOOLEAN", {"default": True})

    return custom_lists

custom_lists = customLists(script_dir + "/custom-lists")

# Custom sublists

def subCustomLists(folder):
    sub_custom_lists = {}

    for filename in os.listdir(folder):
        folder_name = os.path.join(folder, filename)

        if os.path.isdir(folder_name):
            sub_custom_lists[filename] = customLists(folder_name)

    return sub_custom_lists

sub_custom_lists = subCustomLists(script_dir + "/custom-lists")

# Apply weight    

def applyWeight(text, weight):
    if weight == 1:
        return text
    else:
        return f"({text}:{round(weight,2)})"

# Generate prompt (used by the custom list nodes)
    
def generatePrompt(self, text_in_opt="", **kwargs):
    prompt = []

    if text_in_opt != "":
        prompt.append(text_in_opt)

    if kwargs["active"] == True:
        for key in kwargs.keys():
            if WEIGHT_LABEL_SUFFIX not in str(key) and "active" not in str(key):
                if kwargs[key] != "-" and kwargs[key + WEIGHT_LABEL_SUFFIX] > 0:
                    prompt.append(applyWeight(kwargs[key], kwargs[key + WEIGHT_LABEL_SUFFIX]))

    if len(prompt) > 0:
        prompt = ", ".join(prompt)
        prompt = prompt.lower()

        return(prompt,)
    else:
        return("",)

# Setup vars

effects = pmReadTxt(os.path.join(script_dir, "lists/effects.txt"))
effects.sort()
effects = ['-'] + effects

styles = pmReadTxt(os.path.join(script_dir, "lists/styles.txt"))
styles.sort()
styles = ['-'] + styles

# Prompt Composer Custom Lists

class PromptComposerCustomLists:
    def __init__(self):
        pass
    @classmethod
    def INPUT_TYPES(s):
        return {
            "optional": {
                "text_in_opt": ("STRING", {"forceInput": True}),
            },
            "required": custom_lists
        }
    RETURN_TYPES = ("STRING",)
    RETURN_NAMES = ("text_out",)
    FUNCTION = "generatePrompt"
    CATEGORY = "AI WizArt/Prompt Composer Tools"
    generatePrompt = generatePrompt

# Prompt Composer Single Text Node

class PromptComposerTextSingle:
    def __init__(self):
        pass
    @classmethod
    def INPUT_TYPES(s):
        return {
            "optional": {
                "text_in_opt": ("STRING", {"forceInput": True}),
            },
            "required": {
                "text": ("STRING", {
                    "multiline": True
                }),
                "weight": ("FLOAT", {
                    "default": 1,
                    "min": WEIGHT_MIN,
                    "max": WEIGHT_MAX,
                    "step": WEIGHT_STEP,
                    "display": WEIGHT_DISPLAY
                }),
                "active": ("BOOLEAN", {"default": False}),
            }
        }
    RETURN_TYPES = ("STRING",)
    RETURN_NAMES = ("text_out",)
    FUNCTION = "promptComposerTextSingle"
    CATEGORY = "AI WizArt/Prompt Composer Tools"
    def promptComposerTextSingle(self, text_in_opt="", text="", weight=0, active=True):
        prompt = []
        if text_in_opt != "":
            prompt.append(text_in_opt)
        if text != "" and weight > 0 and active:
            prompt.append(applyWeight(text, weight))
        if len(prompt) > 0:
            prompt = ", ".join(prompt)
            prompt = prompt.lower()
            return(prompt,)
        else:
            return("",)

# Prompt Composer Text Node

class promptComposerTextMultiple:
    def __init__(self):
        pass
    @classmethod
    def INPUT_TYPES(s):
        return {
            "optional": {
                "text_in_opt": ("STRING", {"forceInput": True}),
            },
            "required": {
                "text_1": ("STRING", {
                    "multiline": True
                }),
                "weight_1": ("FLOAT", {
                    "default": 1,
                    "min": WEIGHT_MIN,
                    "max": WEIGHT_MAX,
                    "step": WEIGHT_STEP,
                    "display": WEIGHT_DISPLAY
                }),
                "text_2": ("STRING", {
                    "multiline": True
                }),
                "weight_2": ("FLOAT", {
                    "default": 1,
                    "min": WEIGHT_MIN,
                    "max": WEIGHT_MAX,
                    "step": WEIGHT_STEP,
                    "display": WEIGHT_DISPLAY
                }),
                "text_3": ("STRING", {
                    "multiline": True
                }),
                "weight_3": ("FLOAT", {
                    "default": 1,
                    "min": WEIGHT_MIN,
                    "max": WEIGHT_MAX,
                    "step": WEIGHT_STEP,
                    "display": WEIGHT_DISPLAY
                }),
                "text_4": ("STRING", {
                    "multiline": True
                }),
                "weight_4": ("FLOAT", {
                    "default": 1,
                    "min": WEIGHT_MIN,
                    "max": WEIGHT_MAX,
                    "step": WEIGHT_STEP,
                    "display": WEIGHT_DISPLAY
                }),
                "text_5": ("STRING", {
                    "multiline": True
                }),
                "weight_5": ("FLOAT", {
                    "default": 1,
                    "min": WEIGHT_MIN,
                    "max": WEIGHT_MAX,
                    "step": WEIGHT_STEP,
                    "display": WEIGHT_DISPLAY
                }),
                "text_6": ("STRING", {
                    "multiline": True
                }),
                "weight_6": ("FLOAT", {
                    "default": 1,
                    "min": WEIGHT_MIN,
                    "max": WEIGHT_MAX,
                    "step": WEIGHT_STEP,
                    "display": WEIGHT_DISPLAY
                }),
                "text_7": ("STRING", {
                    "multiline": True
                }),
                "weight_7": ("FLOAT", {
                    "default": 1,
                    "min": WEIGHT_MIN,
                    "max": WEIGHT_MAX,
                    "step": WEIGHT_STEP,
                    "display": WEIGHT_DISPLAY
                }),
                "text_8": ("STRING", {
                    "multiline": True
                }),
                "weight_8": ("FLOAT", {
                    "default": 1,
                    "min": WEIGHT_MIN,
                    "max": WEIGHT_MAX,
                    "step": WEIGHT_STEP,
                    "display": WEIGHT_DISPLAY
                }),
                "text_9": ("STRING", {
                    "multiline": True
                }),
                "weight_9": ("FLOAT", {
                    "default": 1,
                    "min": WEIGHT_MIN,
                    "max": WEIGHT_MAX,
                    "step": WEIGHT_STEP,
                    "display": WEIGHT_DISPLAY
                }),
                "text_10": ("STRING", {
                    "multiline": True
                }),
                "weight_10": ("FLOAT", {
                    "default": 1,
                    "min": WEIGHT_MIN,
                    "max": WEIGHT_MAX,
                    "step": WEIGHT_STEP,
                    "display": WEIGHT_DISPLAY
                }),
                "active": ("BOOLEAN", {"default": False}),
            }
        }
    RETURN_TYPES = ("STRING",)
    RETURN_NAMES = ("text_out",)
    FUNCTION = "promptComposerTextMultiple"
    CATEGORY = "AI WizArt/Prompt Composer Tools"
    def promptComposerTextMultiple(self, text_in_opt="", text_1="", weight_1=0, text_2="", weight_2=0, text_3="", weight_3=0, text_4="", weight_4=0, text_5="", weight_5=0, text_6="", weight_6=0, text_7="", weight_7=0, text_8="", weight_8=0, text_9="", weight_9=0, text_10="", weight_10=0, active=True):
        prompt = []
        if text_in_opt != "":
            prompt.append(text_in_opt)
        if text_1 != "" and weight_1 > 0 and active:
            prompt.append(applyWeight(text_1, weight_1))
        if text_2 != "" and weight_2 > 0 and active:
            prompt.append(applyWeight(text_2, weight_2))
        if text_3 != "" and weight_3 > 0 and active:
            prompt.append(applyWeight(text_3, weight_3))
        if text_4 != "" and weight_4 > 0 and active:
            prompt.append(applyWeight(text_4, weight_4))
        if text_5 != "" and weight_5 > 0 and active:
            prompt.append(applyWeight(text_5, weight_5))
        if text_6 != "" and weight_6 > 0 and active:
            prompt.append(applyWeight(text_6, weight_6))
        if text_7 != "" and weight_7 > 0 and active:
            prompt.append(applyWeight(text_7, weight_7))
        if text_8 != "" and weight_8 > 0 and active:
            prompt.append(applyWeight(text_8, weight_8))
        if text_9 != "" and weight_9 > 0 and active:
            prompt.append(applyWeight(text_9, weight_9))
        if text_10 != "" and weight_10 > 0 and active:
            prompt.append(applyWeight(text_10, weight_10))
        if len(prompt) > 0:
            prompt = ", ".join(prompt)
            prompt = prompt.lower()
            return(prompt,)
        else:
            return("",)

# Styler Node
    
class PromptComposerStyler:
    def __init__(self):
        pass
    @classmethod
    def INPUT_TYPES(s):
        return {
            "optional": {
                "text_in_opt": ("STRING", {"forceInput": True}),
            },
            "required": {
                "style": (styles, {
                    "default": styles[0],
                }),
                "style_weight": ("FLOAT", {
                    "default": 1,
                    "step": WEIGHT_STEP,
                    "min": WEIGHT_MIN,
                    "max": WEIGHT_MAX,
                    "display": WEIGHT_DISPLAY,
                }),
                "active": ("BOOLEAN", {"default": False}),
            },
        }
    RETURN_TYPES = ("STRING",)
    RETURN_NAMES = ("text_out",)
    FUNCTION = "promptComposerStyler"
    CATEGORY = "AI WizArt/Prompt Composer Tools/Deprecated"
    def promptComposerStyler(self, text_in_opt="", style="-", style_weight=0, active=True):
        prompt = []
        if text_in_opt != "":
            prompt.append(text_in_opt)
        if style != '-' and style_weight > 0 and active:
            prompt.append(f"({style} style:{round(style_weight,2)})")
        if len(prompt) > 0:
            prompt = ", ".join(prompt)
            prompt = prompt.lower()
            return(prompt,)
        else:
            return("",)

# Effect Node
    
class PromptComposerEffect:
    def __init__(self):
        pass
    @classmethod
    def INPUT_TYPES(s):
        return {
            "optional": {
                "text_in_opt": ("STRING", {"forceInput": True}),
            },
            "required": {
                "effect": (effects, {
                    "default": effects[0],
                }),
                "effect_weight": ("FLOAT", {
                    "default": 1,
                    "step": WEIGHT_STEP,
                    "min": WEIGHT_MIN,
                    "max": WEIGHT_MAX,
                    "display": WEIGHT_DISPLAY,
                }),
                "active": ("BOOLEAN", {"default": False}),
            },
        }
    RETURN_TYPES = ("STRING",)
    RETURN_NAMES = ("text_out",)
    FUNCTION = "promptComposerEffect"
    CATEGORY = "AI WizArt/Prompt Composer Tools/Deprecated"
    def promptComposerEffect(self, text_in_opt="", effect="-", effect_weight=0, active=True):
        prompt = []
        if text_in_opt != "":
            prompt.append(text_in_opt)
        if effect != '-' and effect_weight > 0 and active:
            prompt.append(f"({effect} effect:{round(effect_weight,2)})")
        if len(prompt) > 0:
            prompt = ", ".join(prompt)
            prompt = prompt.lower()
            return(prompt,)
        else:
            return("",)

# Grouping Node
    
class PromptComposerGrouping:
    def __init__(self):
        pass
    @classmethod
    def INPUT_TYPES(s):
        return {
            "required": {
                "text_in": ("STRING", {"forceInput": True}),
                "weight": ("FLOAT", {
                    "default": 1,
                    "step": WEIGHT_STEP,
                    "min": WEIGHT_MIN,
                    "max": WEIGHT_MAX,
                    "display": WEIGHT_DISPLAY,
                }),
                "active": ("BOOLEAN", {"default": False}),
            }
        }
    RETURN_TYPES = ("STRING",)
    RETURN_NAMES = ("text_out",)
    FUNCTION = "promptComposerGrouping"
    CATEGORY = "AI WizArt/Prompt Composer Tools"
    def promptComposerGrouping(self, text_in="", weight=0, active=True):
        prompt = text_in
        if text_in != "" and weight > 0 and active:
            prompt = applyWeight(text_in, weight)
        return(prompt,)

# Merge Node
    
class PromptComposerMerge:
    def __init__(self):
        pass
    @classmethod
    def INPUT_TYPES(s):
        return {
            "required": {
                "text_a": ("STRING", {"forceInput": True}),
                "text_b": ("STRING", {"forceInput": True}),
            }
        }
    RETURN_TYPES = ("STRING",)
    RETURN_NAMES = ("text_out",)
    FUNCTION = "promptComposerMerge"
    CATEGORY = "AI WizArt/Prompt Composer Tools"
    def promptComposerMerge(self, text_a="", text_b=""):
        return(text_a + ", " + text_b,)

# Mapping

NODE_CLASS_MAPPINGS = {
    "PromptComposerCustomLists": PromptComposerCustomLists,
    "PromptComposerTextSingle": PromptComposerTextSingle,
    "promptComposerTextMultiple": promptComposerTextMultiple,
    "PromptComposerStyler": PromptComposerStyler,
    "PromptComposerEffect": PromptComposerEffect,
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

for folder_name, widget_data in sub_custom_lists.items():
    class_name = "PromptComposerListFolders" + folder_name.capitalize()
    
    class_attrs = {
        'RETURN_TYPES': ("STRING",),
        'RETURN_NAMES': ("text_out",),
        'FUNCTION': "generatePrompt",
        'CATEGORY': f"AI WizArt/Prompt Composer Tools",
        
        'INPUT_TYPES': classmethod(lambda cls: {
            "optional": {
                "text_in_opt": ("STRING", {"forceInput": True}),
            },
            "required": widget_data 
        }),
        'generatePrompt': generatePrompt
    }

    # Dynamically create the class using `type()`
    new_class = type(class_name, (object,), class_attrs)

    # Add the new class to the mappings
    NODE_CLASS_MAPPINGS[class_name] = new_class
    NODE_DISPLAY_NAME_MAPPINGS[class_name] = f"Prompt Composer List - {folder_name.capitalize()}"