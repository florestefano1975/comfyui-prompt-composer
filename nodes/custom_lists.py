from . import utils
import os

class PromptComposerCustomLists:
    RETURN_TYPES = ("STRING",)
    RETURN_NAMES = ("text_out",)
    FUNCTION = "generatePrompt"
    CATEGORY = "AI WizArt/Prompt Composer Tools"

    generatePrompt = utils.generate_prompt
    custom_lists = None

    @classmethod
    def INPUT_TYPES(cls):
        if cls.custom_lists is None:
            base_dir = os.path.dirname(os.path.dirname(__file__))
            cls.custom_lists = utils.custom_lists(
                os.path.join(base_dir, "custom-lists")
            )

        return {
            "optional": {
                "text_in_opt": ("STRING", {"forceInput": True}),
            },
            "required": cls.custom_lists
        }
