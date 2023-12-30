# PROMPT COMPOSER TOOLS
# Created by AI Wiz Art (Stefano Flore)
# Version: 1.1
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
                "text_in_opt": ("TUPLE",),
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
    RETURN_TYPES = ("TUPLE",)
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
                "text_in_opt": ("TUPLE",),
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
    RETURN_TYPES = ("TUPLE",)
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
                "text_in_opt": ("TUPLE",),
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
    RETURN_TYPES = ("TUPLE",)
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
                "text_in_opt": ("TUPLE",),
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
    RETURN_TYPES = ("TUPLE",)
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

# Assembler Node
    
class PromptComposerAssembler:
    def __init__(self):
        pass
    @classmethod
    def INPUT_TYPES(s):
        return {
            "required": {},
            "optional": {
                "text_1": ("TUPLE",),
                "text_2": ("TUPLE",),
                "text_3": ("TUPLE",),
                "text_4": ("TUPLE",),
                "text_5": ("TUPLE",),
                "text_6": ("TUPLE",),
            }
        }
    RETURN_TYPES = ("STRING",)
    RETURN_NAMES = ("text_out",)
    FUNCTION = "promptComposerAssembler"
    CATEGORY = "AI WizArt/Prompt Composer Tools"
    def promptComposerAssembler(self, text_1="", text_2="", text_3="", text_4="", text_5="", text_6=""):
        prompt = []
        if text_1 != "":
            prompt.append(text_1)
        if text_2 != "":
            prompt.append(text_2)
        if text_3 != "":
            prompt.append(text_3)
        if text_4 != "":
            prompt.append(text_4)
        if text_5 != "":
            prompt.append(text_5)
        if text_6 != "":
            prompt.append(text_6)
        prompt = ", ".join(prompt)
        prompt = prompt.lower()
        return(prompt,)

# Mapping

NODE_CLASS_MAPPINGS = {
    "PromptComposerTextSingle": PromptComposerTextSingle,
    "promptComposerTextMultiple": promptComposerTextMultiple,
    "PromptComposerStyler": PromptComposerStyler,
    "PromptComposerEffect": PromptComposerEffect,
    "PromptComposerAssembler": PromptComposerAssembler,
}

NODE_DISPLAY_NAME_MAPPINGS = {
    "PromptComposerTextSingle": "Prompt Composer Single Text",
    "promptComposerTextMultiple": "Prompt Composer Multiple Text",
    "PromptComposerStyler": "Prompt Composer Styler",
    "PromptComposerEffect": "Prompt Composer Effect",
    "PromptComposerAssembler": "Prompt Composer Assembler",
}
