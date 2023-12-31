# PROMPT COMPOSER TOOLS
# Created by AI Wiz Art (Stefano Flore)
# Version: 1.3
# https://stefanoflore.it
# https://ai-wiz.art

import os

script_dir = os.path.dirname(__file__)

# Read txt file

def pmReadTxt(file_path):
    with open(file_path, 'r') as file:
        lines = file.readlines()
        values = [line.strip() for line in lines]
        return values

# Apply weight
    
def applyWeight(text, weight):
    if weight == 1:
        return text
    else:
        return f"({text}:{round(weight,2)})"

# Setup vars

effects = pmReadTxt(os.path.join(script_dir, "lists/effects.txt"))
effects.sort()
effects = ['-'] + effects

styles = pmReadTxt(os.path.join(script_dir, "lists/styles.txt"))
styles.sort()
styles = ['-'] + styles

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
                    "min": 0,
                    "max": 1.95,
                    "step": 0.05,
                    "display": "slider"
                }),
            }
        }
    RETURN_TYPES = ("STRING",)
    RETURN_NAMES = ("text_out",)
    FUNCTION = "promptComposerTextSingle"
    CATEGORY = "AI WizArt/Prompt Composer Tools"
    def promptComposerTextSingle(self, text_in_opt="", text="", weight=0):
        prompt = []
        if text_in_opt != "":
            prompt.append(text_in_opt)
        if text != "" and weight > 0:
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
                    "min": 0,
                    "max": 1.95,
                    "step": 0.05,
                    "display": "slider"
                }),
                "text_2": ("STRING", {
                    "multiline": True
                }),
                "weight_2": ("FLOAT", {
                    "default": 1,
                    "min": 0,
                    "max": 1.95,
                    "step": 0.05,
                    "display": "slider"
                }),
                "text_3": ("STRING", {
                    "multiline": True
                }),
                "weight_3": ("FLOAT", {
                    "default": 1,
                    "min": 0,
                    "max": 1.95,
                    "step": 0.05,
                    "display": "slider"
                }),
                "text_4": ("STRING", {
                    "multiline": True
                }),
                "weight_4": ("FLOAT", {
                    "default": 1,
                    "min": 0,
                    "max": 1.95,
                    "step": 0.05,
                    "display": "slider"
                }),
                "text_5": ("STRING", {
                    "multiline": True
                }),
                "weight_5": ("FLOAT", {
                    "default": 1,
                    "min": 0,
                    "max": 1.95,
                    "step": 0.05,
                    "display": "slider"
                }),
                "text_6": ("STRING", {
                    "multiline": True
                }),
                "weight_6": ("FLOAT", {
                    "default": 1,
                    "min": 0,
                    "max": 1.95,
                    "step": 0.05,
                    "display": "slider"
                }),
            }
        }
    RETURN_TYPES = ("STRING",)
    RETURN_NAMES = ("text_out",)
    FUNCTION = "promptComposerTextMultiple"
    CATEGORY = "AI WizArt/Prompt Composer Tools"
    def promptComposerTextMultiple(self, text_in_opt="", text_1="", weight_1=0, text_2="", weight_2=0, text_3="", weight_3=0, text_4="", weight_4=0, text_5="", weight_5=0, text_6="", weight_6=0):
        prompt = []
        if text_in_opt != "":
            prompt.append(text_in_opt)
        if text_1 != "" and weight_1 > 0:
            prompt.append(applyWeight(text_1, weight_1))
        if text_2 != "" and weight_2 > 0:
            prompt.append(applyWeight(text_2, weight_2))
        if text_3 != "" and weight_3 > 0:
            prompt.append(applyWeight(text_3, weight_3))
        if text_4 != "" and weight_4 > 0:
            prompt.append(applyWeight(text_4, weight_4))
        if text_5 != "" and weight_5 > 0:
            prompt.append(applyWeight(text_5, weight_5))
        if text_6 != "" and weight_3 > 0:
            prompt.append(applyWeight(text_6, weight_6))
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
                    "step": 0.05,
                    "min": 0,
                    "max": 1.95,
                    "display": "slider",
                }),
            },
        }
    RETURN_TYPES = ("STRING",)
    RETURN_NAMES = ("text_out",)
    FUNCTION = "promptComposerStyler"
    CATEGORY = "AI WizArt/Prompt Composer Tools"
    def promptComposerStyler(self, text_in_opt="", style="-", style_weight=0):
        prompt = []
        if text_in_opt != "":
            prompt.append(text_in_opt)
        if style != '-' and style_weight > 0:
            prompt.append(f"({style} style, {style} photography:{round(style_weight,2)})")
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
                    "step": 0.05,
                    "min": 0,
                    "max": 1.95,
                    "display": "slider",
                }),
            },
        }
    RETURN_TYPES = ("STRING",)
    RETURN_NAMES = ("text_out",)
    FUNCTION = "promptComposerEffect"
    CATEGORY = "AI WizArt/Prompt Composer Tools"
    def promptComposerEffect(self, text_in_opt="", effect="-", effect_weight=0):
        prompt = []
        if text_in_opt != "":
            prompt.append(text_in_opt)
        if effect != '-' and effect_weight > 0:
            prompt.append(f"({effect} effect:{round(effect_weight,2)})")
        if len(prompt) > 0:
            prompt = ", ".join(prompt)
            prompt = prompt.lower()
            return(prompt,)
        else:
            return("",)

# Merge Node
    
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
                    "step": 0.05,
                    "min": 0,
                    "max": 1.95,
                    "display": "slider",
                }),
            }
        }
    RETURN_TYPES = ("STRING",)
    RETURN_NAMES = ("text_out",)
    FUNCTION = "promptComposerGrouping"
    CATEGORY = "AI WizArt/Prompt Composer Tools"
    def promptComposerGrouping(self, text_in="", weight=0):
        prompt = ""
        if text_in != "" and weight > 0:
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
    "PromptComposerTextSingle": PromptComposerTextSingle,
    "promptComposerTextMultiple": promptComposerTextMultiple,
    "PromptComposerStyler": PromptComposerStyler,
    "PromptComposerEffect": PromptComposerEffect,
    "PromptComposerGrouping": PromptComposerGrouping,
    "PromptComposerMerge": PromptComposerMerge,
}

NODE_DISPLAY_NAME_MAPPINGS = {
    "PromptComposerTextSingle": "Prompt Composer Single Text",
    "promptComposerTextMultiple": "Prompt Composer Multiple Text",
    "PromptComposerStyler": "Prompt Composer Styler",
    "PromptComposerEffect": "Prompt Composer Effect",
    "PromptComposerGrouping": "Prompt Composer Grouping",
    "PromptComposerMerge": "Prompt Composer Merge",
}
