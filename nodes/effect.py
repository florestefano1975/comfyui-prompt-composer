import os
from . import utils

# Effect Node
class PromptComposerEffect:
    RETURN_TYPES = ("STRING",)
    RETURN_NAMES = ("text_out",)
    FUNCTION = "promptComposerEffect"
    CATEGORY = "AI WizArt/Prompt Composer Tools/Deprecated"

    effects = None

    def __init__(self, script_dir: str):        
        effects = utils.read_words_from_file(os.path.join(script_dir, "lists/effects.txt"))

        effects.sort()
        
        effects = ['-'] + effects

        PromptComposerEffect.effects = effects

    @classmethod
    def INPUT_TYPES(s):
        return {
            "optional": {
                "text_in_opt": ("STRING", {"forceInput": True}),
            },
            "required": {
                "effect": (s.effects, {
                    "default": s.effects[0],
                }),
                "effect_weight": ("FLOAT", {
                    "default": 1,
                    "step": utils.WEIGHT_STEP,
                    "min": utils.WEIGHT_MIN,
                    "max": utils.WEIGHT_MAX,
                    "display": utils.WEIGHT_DISPLAY,
                }),
                "active": ("BOOLEAN", {"default": False}),
            },
        }

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