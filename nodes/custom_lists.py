from . import utils

# Prompt Composer Custom Lists
class PromptComposerCustomLists:
    RETURN_TYPES = ("STRING",)
    RETURN_NAMES = ("text_out",)
    FUNCTION = "generatePrompt"
    CATEGORY = "AI WizArt/Prompt Composer Tools"

    generatePrompt = utils.generate_prompt
    custom_lists  = None

    def __init__(self, script_dir: str):
        PromptComposerCustomLists.custom_lists  = utils.custom_lists(script_dir + "/custom-lists")

    @classmethod
    def INPUT_TYPES(s):
        return {
            "optional": {
                "text_in_opt": ("STRING", {"forceInput": True}),
            },
            "required": s.custom_lists
        }