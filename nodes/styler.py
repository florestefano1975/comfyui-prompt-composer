import os
from . import utils

# Styler Node
class PromptComposerStyler:
    RETURN_TYPES = ("STRING",)
    RETURN_NAMES = ("text_out",)
    FUNCTION = "promptComposerStyler"
    CATEGORY = "AI WizArt/Prompt Composer Tools/Deprecated"

    styles = None

    def __init__(self, script_dir: str):
        styles = utils.read_words_from_file(os.path.join(script_dir, "lists/styles.txt"))

        styles.sort()

        styles = ['-'] + styles

        PromptComposerStyler.styles = styles

    @classmethod
    def INPUT_TYPES(s):
        return {
            "optional": {
                "text_in_opt": ("STRING", {"forceInput": True}),
            },
            "required": {
                "style": (s.styles, {
                    "default": s.styles[0],
                }),
                "style_weight": ("FLOAT", {
                    "default": 1,
                    "step": utils.WEIGHT_STEP,
                    "min": utils.WEIGHT_MIN,
                    "max": utils.WEIGHT_MAX,
                    "display": utils.WEIGHT_DISPLAY,
                }),
                "active": ("BOOLEAN", {"default": False}),
            },
        }
    
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
