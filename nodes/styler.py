import os
from . import utils

class PromptComposerStyler:
    RETURN_TYPES = ("STRING",)
    RETURN_NAMES = ("text_out",)
    FUNCTION = "promptComposerStyler"
    CATEGORY = "AI WizArt/Prompt Composer Tools/Deprecated"

    styles = None

    @classmethod
    def INPUT_TYPES(cls):
        if cls.styles is None:
            base_dir = os.path.dirname(os.path.dirname(__file__))
            styles = utils.read_words_from_file(
                os.path.join(base_dir, "lists", "styles.txt")
            )

            styles.sort()
            cls.styles = ['-'] + styles

        return {
            "optional": {
                "text_in_opt": ("STRING", {"forceInput": True}),
            },
            "required": {
                "style": (cls.styles, {"default": cls.styles[0]}),
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

        if text_in_opt:
            prompt.append(text_in_opt)
        if style != '-' and style_weight > 0 and active:
            prompt.append(f"({style} style:{round(style_weight, 2)})")

        if prompt:
            return (", ".join(prompt).lower(),)
        return ("",)
