import os
from . import utils

class PromptComposerEffect:
    RETURN_TYPES = ("STRING",)
    RETURN_NAMES = ("text_out",)
    FUNCTION = "promptComposerEffect"
    CATEGORY = "AI WizArt/Prompt Composer Tools/Deprecated"

    effects = None

    @classmethod
    def INPUT_TYPES(cls):
        if cls.effects is None:
            base_dir = os.path.dirname(os.path.dirname(__file__))
            effects = utils.read_words_from_file(
                os.path.join(base_dir, "lists", "effects.txt")
            )

            effects.sort()
            cls.effects = ['-'] + effects

        return {
            "optional": {
                "text_in_opt": ("STRING", {"forceInput": True}),
            },
            "required": {
                "effect": (cls.effects, {"default": cls.effects[0]}),
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

        if text_in_opt:
            prompt.append(text_in_opt)
        if effect != '-' and effect_weight > 0 and active:
            prompt.append(f"({effect} effect:{round(effect_weight, 2)})")

        if prompt:
            return (", ".join(prompt).lower(),)
        return ("",)
